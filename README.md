# T6.2

Course: Product Analytics
Assignment: T6.2

# PROBLEM 1

## 1.1. Do commuting hours experience a higher number of ridesharing (Express + POOL) trips compared to non-commuting hours?
Mean commuting rides: 5046.00  
Mean non-commuting rides: 3763.40  
Answer: YES

## 1.2. What is the difference in the number of ridesharing trips between commuting and non-commuting hours?
Difference: 1282.60 trips

## 1.3. Is the difference statistically significant at the 5% confidence level?
t-statistic: 7.7715, p-value: 0.000010  
Statistically significant? YES

## 1.4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?
Mean Express share (commute): 0.6981  
Mean Express share (non-commute): 0.6480  
Answer: YES

## 1.5. What is the difference in the share of Express trips between commuting and non-commuting hours?
Difference: 0.0501 (or 5.01 percentage points)

## 1.6. Is the difference statistically significant at the 5% confidence level?
t-statistic: 3.7599, p-value: 0.001620  
Statistically significant? YES

## 1.7. Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride. What is the difference in revenues between commuting and non-commuting hours?
Mean revenue (commute): $54256.25  
Mean revenue (non-commute): $40945.28  
Difference: $13310.97

## 1.8. Is the difference statistically significant at the 5% confidence level?
t-statistic: 7.6565, p-value: 0.000010  
Statistically significant? YES

## 1.9. What is the difference in profits per trip between commuting and non-commuting hours?
Mean profit per trip (commute): $2.94  
Mean profit per trip (non-commute): $3.60  
Difference: $-0.66

## 1.10. Is the difference statistically significant at the 5% confidence level?
t-statistic: -4.4526, p-value: 0.000346  
Statistically significant? YES

# PROBLEM 2

## 2.1. What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?
Mean rides (treatment): 4724.10  
Mean rides (control): 5046.00  
Difference: -321.90

## 2.2. Is the difference statistically significant at the 5% confidence level?
t-statistic: -1.4197, p-value: 0.172812  
Statistically significant? NO

## 2.3. What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?
Mean cancellations (treatment): 303.20  
Mean cancellations (control): 246.90  
Difference: 56.30

## 2.4. Is the difference statistically significant at the 5% confidence level?
t-statistic: 3.1953, p-value: 0.006799  
Statistically significant? YES

## 2.5. What is the difference in driver payout per trip between the treatment and control groups during commuting hours?
Mean payout per trip (treatment): $7.57  
Mean payout per trip (control): $7.81  
Difference: $-0.24

## 2.6. Is the difference statistically significant at the 5% confidence level?
t-statistic: -1.1067, p-value: 0.283821  
Statistically significant? NO

## 2.7. What is the difference in overall match rate between the treatment and control groups during commuting hours?
Mean matches (treatment): 3474.40  
Mean matches (control): 3789.30  
Difference: -314.90

## 2.8. Is the difference statistically significant at the 5% confidence level?
t-statistic: -1.2147, p-value: 0.240178  
Statistically significant? NO

## 2.9. What is the difference in double match rate between the treatment and control groups during commuting hours?
Mean double matches (treatment): 1807.80  
Mean double matches (control): 1794.30  
Difference: 13.50

## 2.10. Is the difference statistically significant at the 5% confidence level?
t-statistic: 0.0770, p-value: 0.939449  
Statistically significant? NO

## 2.11. Does the analysis support extending waiting times to 5 minutes for commuting hours?
Conclusion: No, the data provides clear evidence against extending waiting times.

## 2.12. What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?
Mean rides (treatment): 3720.83  
Mean rides (control): 3763.40  
Difference: -42.57

## 2.13. Is the difference statistically significant at the 5% confidence level? (Corrected)
t-statistic: -0.5981, p-value: 0.551058  
Statistically significant? NO

## 2.14. What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?
Mean cancellations (treatment): 168.79  
Mean cancellations (control): 149.96  
Difference: 18.83

## 2.15. Is the difference statistically significant at the 5% confidence level?
t-statistic: 4.2183, p-value: 0.000054  
Statistically significant? YES

## 2.16. What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?
Mean payout per trip (treatment): $6.88  
Mean payout per trip (control): $7.28  
Difference: $-0.40

## 2.17. Is the difference statistically significant at the 5% confidence level?
t-statistic: -3.5404, p-value: 0.000599  
Statistically significant? YES

## 2.18. What is the difference in overall match rate between the treatment and control groups during non-commuting hours?
Mean matches (treatment): 2242.81  
Mean matches (control): 2415.08  
Difference: -172.26

## 2.19. Is the difference statistically significant at the 5% confidence level?
t-statistic: -2.8247, p-value: 0.005677  
Statistically significant? YES

## 2.20. What is the difference in double match rate between the treatment and control groups during non-commuting hours?
Mean double matches (treatment): 1272.81  
Mean double matches (control): 1191.47  
Difference: 81.34

## 2.21. Is the difference statistically significant at the 5% confidence level?
t-statistic: 1.6192, p-value: 0.108557  
Statistically significant? NO

## 2.22. Does the analysis support extending waiting times to 5 minutes for non-commuting hours?
Conclusion: No, the data provides clear evidence against extending waiting times.

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
More trips and total_matches. Conclusion commuting hours are busier.

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
More rider cancellations in treatment group(longer wait). Trips and matches stayed the ~same.
Conclusion people commuting don't want to wait longer.




