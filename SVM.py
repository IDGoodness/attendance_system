import matplotlib.pyplot as plt

# Data from the SVM performance table
thresholds = [0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 0.90]
far_values = [18.0, 8.0, 2.0, 0.0, 0.0, 0.0, 0.0]
frr_values = [0.0, 0.0, 1.0, 1.0, 3.0, 7.0, 19.0]
acc_values = [91.0, 96.0, 98.5, 99.5, 98.5, 96.5, 90.5]

plt.figure(figsize=(9, 5.5))

# Plot Curves
plt.plot(thresholds, far_values, marker='o', color='#d9534f', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(thresholds, frr_values, marker='s', color='#0275d8', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(thresholds, acc_values, marker='^', color='#5cb85c', linewidth=2.0, linestyle='--', label='Overall Accuracy (%)')

# Highlight Optimal Region
plt.axvspan(0.73, 0.77, color='#5cb85c', alpha=0.15, label='Optimal Operational Zone (P_th = 0.75)')

plt.title('FIGURE 4.4: SVM Classification Performance Across Probability Thresholds', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('SVM Probability Threshold (P_th)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.xticks(thresholds)
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='center right', frameon=True)

# Export high-resolution chart for report
plt.savefig('Figure_SVM_Threshold_Analysis.png', dpi=300, bbox_inches='tight')
plt.show()