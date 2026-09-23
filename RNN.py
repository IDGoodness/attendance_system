import matplotlib.pyplot as plt

# Data from the RNN performance table
thresholds = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90, 0.95]
far_values = [22.0, 10.0, 4.0, 0.0, 0.0, 0.0, 0.0]
frr_values = [0.0, 0.0, 2.0, 2.0, 6.0, 14.0, 30.0]
acc_values = [89.0, 95.0, 97.0, 99.0, 97.0, 93.0, 85.0]

plt.figure(figsize=(9, 5.5))

# Plotting Curves
plt.plot(thresholds, far_values, marker='o', color='#d9534f', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(thresholds, frr_values, marker='s', color='#0275d8', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(thresholds, acc_values, marker='^', color='#5cb85c', linewidth=2.0, linestyle='--', label='Anti-Spoofing Accuracy (%)')

# Highlight Optimal Region
plt.axvspan(0.78, 0.82, color='#5cb85c', alpha=0.15, label='Optimal Operational Zone (L_th = 0.80)')

plt.title('FIGURE 4.5: RNN Dynamic Liveness Verification Across Confidence Thresholds', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Temporal Liveness Threshold (L_th)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.xticks(thresholds)
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='center right', frameon=True)

# Save chart image for report
plt.savefig('Figure_RNN_Threshold_Analysis.png', dpi=300, bbox_inches='tight')
plt.show()