# Spracherkennung 2 – Prompt Engineering for Diabetic Health

This project explores how prompt engineering and fine-tuned language models can be used to assist people with diabetes by providing personalized health advice through a chatbot interface.

## 🔍 Overview

The goal is to build a specialized chatbot capable of generating tailored advice for individuals with Type 1 and Type 2 diabetes. It focuses on:

- Recipe suggestions
- Exercise recommendations
- Basic Q&A about diabetes

The system uses a fine-tuned Large Language Model (LLM) trained on a custom dataset, allowing it to address the challenges of diabetes care: complexity, communication gaps, and cost.

---

## Technologies Used

- **Prompt Engineering**: Customized prompts using temperature and nucleus sampling (top-p) to improve response quality.
- **Alpaca Format**: Training data structured in Alpaca JSON format for instruction tuning.
- **Unsloth**: Efficient fine-tuning of LLMs.
  - GitHub: [unslothai/unsloth](https://github.com/unslothai/unsloth)
- **Ollama**: Local deployment and testing of fine-tuned models.
  - GitHub: [ollama/ollama](https://github.com/ollama/ollama)

---

## ⚙️ Key Steps

1. **Problem Definition**
   - Address diabetes management complexity and healthcare accessibility.
2. **Data Preparation**
   - Built a custom Alpaca-style JSON dataset with realistic diabetes-related prompts.
3. **Model Fine-Tuning**
   - Used Unsloth to train a model on the Alpaca JSON data.
4. **Deployment**
   - Deployed and tested the model locally using Ollama.
5. **Testing**
   - Evaluated model performance with test prompts such as:
     - "What is a healthy lunch for someone with Type 1 diabetes and moderate insulin resistance?"
     - "Can I eat carbohydrates if I have diabetes?"

---

## Included Files

- `diabetes_alpaca.json`: Instruction-based dataset used for fine-tuning.
- `sprache2-presentation.pdf`: PowerPoint exported as PDF, presenting the methodology and results.
- `README.md`: This file.

> ⚠️ The fine-tuning code is **not included** in this repository because it is open source and publicly available from the links above.

---

## Results

- The chatbot successfully returns relevant answers based on specific diabetic profiles.
- Fine-tuning even on a small dataset led to noticeable improvement in response quality.
- Demonstrated how LLMs can assist in low-cost, domain-specific healthcare support.

---

## Conclusion

This project proves that domain-specific prompt engineering and LLM fine-tuning can support better communication and decision-making for diabetes care. 


