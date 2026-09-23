import matplotlib.pyplot as plt

# Data from the CNN threshold table
thresholds = [0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.80]
far_values = [0.0, 0.0, 0.0, 0.0, 3.0, 10.0, 28.0]
frr_values = [32.0, 12.0, 4.0, 1.0, 0.0, 0.0, 0.0]
accuracy_values = [84.0, 94.0, 98.0, 99.5, 98.5, 95.0, 86.0]

plt.figure(figsize=(9, 5.5))

# Plotting FAR, FRR, and Accuracy
plt.plot(thresholds, far_values, marker='o', color='#d9534f', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(thresholds, frr_values, marker='s', color='#0275d8', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(thresholds, accuracy_values, marker='^', color='#5cb85c', linewidth=2.0, linestyle='--', label='Overall Accuracy (%)')

# Highlight the optimal threshold region
plt.axvspan(0.58, 0.62, color='#5cb85c', alpha=0.15, label='Optimal Operational Zone (d = 0.60)')


plt.title('FIGURE 4.3: CNN Threshold Evaluation (FAR vs. FRR)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Threshold (d)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.xticks(thresholds)
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='center right', frameon=True)

# Save high-res image
plt.savefig('Figure_CNN_Threshold_Analysis.png', dpi=300, bbox_inches='tight')
plt.show()