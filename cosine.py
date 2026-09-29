import matplotlib.pyplot as plt

# Data from Table 4.1
tau = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
far = [30.0, 12.0, 0.0, 0.0, 0.0, 0.0]
frr = [0.0, 0.0, 2.0, 5.0, 18.0, 36.0]
acc = [85.0, 94.0, 99.0, 97.5, 91.0, 82.0]

plt.figure(figsize=(8, 5.2))
plt.plot(tau, far, marker='o', color='#d62728', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(tau, frr, marker='s', color='#1f77b4', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(tau, acc, marker='^', color='#2ca02c', linestyle='-.', linewidth=2.0, label='Overall Accuracy (%)')

# Highlight Optimal Operational Threshold
plt.axvspan(0.38, 0.42, color='#2ca02c', alpha=0.15, label=r'Optimal Operating Point ($\tau = 0.40$)')

plt.title('Cosine Similarity Biometric Error Trade-off Curve', fontsize=12, fontweight='bold', pad=12)
plt.xlabel(r'Cosine Similarity Threshold ($\tau$)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='center right', frameon=True, fontsize=10)
plt.tight_layout()

plt.savefig('Figure_4_2_Cosine_Operating_Curve.png', dpi=300)
plt.show()