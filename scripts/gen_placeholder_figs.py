#!/usr/bin/env python3
"""
Generate placeholder figures for ensemble size study
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set up the style
plt.style.use(['seaborn-v0_8-whitegrid', 'seaborn-v0_8-paper'])
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 12
})

# Ensure output directory exists
output_dir = Path("figs")
output_dir.mkdir(exist_ok=True)

# Mock data for ensemble sizes 1-8
ensemble_sizes = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# CPU latency data (grows more linearly)
cpu_p50_latency = np.array([4.1, 6.8, 9.2, 12.1, 15.8, 19.4, 23.1, 27.3])
cpu_p99_latency = np.array([8.1, 11.4, 14.9, 18.3, 23.7, 28.2, 34.1, 41.2])

# GPU latency data (flatter initially, then grows)
gpu_p50_latency = np.array([2.8, 3.1, 3.7, 4.2, 5.1, 6.8, 8.4, 10.2])
gpu_p99_latency = np.array([5.2, 6.1, 7.3, 8.7, 11.2, 12.7, 15.9, 19.8])

# Energy data
cpu_energy = np.array([15.2, 23.7, 32.1, 45.2, 58.9, 71.4, 85.3, 102.1])
gpu_energy = np.array([12.8, 18.4, 19.7, 21.3, 23.1, 28.4, 33.7, 41.2])

# Create latency plot
fig, ax = plt.subplots(1, 1, figsize=(6, 4))

# Plot CPU latency
ax.plot(ensemble_sizes, cpu_p50_latency, 'o-', color='tab:blue', 
        label='CPU p50', linewidth=2, markersize=6)
ax.plot(ensemble_sizes, cpu_p99_latency, 's--', color='tab:blue', 
        label='CPU p99', linewidth=2, markersize=6, alpha=0.7)

# Plot GPU latency  
ax.plot(ensemble_sizes, gpu_p50_latency, 'o-', color='tab:orange',
        label='GPU p50', linewidth=2, markersize=6)
ax.plot(ensemble_sizes, gpu_p99_latency, 's--', color='tab:orange',
        label='GPU p99', linewidth=2, markersize=6, alpha=0.7)

# Highlight knee points
ax.axvline(x=4, color='tab:blue', linestyle=':', alpha=0.6, label='CPU knee')
ax.axvline(x=8, color='tab:orange', linestyle=':', alpha=0.6, label='GPU knee')

ax.set_xlabel('Ensemble Size (k)')
ax.set_ylabel('Latency (ms)')
ax.set_title('Latency vs Ensemble Size')
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.5, 8.5)
ax.set_ylim(0, 45)

plt.tight_layout()
plt.savefig(output_dir / "latency_vs_ensemble_size.pdf", dpi=300, bbox_inches='tight')
plt.close()

# Create energy plot
fig, ax = plt.subplots(1, 1, figsize=(6, 4))

ax.plot(ensemble_sizes, cpu_energy, 'o-', color='tab:red', 
        label='CPU', linewidth=2, markersize=6)
ax.plot(ensemble_sizes, gpu_energy, 'o-', color='tab:green',
        label='GPU', linewidth=2, markersize=6)

# Mark budget-friendly sizes
ax.axvline(x=3, color='tab:red', linestyle=':', alpha=0.6, 
           label='CPU budget point')
ax.axvline(x=6, color='tab:green', linestyle=':', alpha=0.6,
           label='GPU budget point')

ax.set_xlabel('Ensemble Size (k)')
ax.set_ylabel('Energy per Inference (mJ)')
ax.set_title('Energy vs Ensemble Size')
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.5, 8.5)
ax.set_ylim(0, 110)

plt.tight_layout()
plt.savefig(output_dir / "energy_vs_ensemble_size.pdf", dpi=300, bbox_inches='tight')
plt.close()

print("✅ Generated placeholder figures:")
print(f"   - {output_dir}/latency_vs_ensemble_size.pdf")
print(f"   - {output_dir}/energy_vs_ensemble_size.pdf")