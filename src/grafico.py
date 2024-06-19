from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def create_plot(speeds, distance_per_revolution):
    x = [(i + 1) * distance_per_revolution for i in range(len(speeds))]
    y = speeds
    
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    ax.plot(x, y, marker='o', linestyle='-')
    ax.set_xlabel('Metri Percorsi')
    ax.set_ylabel('Velocità (km/h)')
    ax.set_title('Grafico Velocità vs Metri Percorsi')
    
    return fig, ax
