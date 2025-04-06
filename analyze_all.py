import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from scipy.stats import ttest_ind

print("# Course: Product Analytics")
print("# Assignment: T6.2")
print("# Analyzing how Uber driver payouts are affected by wait time and commuting hours\n")

excel_path = "./dataset.xlsx"
df = pd.read_excel(excel_path, sheet_name='Switchbacks')

print("# 1.1. Do commuting hours experience a higher number of ridesharing (Express + POOL) trips compared to non-commuting hours?")

control = df[df['treat'] == False]
commute = control[control['commute'] == True]
non_commute = control[control['commute'] == False]

commute_rides = commute['trips_pool'] + commute['trips_express']
non_commute_rides = non_commute['trips_pool'] + non_commute['trips_express']
mean_commute_rides = commute_rides.mean()
mean_non_commute_rides = non_commute_rides.mean()

if mean_commute_rides > mean_non_commute_rides:
    result = "YES"
else:
    result = "NO"

print(f"Mean commuting rides: {mean_commute_rides:.2f}")
print(f"Mean non-commuting rides: {mean_non_commute_rides:.2f}")
print(f"Answer: {result}\n")

print("# 1.2. What is the difference in the number of ridesharing trips between commuting and non-commuting hours?")
ride_diff = mean_commute_rides - mean_non_commute_rides
print(f"Difference: {ride_diff:.2f} trips\n")

print("# 1.3. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(commute_rides, non_commute_rides, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 1.4. Do riders use Express at higher rates during commuting hours compared to non-commuting hours?")

commute_express_share = commute['trips_express'] / (commute['trips_pool'] + commute['trips_express'])
non_commute_express_share = non_commute['trips_express'] / (non_commute['trips_pool'] + non_commute['trips_express'])
mean_commute_share = commute_express_share.mean()
mean_non_commute_share = non_commute_express_share.mean()

result = "YES" if mean_commute_share > mean_non_commute_share else "NO"

print(f"Mean Express share (commute): {mean_commute_share:.4f}")
print(f"Mean Express share (non-commute): {mean_non_commute_share:.4f}")
print(f"Answer: {result}\n")

print("# 1.5. What is the difference in the share of Express trips between commuting and non-commuting hours?")
share_diff = mean_commute_share - mean_non_commute_share
print(f"Difference: {share_diff:.4f} (or {share_diff*100:.2f} percentage points)\n")

print("# 1.6. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(commute_express_share, non_commute_express_share, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 1.7. Assume that riders pay $12.5 on average for a POOL ride, and $10 for an Express ride.")
print("# What is the difference in revenues between commuting and non-commuting hours?")

commute_revenue = commute['trips_pool'] * 12.5 + commute['trips_express'] * 10
non_commute_revenue = non_commute['trips_pool'] * 12.5 + non_commute['trips_express'] * 10
mean_commute_revenue = commute_revenue.mean()
mean_non_commute_revenue = non_commute_revenue.mean()

revenue_diff = mean_commute_revenue - mean_non_commute_revenue
print(f"Mean revenue (commute): ${mean_commute_revenue:.2f}")
print(f"Mean revenue (non-commute): ${mean_non_commute_revenue:.2f}")
print(f"Difference: ${revenue_diff:.2f}\n")

print("# 1.8. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(commute_revenue, non_commute_revenue, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 1.9. What is the difference in profits per trip between commuting and non-commuting hours?")

commute_total_trips = commute['trips_pool'] + commute['trips_express']
non_commute_total_trips = non_commute['trips_pool'] + non_commute['trips_express']
commute_profit_per_trip = (commute_revenue - commute['total_driver_payout']) / commute_total_trips
non_commute_profit_per_trip = (non_commute_revenue - non_commute['total_driver_payout']) / non_commute_total_trips
mean_commute_profit = commute_profit_per_trip.mean()
mean_non_commute_profit = non_commute_profit_per_trip.mean()
profit_diff = mean_commute_profit - mean_non_commute_profit

print(f"Mean profit per trip (commute): ${mean_commute_profit:.2f}")
print(f"Mean profit per trip (non-commute): ${mean_non_commute_profit:.2f}")
print(f"Difference: ${profit_diff:.2f}\n")

print("# 1.10. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(commute_profit_per_trip, non_commute_profit_per_trip, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# PROBLEM 2: Estimating the Effect of Extending Wait Times (Commuting Hours Only)")

commute = df[df['commute'] == True]
commute_treat = commute[commute['treat'] == True]
commute_control = commute[commute['treat'] == False]

print("# 2.1. What is the difference in the number of ridesharing trips between the treatment and control groups during commuting hours?")
treat_rides = commute_treat['trips_pool'] + commute_treat['trips_express']
control_rides = commute_control['trips_pool'] + commute_control['trips_express']
mean_treat_rides = treat_rides.mean()
mean_control_rides = control_rides.mean()
ride_diff = mean_treat_rides - mean_control_rides

print(f"Mean rides (treatment): {mean_treat_rides:.2f}")
print(f"Mean rides (control): {mean_control_rides:.2f}")
print(f"Difference: {ride_diff:.2f}\n")

print("# 2.2. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_rides, control_rides, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.3. What is the difference in the number of rider cancellations between the treatment and control groups during commuting hours?")
treat_cancels = commute_treat['rider_cancellations']
control_cancels = commute_control['rider_cancellations']
mean_treat_cancels = treat_cancels.mean()
mean_control_cancels = control_cancels.mean()
cancel_diff = mean_treat_cancels - mean_control_cancels

print(f"Mean cancellations (treatment): {mean_treat_cancels:.2f}")
print(f"Mean cancellations (control): {mean_control_cancels:.2f}")
print(f"Difference: {cancel_diff:.2f}\n")

print("# 2.4. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_cancels, control_cancels, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.5. What is the difference in driver payout per trip between the treatment and control groups during commuting hours?")

treat_total_payout = commute_treat['total_driver_payout']
control_total_payout = commute_control['total_driver_payout']
treat_total_trips = commute_treat['trips_pool'] + commute_treat['trips_express']
control_total_trips = commute_control['trips_pool'] + commute_control['trips_express']

treat_payout_per_trip = treat_total_payout / treat_total_trips
control_payout_per_trip = control_total_payout / control_total_trips

mean_treat_payout = treat_payout_per_trip.mean()
mean_control_payout = control_payout_per_trip.mean()
payout_diff = mean_treat_payout - mean_control_payout

print(f"Mean payout per trip (treatment): ${mean_treat_payout:.2f}")
print(f"Mean payout per trip (control): ${mean_control_payout:.2f}")
print(f"Difference: ${payout_diff:.2f}\n")

print("# 2.6. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_payout_per_trip, control_payout_per_trip, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.7. What is the difference in overall match rate between the treatment and control groups during commuting hours?")

treat_matches = commute_treat['total_matches']
control_matches = commute_control['total_matches']
mean_treat_matches = treat_matches.mean()
mean_control_matches = control_matches.mean()
match_diff = mean_treat_matches - mean_control_matches

print(f"Mean matches (treatment): {mean_treat_matches:.2f}")
print(f"Mean matches (control): {mean_control_matches:.2f}")
print(f"Difference: {match_diff:.2f}\n")

print("# 2.8. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_matches, control_matches, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.9. What is the difference in double match rate between the treatment and control groups during commuting hours?")

treat_double_matches = commute_treat['total_double_matches']
control_double_matches = commute_control['total_double_matches']
mean_treat_double = treat_double_matches.mean()
mean_control_double = control_double_matches.mean()
double_diff = mean_treat_double - mean_control_double

print(f"Mean double matches (treatment): {mean_treat_double:.2f}")
print(f"Mean double matches (control): {mean_control_double:.2f}")
print(f"Difference: {double_diff:.2f}\n")

print("# 2.10. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_double_matches, control_double_matches, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.11. Does the analysis support extending waiting times to 5 minutes for commuting hours?")

if p_val < 0.05 and payout_diff > 0 and match_diff > 0 and cancel_diff < 0:
    conclusion = "Yes, the data provides clear support for extending waiting times."
elif p_val > 0.05 and (abs(payout_diff) < 0.5 and abs(match_diff) < 50):
    conclusion = "No, the data provides mixed evidence for extending waiting times."
else:
    conclusion = "No, the data provides clear evidence against extending waiting times."

print(f"Conclusion: {conclusion}\n")

non_commute = df[df['commute'] == False]
non_commute_treat = non_commute[non_commute['treat'] == True]
non_commute_control = non_commute[non_commute['treat'] == False]

print("# 2.12. What is the difference in the number of ridesharing trips between the treatment and control groups during non-commuting hours?")
treat_rides = non_commute_treat['trips_pool'] + non_commute_treat['trips_express']
control_rides = non_commute_control['trips_pool'] + non_commute_control['trips_express']
mean_treat_rides = treat_rides.mean()
mean_control_rides = control_rides.mean()
ride_diff = mean_treat_rides - mean_control_rides

print(f"Mean rides (treatment): {mean_treat_rides:.2f}")
print(f"Mean rides (control): {mean_control_rides:.2f}")
print(f"Difference: {ride_diff:.2f}\n")

print("# 2.13. Is the difference statistically significant at the 5% confidence level?")

ride_tstat, ride_pval = ttest_ind(treat_rides, control_rides, equal_var=False)
sig_result = "YES" if ride_pval < 0.05 else "NO"

print(f"# t-statistic: {ride_tstat:.4f}, p-value: {ride_pval:.6f}")
print(f"# Statistically significant? {sig_result}\n")


print("# 2.14. What is the difference in the number of rider cancellations between the treatment and control groups during non-commuting hours?")
treat_cancels = non_commute_treat['rider_cancellations']
control_cancels = non_commute_control['rider_cancellations']
mean_treat_cancels = treat_cancels.mean()
mean_control_cancels = control_cancels.mean()
cancel_diff = mean_treat_cancels - mean_control_cancels

print(f"Mean cancellations (treatment): {mean_treat_cancels:.2f}")
print(f"Mean cancellations (control): {mean_control_cancels:.2f}")
print(f"Difference: {cancel_diff:.2f}\n")

print("# 2.15. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_cancels, control_cancels, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.16. What is the difference in driver payout per trip between the treatment and control groups during non-commuting hours?")

treat_total_payout = non_commute_treat['total_driver_payout']
control_total_payout = non_commute_control['total_driver_payout']
treat_total_trips = non_commute_treat['trips_pool'] + non_commute_treat['trips_express']
control_total_trips = non_commute_control['trips_pool'] + non_commute_control['trips_express']

treat_payout_per_trip = treat_total_payout / treat_total_trips
control_payout_per_trip = control_total_payout / control_total_trips

mean_treat_payout = treat_payout_per_trip.mean()
mean_control_payout = control_payout_per_trip.mean()
payout_diff = mean_treat_payout - mean_control_payout

print(f"Mean payout per trip (treatment): ${mean_treat_payout:.2f}")
print(f"Mean payout per trip (control): ${mean_control_payout:.2f}")
print(f"Difference: ${payout_diff:.2f}\n")

print("# 2.17. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_payout_per_trip, control_payout_per_trip, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.18. What is the difference in overall match rate between the treatment and control groups during non-commuting hours?")

treat_matches = non_commute_treat['total_matches']
control_matches = non_commute_control['total_matches']
mean_treat_matches = treat_matches.mean()
mean_control_matches = control_matches.mean()
match_diff = mean_treat_matches - mean_control_matches

print(f"Mean matches (treatment): {mean_treat_matches:.2f}")
print(f"Mean matches (control): {mean_control_matches:.2f}")
print(f"Difference: {match_diff:.2f}\n")

print("# 2.19. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_matches, control_matches, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.20. What is the difference in double match rate between the treatment and control groups during non-commuting hours?")

treat_double_matches = non_commute_treat['total_double_matches']
control_double_matches = non_commute_control['total_double_matches']
mean_treat_double = treat_double_matches.mean()
mean_control_double = control_double_matches.mean()
double_diff = mean_treat_double - mean_control_double

print(f"Mean double matches (treatment): {mean_treat_double:.2f}")
print(f"Mean double matches (control): {mean_control_double:.2f}")
print(f"Difference: {double_diff:.2f}\n")

print("# 2.21. Is the difference statistically significant at the 5% confidence level?")
t_stat, p_val = ttest_ind(treat_double_matches, control_double_matches, equal_var=False)
sig_result = "YES" if p_val < 0.05 else "NO"
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.6f}")
print(f"Statistically significant? {sig_result}\n")

print("# 2.22. Does the analysis support extending waiting times to 5 minutes for non-commuting hours?")

if (
    match_diff < 0 and
    cancel_diff > 0 and
    payout_diff < 0 and
    p_val > 0.05
):
    conclusion = "No, the data provides clear evidence against extending waiting times."
elif abs(match_diff) < 50 and abs(payout_diff) < 0.5 and p_val > 0.05:
    conclusion = "No, the data provides mixed evidence for extending waiting times."
else:
    conclusion = "Yes, the data provides clear support for extending waiting times."

print(f"Conclusion: {conclusion}\n")







