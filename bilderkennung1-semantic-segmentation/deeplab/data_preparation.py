import os
import shutil
import random
import numpy as np
import cv2
from imutils import paths

# Paths where the dataset is downloaded
inputPath = r"/Users/e/Downloads/headsegmentation_dataset_ccncsa/samples"
labelsPath = r"/Users/e/Downloads/headsegmentation_dataset_ccncsa/labels"

# New folder where the cleaned up and organized dataset is placed
outputPath = r"/Users/e/Desktop/samplesArranged"
finalPath = r"/Users/e/Desktop/dataset"
subSamplesPath = r"/Users/e/Desktop/dataset/subsamples"


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# Step 1: Look at folder arrangement
labelsDist = sorted([f for f in os.listdir(labelsPath) if f != '.DS_Store'])

# Creating folders in output directory
for folder in labelsDist:
    create_directory(os.path.join(outputPath, folder))

# Step 2: Dataset can be grouped into 4 categories as below
folderTypes = {"female": [], "male": [], "multiperson": [], "real": []}

for folder in os.listdir(inputPath):
    if folder == '.DS_Store':
        continue
    if folder.startswith("female"):
        folderTypes["female"].append(folder)
        destFolder = folder.split("_")[0]
    elif folder.startswith("multiperson"):
        folderTypes["multiperson"].append(folder)
        destFolder = folder.split("_")[0]
    elif folder.startswith("male"):
        folderTypes["male"].append(folder)
        destFolder = folder.split("_")[0] if "nolight" not in folder else folder.split("_")[0] + "_2"
    else:
        if folder.startswith("real"):
            destFolder = "real"

    if os.path.isdir(os.path.join(outputPath, destFolder)):
        for file in os.listdir(os.path.join(inputPath, folder)):
            if file == '.DS_Store':
                continue
            shutil.copy(os.path.join(inputPath, folder, file), os.path.join(outputPath, destFolder, file))

# Step 3: Look at the distribution of images in each folder
for folder in labelsDist:
    if len(os.listdir(os.path.join(labelsPath, folder))) != len(os.listdir(os.path.join(outputPath, folder))):
        print(folder, len(os.listdir(os.path.join(labelsPath, folder))),
              len(os.listdir(os.path.join(outputPath, folder))))

# Step 4: Move Dataset to a single folder
create_directory(os.path.join(finalPath, "images"))
create_directory(os.path.join(finalPath, "masks"))

for folder in labelsDist:
    image_folder = os.path.join(outputPath, folder)
    mask_folder = os.path.join(labelsPath, folder)
    for file in os.listdir(image_folder):
        if file == '.DS_Store':
            continue
        imagePath = os.path.join(image_folder, file)
        maskPath = os.path.join(mask_folder, file)
        if os.path.exists(maskPath):  # Ensure the corresponding mask exists
            shutil.copy(imagePath, os.path.join(finalPath, "images", folder + "_" + file))
            shutil.copy(maskPath, os.path.join(finalPath, "masks", folder + "_" + file))


def dhash(image, hashSize=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


imagePaths = list(paths.list_images(os.path.join(finalPath, "images")))
hashes = {}
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    h = dhash(image)
    p = hashes.get(h, [])
    p.append(imagePath)
    hashes[h] = p

remove = True

for (h, hashedPaths) in hashes.items():
    if len(hashedPaths) > 1:
        if not remove:
            montage = None
            for p in hashedPaths:
                image = cv2.imread(p)
                image = cv2.resize(image, (150, 150))
                if montage is None:
                    montage = image
                else:
                    montage = np.hstack([montage, image])
            print("[INFO] hash: {}".format(h))
            cv2.imshow("Montage", montage)
            cv2.waitKey(0)
        else:
            for p in hashedPaths[1:]:
                os.remove(p)
                os.remove(p.replace("/images/", "/masks/"))

oldFolders = {}
for imageFile, maskFile in zip(os.listdir(os.path.join(finalPath, "images")),
                               os.listdir(os.path.join(finalPath, "masks"))):
    if imageFile == maskFile:
        key = imageFile.split("_")[0]
        oldFolders[key] = oldFolders.get(key, 0) + 1
    else:
        print(imageFile)

addedFiles = {k: 0 for k in oldFolders.keys()}
allImages = os.listdir(os.path.join(finalPath, "images"))
random.shuffle(allImages)

for image in allImages:
    key = image.split("_")[0]
    if key == "real" or (key == "multiperson" and addedFiles[key] < 50) or addedFiles[key] < 10:
        addedFiles[key] += 1
        shutil.copy(os.path.join(finalPath, "images", image), os.path.join(subSamplesPath, "images", image))
        shutil.copy(os.path.join(finalPath, "masks", image), os.path.join(subSamplesPath, "masks", image))

newFolders = {}
for imageFile, maskFile in zip(os.listdir(os.path.join(subSamplesPath, "images")),
                               os.listdir(os.path.join(subSamplesPath, "masks"))):
    if imageFile == maskFile:
        key = imageFile.split("_")[0]
        newFolders[key] = newFolders.get(key, 0) + 1
    else:
        print(imageFile)

print("NEW DISTRIBUTION OF SAMPLES: ", len(os.listdir(os.path.join(subSamplesPath, "images"))))
print(newFolders)

