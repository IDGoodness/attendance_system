import matplotlib.pyplot as plt

stages = ['Very Permissive', 'Permissive', 'Balanced', 'Optimal Point', 'Strict', 'Overly Strict']
x = range(len(stages))

# False Acceptance Rates (%)
far_cos = [30.0, 12.0, 0.0, 0.0, 0.0, 0.0]
far_cnn = [24.0, 11.0, 4.0, 0.0, 0.0, 0.0]
far_svm = [18.0, 8.0, 2.0, 0.0, 0.0, 0.0]
far_rnn = [22.0, 10.0, 4.0, 0.0, 0.0, 0.0]

# True Acceptance Rates (%) [100 - FRR]
tar_cos = [100.0, 100.0, 95.0, 98.0, 82.0, 64.0]
tar_cnn = [100.0, 100.0, 100.0, 99.0, 96.0, 88.0]
tar_svm = [100.0, 100.0, 99.0, 99.0, 97.0, 81.0]
tar_rnn = [100.0, 100.0, 99.0, 97.0, 94.0, 86.0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

# Subplot 1: Security Risk (False Acceptance Rate)
ax1.plot(x, far_cos, marker='^', color='#1f77b4', linewidth=2.0, label='Cosine Similarity')
ax1.plot(x, far_cnn, marker='o', color='#2ca02c', linewidth=2.2, label='CNN Softmax')
ax1.plot(x, far_svm, marker='s', color='#ff7f0e', linewidth=2.2, label='SVM (RBF)')
ax1.plot(x, far_rnn, marker='d', color='#9467bd', linewidth=2.0, label='RNN Temporal')
ax1.axvline(x=3, color='gray', linestyle=':', label='Optimal Operating Boundary')
ax1.set_title('A: Security Vulnerability (False Acceptance Rate)', fontsize=11, fontweight='bold')
ax1.set_xlabel('Operational Strictness', fontsize=10, fontweight='bold')
ax1.set_ylabel('False Acceptance Rate (FAR %)', fontsize=10, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(stages, rotation=25, fontsize=9)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.legend(fontsize=9)

# Subplot 2: User Usability (True Acceptance Rate)
ax2.plot(x, tar_cnn, marker='o', color='#2ca02c', linewidth=2.2, label='CNN Softmax')
ax2.plot(x, tar_svm, marker='s', color='#ff7f0e', linewidth=2.2, label='SVM (RBF)')
ax2.plot(x, tar_cos, marker='^', color='#1f77b4', linewidth=2.0, label='Cosine Similarity')
ax2.plot(x, tar_rnn, marker='d', color='#9467bd', linewidth=2.0, label='RNN Temporal')
ax2.axvline(x=3, color='gray', linestyle=':', label='Optimal Operating Boundary')
ax2.set_title('B: Verification Usability (True Acceptance Rate)', fontsize=11, fontweight='bold')
ax2.set_xlabel('Operational Strictness', fontsize=10, fontweight='bold')
ax2.set_ylabel('True Acceptance Rate (TAR %)', fontsize=10, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(stages, rotation=25, fontsize=9)
ax2.set_ylim(60, 103)
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.legend(fontsize=9, loc='lower left')

plt.suptitle('Comparative Biometric Acceptance Analysis Across Candidate Models', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('Figure_4_Acceptance_Comparison.png', dpi=300)
plt.show()