import matplotlib.pyplot as plt

# Styling configuration
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.1

# Empirical data from Tables 4.1 - 4.4
tau_vals = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
acc_cos = [85.0, 94.0, 99.0, 97.5, 91.0, 82.0]

pth_cnn = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
acc_cnn = [88.0, 94.5, 98.0, 99.5, 98.0, 94.0]

pth_svm = [0.50, 0.60, 0.70, 0.75, 0.80, 0.85]
acc_svm = [91.0, 96.0, 98.5, 99.5, 98.5, 96.5]

lth_rnn = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
acc_rnn = [89.0, 95.0, 97.5, 98.5, 97.0, 93.0]

plt.figure(figsize=(10, 6.2))

# Plot all models on the shared numerical threshold axis
plt.plot(tau_vals, acc_cos, marker='^', color='#1f77b4', linewidth=2.3, markersize=7, 
         label=r'Cosine Similarity ($\tau$: 0.30 – 0.55)')
plt.plot(pth_cnn, acc_cnn, marker='o', color='#2ca02c', linewidth=2.3, markersize=7, 
         label=r'CNN Softmax ($P_{th}$: 0.50 – 0.90)')
plt.plot(pth_svm, acc_svm, marker='s', color='#ff7f0e', linewidth=2.3, markersize=7, 
         label=r'SVM RBF Kernel ($P_{th}$: 0.50 – 0.85)')
plt.plot(lth_rnn, acc_rnn, marker='d', color='#9467bd', linewidth=2.1, markersize=7, 
         label=r'RNN Sequence ($L_{th}$: 0.50 – 0.90)')

# Highlight the optimal operating convergence points
optimal_points = [
    (0.40, 99.0, '#1f77b4', r'$\tau=0.40$ (99.0%)'),
    (0.80, 99.5, '#2ca02c', r'$P_{th}=0.80$ (99.5%)'),
    (0.75, 99.5, '#ff7f0e', r'$P_{th}=0.75$ (99.5%)'),
    (0.80, 98.5, '#9467bd', r'$L_{th}=0.80$ (98.5%)')
]

for x_val, y_val, col, txt in optimal_points:
    plt.scatter(x_val, y_val, color=col, s=90, zorder=5, edgecolor='black', linewidth=0.8)

# Annotate peaks
plt.annotate(r'Cosine Peak: $\tau=0.40$ (99.0%)', xy=(0.40, 99.0), xytext=(0.31, 100.2),
             arrowprops=dict(arrowstyle="->", color='#1f77b4', lw=1.2),
             fontsize=9, fontweight='bold', color='#1f77b4')

plt.annotate(r'SVM Peak: $P_{th}=0.75$ (99.5%)', xy=(0.75, 99.5), xytext=(0.58, 101.0),
             arrowprops=dict(arrowstyle="->", color='#ff7f0e', lw=1.2),
             fontsize=9, fontweight='bold', color='#ff7f0e')

plt.annotate(r'CNN Peak: $P_{th}=0.80$ (99.5%)', xy=(0.80, 99.5), xytext=(0.82, 100.8),
             arrowprops=dict(arrowstyle="->", color='#2ca02c', lw=1.2),
             fontsize=9, fontweight='bold', color='#2ca02c')

plt.annotate(r'RNN Peak: $L_{th}=0.80$ (98.5%)', xy=(0.80, 98.5), xytext=(0.82, 97.2),
             arrowprops=dict(arrowstyle="->", color='#9467bd', lw=1.2),
             fontsize=9, fontweight='bold', color='#9467bd')

# plt.title('Verification Accuracy vs. Operating Decision Thresholds', fontsize=12, fontweight='bold', pad=14)
plt.xlabel('Operating Decision Threshold Value', fontsize=11, fontweight='bold')
plt.ylabel('System Classification Accuracy (%)', fontsize=11, fontweight='bold')
plt.xlim(0.28, 0.95)
plt.ylim(80, 103)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower left', frameon=True, fontsize=9.5)
plt.tight_layout()

plt.savefig('Figure_4_3_Accuracy_Single_Graph.png', dpi=300)
plt.show()