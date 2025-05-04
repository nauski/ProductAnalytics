# Random Forest Model Report

### Steps Taken

1. **Target Variable**  
   - Used the `purchased` column (1 = purchased, 0 = not purchased)

2. **Features Used**  
   Included:
   - Customer attributes: `customer_age`, `gender`, `driving_type`
   - Car details: `car_age`
   - Quote options and protection prices: `collision`, `theft_fire`, etc.
   - Subscription indicators: `base_subscription`, `pay_subscription`, `premium_subscription`
   - One-hot encoded variables

3. **Model Details**
   - Model: `RandomForestClassifier` with `n_estimators=100`, `max_depth=15`
   - Data split: 70% training / 30% testing
   - Used `n_jobs=-1` to train using all CPU cores

## 2. Model Performance & Limitations

### Evaluation Metrics

| Metric        | Value   | Interpretation                             |
|---------------|---------|---------------------------------------------|
| Accuracy      | 88.85%  | Very good general performance               |
| Precision     | 100.00% | No false positives                          |
| Recall        | 64.20%  | Missed ~1/3 of actual buyers                |
| F1 Score      | 78.20%  | Balanced measure between precision and recall |
| ROC AUC       | 0.8910  | Best AUC among tested models                |

### Confusion Matrix

- Correct non-buyers: 5520
- False positives: 0
- Missed buyers: 894
- Correct buyers: 1603

### Limitations
- Still moderate false negative rate (missed buyers)
- Heavily influenced by `guarantees_purchased_*` columns, which may leak post-purchase info
- May require careful feature auditing or threshold tuning for business use

## 3. Performance Metrics Considered

| Metric     | Reason for Use                                          |
|------------|----------------------------------------------------------|
| Accuracy   | High-level overview of correctness                       |
| Precision  | Prevents wasted effort by minimizing false positives     |
| Recall     | Important to catch real buyers and maximize conversion   |
| F1 Score   | Useful when balancing precision and recall               |
| ROC AUC    | Best overall indicator of model discriminative power     |

## Top 10 Feature Importances

| Feature                                               | Importance |
|--------------------------------------------------------|------------|
| `guarantees_purchased_RCA`                             | 0.4096     |
| `guarantees_purchased_Assistenza Stradale - RCA`       | 0.0397     |
| `guarantees_purchased_Infortuni del Conducente...`     | 0.0310     |
| `guarantees_purchased_Furto e Incendio - RCA`          | 0.0307     |
| `guarantees_purchased_Infortuni del Conducente - RCA`  | 0.0283     |
| `legal_protection`                                     | 0.0271     |
| `guarantees_purchased_Cristalli...`                    | 0.0222     |
| `waive_right_compensation`                             | 0.0207     |
| `protected_bonus`                                      | 0.0189     |
| `driver_injury`                                        | 0.0171     |


Random Forest delivered the best class separation (AUC = 0.89) and perfect precision, but recall and reliance on potentially post-purchase fields must be considered for deployment.

