from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def create_plot(speeds, distance_per_revolution):
    x = [(i + 1) * distance_per_revolution for i in range(len(speeds))]
    y = speeds
    
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    ax.plot(x, y, marker='o', linestyle='-', markersize=4)
    ax.set_xlabel('DISTANCE')
    ax.set_ylabel('SPEED [km/h]')
    
    return fig, ax
