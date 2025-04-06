# T6.2

## Analyzing Uber driver payouts

```
Task 1: Commute vs Non-Commute (Control Group)
Mean (Commute): $39,524.42
Mean (Non-Commute): $27,360.45
t-statistic: 6.9313, p-value: 0.0000
Interpretation: Significant difference
```
![Graph showing Significant difference](https://raw.githubusercontent.com/nauski/ProductAnalytics/refs/heads/main/task1_payouts.png)

```
Task 2: Treatment vs Control (Commute Only)
Mean (Treatment - 5 min wait): $35,744.23
Mean (Control - 2 min wait): $39,524.42
t-statistic: -1.6806, p-value: 0.1105
Interpretation: No significant difference
```

![Graph showing No Significant difference](https://raw.githubusercontent.com/nauski/ProductAnalytics/refs/heads/main/task2_payouts.png)

## Testing to see whether any other variable changes statistically significantly

### Task 1: Commute vs Non-Commute (Control Group)
```
+---+----------------------+----------------+--------------------+-------------------+------------------------+
|   |       Variable       | Mean (Commute) | Mean (Non-Commute) |      t-stat       |        p-value         |
+---+----------------------+----------------+--------------------+-------------------+------------------------+
| 0 |      trips_pool      |     1518.5     | 1324.5283018867924 | 2.743149710864189 |  0.015982000439602725  |
| 1 |    trips_express     |     3527.5     | 2438.867924528302  | 7.416842820309388 | 1.607460595467799e-05  |
| 2 | rider_cancellations  |     246.9      | 149.96226415094338 | 6.032944463799229 | 0.00013209576668264536 |
| 3 |    total_matches     |     3789.3     | 2415.0754716981132 | 7.228799565826024 | 2.7439838395148742e-05 |
| 4 | total_double_matches |     1794.3     | 1191.4716981132076 | 4.597151121012482 | 0.0008045099321990458  |
+---+----------------------+----------------+--------------------+-------------------+------------------------+
```

### Task 2: Treatment vs Control (Commute Only)
```
+---+----------------------+------------------+----------------+---------------------+----------------------+
|   |       Variable       | Mean (Treatment) | Mean (Control) |       t-stat        |       p-value        |
+---+----------------------+------------------+----------------+---------------------+----------------------+
| 0 |      trips_pool      |      1539.9      |     1518.5     | 0.18391720920086102 |  0.8564729545783536  |
| 1 |    trips_express     |      3184.2      |     3527.5     | -1.6152556724117042 |  0.1239091785365518  |
| 2 | rider_cancellations  |      303.2       |     246.9      |  3.195306793550851  | 0.006799014075396651 |
| 3 |    total_matches     |      3474.4      |     3789.3     | -1.2147066782066438 |  0.2401776887814861  |
| 4 | total_double_matches |      1807.8      |     1794.3     | 0.07703145762818356 |  0.9394486814363104  |
+---+----------------------+------------------+----------------+---------------------+----------------------+
```




