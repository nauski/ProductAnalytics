# Course: Product Analytics
# Assignment: T6.2
# Analyzing how Uber driver payouts are affected by wait time and commuting hours

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from scipy.stats import ttest_ind

excel_path = "./dataset.xlsx"
df = pd.read_excel(excel_path, sheet_name='Switchbacks')

# Task 1: Control group, compare commute vs non-commute
control_group = df[df['treat'] == False]
commuting = control_group[control_group['commute'] == True]
non_commuting = control_group[control_group['commute'] == False]

commuting_payouts = commuting['total_driver_payout']
non_commuting_payouts = non_commuting['total_driver_payout']

t_stat_1, p_value_1 = ttest_ind(commuting_payouts, non_commuting_payouts, equal_var=False)
mean_commuting = commuting_payouts.mean()
mean_non_commuting = non_commuting_payouts.mean()

print("Task 1: Commute vs Non-Commute (Control Group)")
print(f"Mean (Commute): ${mean_commuting:,.2f}")
print(f"Mean (Non-Commute): ${mean_non_commuting:,.2f}")
print(f"t-statistic: {t_stat_1:.4f}, p-value: {p_value_1:.4f}")
print("Interpretation:", "Significant difference" if p_value_1 < 0.05 else "No significant difference")

# Task 2: Commute hours only, compare treat vs control
commute_only = df[df['commute'] == True]
treatment_commute = commute_only[commute_only['treat'] == True]
control_commute = commute_only[commute_only['treat'] == False]

payout_treatment = treatment_commute['total_driver_payout']
payout_control = control_commute['total_driver_payout']

t_stat_2, p_value_2 = ttest_ind(payout_treatment, payout_control, equal_var=False)
mean_treatment = payout_treatment.mean()
mean_control = payout_control.mean()

print("\nTask 2: Treatment vs Control (Commute Only)")
print(f"Mean (Treatment - 5 min wait): ${mean_treatment:,.2f}")
print(f"Mean (Control - 2 min wait): ${mean_control:,.2f}")
print(f"t-statistic: {t_stat_2:.4f}, p-value: {p_value_2:.4f}")
print("Interpretation:", "Significant difference" if p_value_2 < 0.05 else "No significant difference")

# First Graphs
plt.figure(figsize=(8, 5))
plt.bar(['Commute = TRUE', 'Commute = FALSE'], [mean_commuting, mean_non_commuting], color=['skyblue', 'orange'])
plt.title('Task 1: Mean Driver Payouts (Control Group Only)')
plt.ylabel('Mean Total Driver Payout ($)')
plt.tight_layout()
plt.savefig("task1_payouts.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(['Treatment (5 min)', 'Control (2 min)'], [mean_treatment, mean_control], color=['salmon', 'lightgreen'])
plt.title('Task 2: Mean Driver Payouts (Commute Hours Only)')
plt.ylabel('Mean Total Driver Payout ($)')
plt.tight_layout()
plt.savefig("task2_payouts.png")
plt.show()


# Seeing if any other variable has statistically significant diffenrece
outcome_vars = [
    'trips_pool',
    'trips_express',
    'rider_cancellations',
    'total_matches',
    'total_double_matches'
]

# Containers for results
task1_results = []
task2_results = []

# Task 1: Control group only, commute vs non-commute
control_group = df[df['treat'] == False]
commuting = control_group[control_group['commute'] == True]
non_commuting = control_group[control_group['commute'] == False]

for var in outcome_vars:
    t_stat, p_val = ttest_ind(commuting[var], non_commuting[var], equal_var=False)
    mean_commute = commuting[var].mean()
    mean_non_commute = non_commuting[var].mean()
    task1_results.append((var, mean_commute, mean_non_commute, t_stat, p_val))

# Task 2: Commute hours only, treatment vs control
commute_only = df[df['commute'] == True]
treatment_commute = commute_only[commute_only['treat'] == True]
control_commute = commute_only[commute_only['treat'] == False]

for var in outcome_vars:
    t_stat, p_val = ttest_ind(treatment_commute[var], control_commute[var], equal_var=False)
    mean_treat = treatment_commute[var].mean()
    mean_control = control_commute[var].mean()
    task2_results.append((var, mean_treat, mean_control, t_stat, p_val))

task1_df = pd.DataFrame(task1_results, columns=["Variable", "Mean (Commute)", "Mean (Non-Commute)", "t-stat", "p-value"])
task2_df = pd.DataFrame(task2_results, columns=["Variable", "Mean (Treatment)", "Mean (Control)", "t-stat", "p-value"])

print("\nTask 1: Commute vs Non-Commute (Control Group)")
print(tabulate(task1_df, headers='keys', tablefmt='pretty'))

print("\nTask 2: Treatment vs Control (Commute Only)")
print(tabulate(task2_df, headers='keys', tablefmt='pretty'))
