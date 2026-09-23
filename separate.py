import matplotlib.pyplot as plt
import numpy as np

# Set standard publication font and styling
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.1

# ==========================================
# GRAPH 1: Individual Model Error Trade-off Curves (4-Subplot Layout)
# ==========================================
fig, axs = plt.subplots(2, 2, figsize=(13, 10))

# 1. Cosine Similarity
tau = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
far_cos = [30.0, 12.0, 0.0, 0.0, 0.0, 0.0]
frr_cos = [0.0, 0.0, 2.0, 5.0, 18.0, 36.0]
acc_cos = [85.0, 94.0, 99.0, 97.5, 91.0, 82.0]

axs[0, 0].plot(tau, far_cos, 'r-o', linewidth=2.2, label='FAR (%)')
axs[0, 0].plot(tau, frr_cos, 'b--s', linewidth=2.2, label='FRR (%)')
axs[0, 0].plot(tau, acc_cos, 'g-.^', linewidth=2.0, label='Accuracy (%)')
axs[0, 0].axvspan(0.38, 0.42, color='green', alpha=0.15, label='Optimal Boundary (0.40)')
axs[0, 0].set_title('A: Cosine Similarity Operating Curve', fontweight='bold', fontsize=11)
axs[0, 0].set_xlabel(r'Angular Threshold ($\tau$)', fontweight='bold')
axs[0, 0].set_ylabel('Rate (%)', fontweight='bold')
axs[0, 0].grid(True, linestyle=':', alpha=0.6)
axs[0, 0].legend(fontsize=9, loc='center right')

# 2. CNN Softmax
pth_cnn = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
far_cnn = [24.0, 11.0, 4.0, 0.0, 0.0, 0.0]
frr_cnn = [0.0, 0.0, 0.0, 1.0, 4.0, 12.0]
acc_cnn = [88.0, 94.5, 98.0, 99.5, 98.0, 94.0]

axs[0, 1].plot(pth_cnn, far_cnn, 'r-o', linewidth=2.2, label='FAR (%)')
axs[0, 1].plot(pth_cnn, frr_cnn, 'b--s', linewidth=2.2, label='FRR (%)')
axs[0, 1].plot(pth_cnn, acc_cnn, 'g-.^', linewidth=2.0, label='Accuracy (%)')
axs[0, 1].axvspan(0.78, 0.82, color='green', alpha=0.15, label='Optimal Boundary (0.80)')
axs[0, 1].set_title('B: CNN Softmax Classification Curve', fontweight='bold', fontsize=11)
axs[0, 1].set_xlabel(r'Confidence Threshold ($P_{th}$)', fontweight='bold')
axs[0, 1].set_ylabel('Rate (%)', fontweight='bold')
axs[0, 1].grid(True, linestyle=':', alpha=0.6)
axs[0, 1].legend(fontsize=9, loc='center right')

# 3. SVM (RBF Kernel)
pth_svm = [0.50, 0.60, 0.70, 0.75, 0.80, 0.85]
far_svm = [18.0, 8.0, 2.0, 0.0, 0.0, 0.0]
frr_svm = [0.0, 0.0, 1.0, 1.0, 3.0, 7.0]
acc_svm = [91.0, 96.0, 98.5, 99.5, 98.5, 96.5]

axs[1, 0].plot(pth_svm, far_svm, 'r-o', linewidth=2.2, label='FAR (%)')
axs[1, 0].plot(pth_svm, frr_svm, 'b--s', linewidth=2.2, label='FRR (%)')
axs[1, 0].plot(pth_svm, acc_svm, 'g-.^', linewidth=2.0, label='Accuracy (%)')
axs[1, 0].axvspan(0.73, 0.77, color='green', alpha=0.15, label='Optimal Boundary (0.75)')
axs[1, 0].set_title('C: SVM Hyperplane Separation Curve', fontweight='bold', fontsize=11)
axs[1, 0].set_xlabel(r'Decision Threshold ($P_{th}$)', fontweight='bold')
axs[1, 0].set_ylabel('Rate (%)', fontweight='bold')
axs[1, 0].grid(True, linestyle=':', alpha=0.6)
axs[1, 0].legend(fontsize=9, loc='center right')

# 4. RNN Dynamic Liveness
lth_rnn = [0.50, 0.60, 0.70, 0.80, 0.85, 0.90]
far_rnn = [22.0, 10.0, 4.0, 0.0, 0.0, 0.0]
frr_rnn = [0.0, 0.0, 1.0, 3.0, 6.0, 14.0]
acc_rnn = [89.0, 95.0, 97.5, 98.5, 97.0, 93.0]

axs[1, 1].plot(lth_rnn, far_rnn, 'r-o', linewidth=2.2, label='FAR (%)')
axs[1, 1].plot(lth_rnn, frr_rnn, 'b--s', linewidth=2.2, label='FRR (%)')
axs[1, 1].plot(lth_rnn, acc_rnn, 'g-.^', linewidth=2.0, label='Accuracy (%)')
axs[1, 1].axvspan(0.78, 0.82, color='green', alpha=0.15, label='Optimal Boundary (0.80)')
axs[1, 1].set_title('D: RNN Temporal Sequence Curve', fontweight='bold', fontsize=11)
axs[1, 1].set_xlabel(r'Liveness Threshold ($L_{th}$)', fontweight='bold')
axs[1, 1].set_ylabel('Rate (%)', fontweight='bold')
axs[1, 1].grid(True, linestyle=':', alpha=0.6)
axs[1, 1].legend(fontsize=9, loc='center right')

plt.tight_layout()
plt.savefig('Figure_4_2_Individual_Model_Operating_Curves.png', dpi=300)
plt.close()

# ==========================================
# GRAPH 2: Radar Chart for Consolidated Model Comparison
# ==========================================
categories = ['Accuracy', 'Spoof Rejection (1-FAR)', 'True Accept (1-FRR)', 'Computational Velocity', 'Edge Efficiency']
N = len(categories)

# Normalized scores (0 to 100 scale)
cosine_scores = [99.0, 100.0, 98.0, 95.0, 98.0]
cnn_scores    = [99.5, 100.0, 99.0, 65.0, 60.0]
svm_scores    = [99.5, 100.0, 99.0, 85.0, 88.0]
rnn_scores    = [98.5, 100.0, 97.0, 50.0, 55.0]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angles[:-1], categories, color='black', size=10, fontweight='bold')
ax.set_rlabel_position(0)
plt.yticks([40, 60, 80, 100], ["40", "60", "80", "100"], color="grey", size=8)
plt.ylim(30, 105)

# Plot each model profile
for scores, label, color in [
    (cosine_scores, 'Cosine Similarity', '#1f77b4'),
    (cnn_scores, 'CNN Softmax', '#2ca02c'),
    (svm_scores, 'SVM (RBF)', '#ff7f0e'),
    (rnn_scores, 'RNN Temporal', '#d62728')
]:
    vals = scores + scores[:1]
    ax.plot(angles, vals, linewidth=2.2, linestyle='solid', label=label, color=color)
    ax.fill(angles, vals, color=color, alpha=0.1)

plt.title('Multi-Dimensional Comparative Benchmark of Evaluated Models', size=13, fontweight='bold', y=1.08)
plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=10)
plt.tight_layout()
plt.savefig('Figure_4_3_Comparative_Radar_Graph.png', dpi=300)
plt.close()