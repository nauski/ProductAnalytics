# Logistic Regression Model Report

## 1. Modeling Approach

### Steps Taken

1. **Target Variable**  
   - Used the `issued` column (TRUE/FALSE) to define the target variable:  
     `purchased = 1` if issued is TRUE, otherwise `0`.

2. **Feature Selection**  
   Included:
   - Customer demographics: `customer_age`, `gender`, `driving_type`
   - Car information: `car_age`
   - Insurance options and coverage prices: `collision`, `theft_fire`, `roadside_assistance`, etc.
   - Subscription status: `base_subscription`, `pay_subscription`, `premium_subscription`

   Excluded:
   - Columns leaking target info (e.g., `price_sale`, `discount_percent`)
   - High-cardinality/sparse columns (e.g., `car_model`, `county`)
   - Raw date fields (after deriving age features)

3. **Preprocessing**  
   - Converted dates to `customer_age` and `car_age`
   - Encoded subscription columns as binary (1 = subscribed)
   - One-hot encoded categorical variables
   - Filled missing values with medians/modes

4. **Model Selection**  
   - Used **Logistic Regression** for interpretability and as a solid baseline classifier
   - Increased `max_iter` to 5000 to handle convergence issues

---

## 2. Model Performance & Limitations

### Metrics

| Metric        | Value   | Interpretation                             |
|---------------|---------|---------------------------------------------|
| Accuracy      | 88.9%   | High overall correctness                    |
| Precision     | 99.9%   | Almost all predicted buyers were real       |
| Recall        | 64.5%   | About 2/3 of real buyers were correctly identified |
| F1 Score      | 78.4%   | Balanced precision and recall               |
| ROC AUC       | 0.87    | Strong class separation capability          |

### Confusion Matrix

[[5519 1] [ 887 1610]]

- **True Negatives** (Did not buy, predicted correctly): 5519
- **False Positives** (Predicted buy, actually didn't): 1
- **False Negatives** (Missed buyers): 887
- **True Positives** (Bought, predicted correctly): 1610

### ⚠️ Weaknesses / Limitations
- **Low Recall**: Model misses ~1/3 of buyers.
- **Solver convergence**: Needed high iterations; scaling may help further.
- **No behavioral enrichment**: Didn’t use `Transactions` data.
- **Model simplicity**: Logistic regression may miss complex nonlinear patterns.

---

## 3. Performance Metrics Considered

| Metric     | Reason for Use                                          |
|------------|----------------------------------------------------------|
| Accuracy   | Basic correctness measure (can be misleading alone)      |
| Precision  | Important to minimize false positives                    |
| Recall     | Important to capture as many real buyers as possible     |
| F1 Score   | Balanced trade-off between precision and recall          |
| ROC AUC    | Robust measure across all probability thresholds          |

