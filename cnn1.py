import matplotlib.pyplot as plt

# Data from Table 4.2
pth = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
far = [24.0, 11.0, 4.0, 0.0, 0.0, 0.0]
frr = [0.0, 0.0, 0.0, 1.0, 4.0, 12.0]
acc = [88.0, 94.5, 98.0, 99.5, 98.0, 94.0]

plt.figure(figsize=(8, 5.2))
plt.plot(pth, far, marker='o', color='#d62728', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(pth, frr, marker='s', color='#1f77b4', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(pth, acc, marker='^', color='#2ca02c', linestyle='-.', linewidth=2.0, label='Overall Accuracy (%)')

# Highlight Optimal Operational Threshold
plt.axvspan(0.78, 0.82, color='#2ca02c', alpha=0.15, label=r'Optimal Operating Point ($P_{th} = 0.80$)')

plt.title('CNN Softmax Confidence Classification Error Curve', fontsize=12, fontweight='bold', pad=12)
plt.xlabel(r'Softmax Probability Threshold ($P_{th}$)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='center right', frameon=True, fontsize=10)
plt.tight_layout()

plt.savefig('Figure_4_3_CNN_Operating_Curve.png', dpi=300)
plt.show()