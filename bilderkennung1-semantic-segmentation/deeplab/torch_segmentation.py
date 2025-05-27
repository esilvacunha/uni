import cv2
import pandas as pd
import time

import torch
from matplotlib import pyplot as plt

model_path = "/Users/e/Desktop/results/weights.pt"
image_path = "/Users/e/Desktop/Master/2. Semester/BIld/Semantic Segmentation/Bilder/iStock/C3.jpg"

# Load the trained model
if torch.cuda.is_available():
    model = torch.load(model_path)
else:
    model = torch.load(model_path, map_location=torch.device('cpu'))

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
# Set the model to evaluate mode
model.eval()

# Read a sample image and mask from the data-set
originalImage = cv2.imread(image_path)

# Resize image
img = cv2.resize(originalImage, (256, 256), cv2.INTER_AREA).transpose(2, 0, 1)

img = img.reshape(1, 3, img.shape[1], img.shape[2])

start_time = time.time()
with torch.no_grad():
    if torch.cuda.is_available():
        a = model(torch.from_numpy(img).to(device).type(torch.cuda.FloatTensor) / 255)
    else:
        a = model(torch.from_numpy(img).to(device).type(torch.FloatTensor) / 255)
print("--- %s seconds ---" % (time.time() - start_time))

outImage = a['out'].cpu().detach().numpy()[0]

# Normalize the output image to the range [0, 1]
outImage = (outImage - outImage.min()) / (outImage.max() - outImage.min())

plt.imshow(outImage.transpose(1, 2, 0))
plt.show()
