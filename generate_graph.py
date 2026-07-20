import matplotlib.pyplot as plt
import numpy as np

# Data from Table 4.1
thresholds = [0.30, 0.35, 0.40, 0.45, 0.50, 0.60]
far = [15.0, 6.0, 0.0, 0.0, 0.0, 0.0]  # False Acceptance Rate
frr = [0.0, 0.0, 2.0, 5.0, 18.0, 55.0] # False Rejection Rate

# Configure the plot style for academic papers
plt.figure(figsize=(9, 6))
plt.grid(True, linestyle='--', alpha=0.7)

# Plot the lines
plt.plot(thresholds, far, marker='o', linewidth=2.5, color='#d9534f', label='False Acceptance Rate (FAR)')
plt.plot(thresholds, frr, marker='s', linewidth=2.5, color='#5bc0de', label='False Rejection Rate (FRR)')

# Highlight the optimal threshold zone
plt.axvspan(0.40, 0.45, color='#5cb85c', alpha=0.15, label='Optimal Operational Zone')

# Labels and Title
plt.title('Figure 4.2: FAR vs. FRR across Cosine Similarity Thresholds', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Cosine Similarity Threshold', fontsize=12, fontweight='bold')
plt.ylabel('Error Rate (%)', fontsize=12, fontweight='bold')

# Customize ticks
plt.xticks(thresholds)
plt.yticks(np.arange(0, 61, 10))

# Add a legend
plt.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)

# Save the figure as a high-resolution image for Microsoft Word
filename = 'Figure_4_2_FAR_vs_FRR.png'
plt.savefig(filename, dpi=300, bbox_inches='tight')
print(f"[SUCCESS] Academic graph generated and saved as {filename}")

# Show the graph on your screen
plt.show()