import matplotlib.pyplot as plt

# Data from Table 4.4
lth = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
far = [22.0, 10.0, 4.0, 0.0, 0.0, 0.0]
frr = [0.0, 0.0, 1.0, 3.0, 6.0, 14.0]
acc = [89.0, 95.0, 97.5, 98.5, 97.0, 93.0]

plt.figure(figsize=(8, 5.2))
plt.plot(lth, far, marker='o', color='#d62728', linewidth=2.2, label='False Acceptance Rate (FAR)')
plt.plot(lth, frr, marker='s', color='#1f77b4', linewidth=2.2, label='False Rejection Rate (FRR)')
plt.plot(lth, acc, marker='^', color='#2ca02c', linestyle='-.', linewidth=2.0, label='Anti-Spoofing Accuracy (%)')

# Highlight Optimal Operational Threshold
plt.axvspan(0.78, 0.82, color='#2ca02c', alpha=0.15, label=r'Optimal Operating Point ($L_{th} = 0.80$)')

plt.title('RNN Operating Curve', fontsize=12, fontweight='bold', pad=12)
plt.xlabel(r'Dynamic Liveness Threshold ($L_{th}$)', fontsize=11, fontweight='bold')
plt.ylabel('Rate (%)', fontsize=11, fontweight='bold')
plt.ylim(-2, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='center right', frameon=True, fontsize=10)
plt.tight_layout()

plt.savefig('Figure_4_5_RNN_Operating_Curve.png', dpi=300)
plt.show()