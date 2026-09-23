import matplotlib.pyplot as plt
import numpy as np

# Data for the four algorithms
models = ['Cosine Similarity', 'CNN', 'SVM', 'RNN']
accuracy = [99.0, 99.5, 99.5, 98.5]
far = [0.0, 0.0, 0.0, 0.0]
frr = [2.0, 1.0, 1.0, 3.0]
latency = [8.4, 24.1, 12.6, 38.2]

x = np.arange(len(models))
width = 0.22

fig, ax1 = plt.subplots(figsize=(10, 5.5))

# Plot Accuracy, FAR, and FRR on the primary y-axis
rects1 = ax1.bar(x - width, accuracy, width, label='Accuracy (%)', color='#2ca02c', alpha=0.9)
rects2 = ax1.bar(x, far, width, label='FAR (%)', color='#d62728', alpha=0.9)
rects3 = ax1.bar(x + width, frr, width, label='FRR (%)', color='#ff7f0e', alpha=0.9)

ax1.set_ylabel('Rate (%)', fontsize=11, fontweight='bold')
ax1.set_ylim(0, 115)
ax1.set_xticks(x)
ax1.set_xticklabels(models, fontsize=11, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.4, axis='y')

# Plot Latency as a line overlay on the secondary y-axis
ax2 = ax1.twinx()
line = ax2.plot(x, latency, color='#1f77b4', marker='o', linewidth=2.5, markersize=8, label='Latency (ms)')
ax2.set_ylabel('Inference Latency (ms)', color='#1f77b4', fontsize=11, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#1f77b4')
ax2.set_ylim(0, 50)

# Combine legends
bars_labels = [rects1, rects2, rects3, line[0]]
labels = [l.get_label() for l in bars_labels]
ax1.legend(bars_labels, labels, loc='upper right', frameon=True)

plt.title('Comparative Performance Benchmark of Machine Learning Algorithms', fontsize=13, fontweight='bold', pad=14)
plt.tight_layout()
plt.savefig('Figure_4_2_Comparative_Algorithms_Benchmark.png', dpi=300)
plt.show()