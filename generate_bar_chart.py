import matplotlib.pyplot as plt

# Data from Table 4.3
architectures = ['Single-Threaded\n(Baseline)', 'Asynchronous\nMultithreaded']
fps_values = [4.2, 32.5]

# Configure the plot style for academic papers
plt.figure(figsize=(8, 6))
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

# Create the bar chart
# Red for the slow baseline, Green for the optimized multithreaded architecture
bars = plt.bar(architectures, fps_values, color=['#d9534f', '#5cb85c'], 
               width=0.5, edgecolor='black', zorder=3)

# Add the exact numbers on top of each bar for clarity
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, 
             f'{yval} FPS', ha='center', va='bottom', 
             fontweight='bold', fontsize=12)

# Labels and Title
plt.title('Figure 4.4: Computational Latency Analysis (Laptop CPU)', fontsize=14, pad=15, fontweight='bold')
plt.ylabel('Frames Per Second (FPS)', fontsize=12, fontweight='bold')
plt.ylim(0, 40) # Set the Y-axis limit slightly higher than the max value for headroom

# Save the figure as a high-resolution image for Microsoft Word
filename = 'Figure_4_4_FPS_Comparison.png'
plt.savefig(filename, dpi=300, bbox_inches='tight')
print(f"[SUCCESS] Academic bar chart generated and saved as {filename}")

# Show the graph on your screen
plt.show()