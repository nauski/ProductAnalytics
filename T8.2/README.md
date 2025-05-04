# Telepass Insurance Purchase Prediction – Model Comparison

This repository contains an analysis of three machine learning models — **Logistic Regression**, **Decision Tree**, and **Random Forest** — to predict whether a customer will purchase an insurance policy based on quote data provided by Telepass.

Each model has its own subfolder with:
- Preprocessing script (`cleanup.py`)
- Model training script (`train*.py`)
- Input data (`Telepass.xlsx`)
- Model-specific README containing performance metrics and interpretation

### To reproduce results run:

```
python cleanup.py Telepass.xlsx
python train*.py cleaned_telepass_insurance.csv
```

## Models Compared

| Model               | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|--------------------|----------|-----------|--------|----------|---------|
| Logistic Regression| 88.92%   | 99.94%    | 64.48% | 77.76%   | 0.8689  |
| Decision Tree       | 89.11%   | 95.88%    | 67.96% | 79.54%   | 0.8876  |
| Random Forest       | 88.85%   | 100.00%   | 64.20% | 78.20%   | 0.8910  |

---

## Best Performing Model

### **Random Forest performed the best overall.**

While all models achieved similar accuracy (~89%), **Random Forest** had the **highest ROC AUC (0.8910)** — meaning it was best at distinguishing between buyers and non-buyers across all thresholds. It also had **perfect precision (100%)**, meaning all predicted buyers were indeed buyers, although recall (64.2%) was still moderate.

Random Forest also provided feature importance insights, making it both powerful and interpretable.

## Metrics explained

| Metric         | Meaning                                             | Good For                      |
|----------------|-----------------------------------------------------|-------------------------------|
| Accuracy       | % of correct predictions                           | Balanced datasets             |
| Precision      | % of predicted buyers who actually bought           | Avoiding false positives      |
| Recall         | % of actual buyers correctly identified             | Avoiding false negatives      |
| F1 Score       | Balance between precision and recall                | Overall quality               |
| ROC AUC        | How well the model separates the classes            | Robustness across thresholds  |
| Confusion Matrix | Breakdown of correct/incorrect predictions        | Diagnostic clarity            |
| Feature Importance | Which inputs influenced predictions the most   | Model interpretability        |

