## 1. Modeling Approach

### Steps Taken

1. **Target Variable**  
   - Used the `purchased` column (1 = purchased, 0 = not purchased)

2. **Features Used**  
   Included:
   - Customer info: `customer_age`, `gender`, `driving_type`
   - Car info: `car_age`
   - Quote attributes: insurance option prices (e.g. `collision`, `windows`, `legal_protection`)
   - Subscription flags: `base_subscription`, `pay_subscription`, `premium_subscription`
   - One-hot encoded categorical variables

3. **Model Details**
   - Model: `DecisionTreeClassifier` with `max_depth=10` for regularization
   - Data split: 70% training / 30% testing with `stratify=y`

## 2. Model Performance & Limitations

### Evaluation Metrics

| Metric        | Value   | Interpretation                             |
|---------------|---------|---------------------------------------------|
| Accuracy      | 89.1%   | Slightly better than Logistic Regression     |
| Precision     | 95.9%   | Very few false positives                    |
| Recall        | 67.9%   | Captures more real buyers than Logistic     |
| F1 Score      | 79.5%   | Good balance between precision and recall   |
| ROC AUC       | 0.8876  | Excellent class separation                  |

### Confusion Matrix

- Correct non-buyers: 5447
- False positives: 73
- Missed buyers: 800
- Correct buyers: 1697

### Limitations
- Still a moderate number of false negatives (missed buyers)
- Heavily reliant on one dominant feature (`guarantees_purchased_RCA`)
- May be prone to overfitting if depth is not controlled

## 3. Performance Metrics Considered

| Metric     | Reason for Use                                          |
|------------|----------------------------------------------------------|
| Accuracy   | Basic correctness measure                                |
| Precision  | Important to avoid wasting efforts on wrong buyers       |
| Recall     | Critical to catch as many real buyers as possible        |
| F1 Score   | Balances precision and recall                            |
| ROC AUC    | Measures overall discriminative ability                  |

## Top 10 Feature Importances

| Feature                                               | Importance |
|-------------------------------------------------------|------------|
| `guarantees_purchased_RCA`                            | 0.8883     |
| `legal_protection`                                    | 0.0188     |
| `theft_fire`                                          | 0.0122     |
| `windows`                                             | 0.0092     |
| `car_age`                                             | 0.0086     |
| `customer_age`                                        | 0.0069     |
| `waive_right_compensation`                            | 0.0069     |
| `guarantees_available_Infortuni del Conducente...`    | 0.0068     |
| `protected_bonus`                                     | 0.0068     |
| `basic_coverage`                                      | 0.0066     |


Decision Tree outperformed Logistic Regression on recall and AUC and provides clear feature importance. It is a strong interpretable model for baseline prediction.

