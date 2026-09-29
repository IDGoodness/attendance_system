import matplotlib.pyplot as plt

# Normalized progression stages
stages = ['Very Permissive', 'Permissive', 'Balanced', 'Optimal Point', 'Strict', 'Overly Strict']
x = range(len(stages))

# Precision values (%) across threshold runs
prec_cos = [76.9, 89.3, 97.5, 100.0, 100.0, 100.0]
prec_cnn = [80.6, 90.1, 96.2, 100.0, 100.0, 100.0]
prec_svm = [84.7, 92.6, 98.0, 100.0, 100.0, 100.0]
prec_rnn = [82.0, 90.9, 96.1, 100.0, 100.0, 100.0]

plt.figure(figsize=(9, 5.5))

plt.plot(x, prec_svm, marker='s', color='#ff7f0e', linewidth=2.3, label='SVM (RBF Kernel)')
plt.plot(x, prec_cnn, marker='o', color='#2ca02c', linewidth=2.3, label='CNN Softmax')
plt.plot(x, prec_rnn, marker='d', color='#9467bd', linewidth=2.0, label='RNN Temporal')
plt.plot(x, prec_cos, marker='^', color='#1f77b4', linewidth=2.0, label='Cosine Similarity')

# Highlight the 100% precision plateau
plt.axhline(100, color='gray', linestyle=':', linewidth=1.2)
plt.axvline(x=3, color='green', linestyle='--', alpha=0.5, label='Calibrated Point (100% Precision)')

plt.title('Biometric Precision Trajectory Across Operating Strictness', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Operational Decision Strictness', fontsize=11, fontweight='bold')
plt.ylabel('Precision Rate (PPV %)', fontsize=11, fontweight='bold')
plt.xticks(x, stages, fontsize=10)
plt.ylim(70, 105)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(loc='lower right', frameon=True, fontsize=10)
plt.tight_layout()

plt.savefig('Figure_4_Precision_Comparison.png', dpi=300)
plt.show()