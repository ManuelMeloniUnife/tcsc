import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils import read_speeds_from_file, populate_table
from grafico import create_plot

# Percorso del file di testo
file_path = 'data/velocita.txt'

# Legge le velocità dal file
speeds = read_speeds_from_file(file_path)
distance_per_revolution = 1.552  # Distanza percorsa in ogni giro ruota in metri

# Funzione per gestire il click sulla tabella
def on_table_click(event):
    # Ottiene l'indice della riga selezionata
    selected_row = table.focus()
    if selected_row:
        # Ottiene i valori della riga selezionata
        values = table.item(selected_row)['values']
        if values:
            meters = float(values[0])  # Converti in float
            speed = values[1]
            # Trova l'indice corrispondente nel dataset
            index = int(meters / distance_per_revolution) - 1
            # Evidenzia il punto sul grafico
            highlight_point(index)

# Funzione per evidenziare il punto esatto sul grafico
def highlight_point(index):
    # Resetta tutti i marker nel grafico
    for line in ax.lines:
        line.set_markerfacecolor('none')
    
    # Evidenzia il punto esatto
    ax.lines[0].set_marker('o')
    ax.lines[0].set_markersize(5)
    ax.lines[0].set_alpha(0.5)
    ax.lines[0].set_linewidth(1)
    ax.lines[0].set_markerfacecolor('blue')
    ax.lines[0].set_markeredgecolor('blue')
    ax.lines[0].set_markevery([index])
    
    canvas.draw()

    # Fa scorrere automaticamente la tabella fino alla riga selezionata
    update_table((index + 1) * distance_per_revolution)

# Funzione per gestire il click sul grafico
def on_plot_click(event):
    # Ottiene le coordinate del click nel sistema di coordinate del grafico
    x_click = event.xdata
    if x_click is not None:
        # Cerca l'indice del punto nel dataset delle velocità basato sulla coordinata x del click
        index = find_nearest_index(x_click)
        if index is not None:
            # Ottiene i metri e la velocità corrispondenti
            meters = (index + 1) * distance_per_revolution
            speed = speeds[index]
            # Aggiorna la tabella con i valori del punto più vicino
            update_table(meters)

def find_nearest_index(x_click):
    # Cerca l'indice del punto nel dataset delle velocità basato sulla coordinata x del click
    min_distance = float('inf')
    nearest_index = None
    for i in range(len(speeds)):
        x_value = (i + 1) * distance_per_revolution
        distance = abs(x_click - x_value)
        if distance < min_distance:
            min_distance = distance
            nearest_index = i
    return nearest_index

def update_table(meters):
    # Trova la riga corrispondente nella tabella
    for item in table.get_children():
        values = table.item(item, 'values')
        if values and float(values[0]) == meters:
            table.selection_set(item)
            table.focus(item)
            # Fa scorrere la tabella fino alla riga selezionata
            table.see(item)
            break

# Creazione della finestra principale
root = tk.Tk()
root.title("Tabella e Grafico Metri e Velocità")

# Creazione della tabella con bordi visibili alle celle
style = ttk.Style()
style.configure("Treeview", rowheight=30, font=('Arial', 12))
style.configure("Treeview.Heading", font=('Arial', 12))
style.configure("Treeview", highlightthickness=0, bd=1, relief='ridge')

table = ttk.Treeview(root, columns=("Metri", "Velocità"), show="headings", style="Treeview")
table.heading("Metri", text="Metri Percorsi")
table.heading("Velocità", text="Velocità (km/h)")

# Popolamento della tabella con i dati
populate_table(table, speeds, distance_per_revolution)

# Aggiunta del gestore di eventi per il click sulla tabella
table.bind('<ButtonRelease-1>', on_table_click)

# Creazione del grafico con griglia visibile
fig, ax = create_plot(speeds, distance_per_revolution)
ax.grid(True)

# Creazione del canvas per il grafico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Connette l'evento di click del mouse al grafico
cid = fig.canvas.mpl_connect('button_press_event', on_plot_click)

# Posizionamento della tabella nella finestra
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Avvio del loop principale di Tkinter
root.mainloop()
