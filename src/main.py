import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils import read_speeds_from_file, populate_table
from grafico import create_plot

distance_per_revolution = 1.552  # Distanza percorsa in ogni giro ruota in metri

# Inizializzazione della variabile speeds
speeds = []

# Funzione per aggiornare i dati dal file selezionato
def update_data(file_path):
    global speeds
    speeds = read_speeds_from_file(file_path)
    populate_table(table, speeds, distance_per_revolution)
    update_plot()

# Funzione per aggiornare il grafico con i nuovi dati
def update_plot():
    global fig, ax, canvas
    fig, ax = create_plot(speeds, distance_per_revolution)
    ax.grid(True)
    canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    fig.canvas.mpl_connect('button_press_event', on_plot_click)

# Funzione per aprire un file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        update_data(file_path)

# Funzione per gestire il click sulla tabella
def on_table_click(event):
    selected_row = table.focus()
    if selected_row:
        values = table.item(selected_row)['values']
        if values:
            index = table.index(selected_row)  # Ottieni l'indice della riga selezionata
            meters = float(values[0])  # Converti in float
            speed = float(values[1])
            update_table(index)
            highlight_point(meters, speed)

# Funzione per gestire il click sul grafico
def on_plot_click(event):
    x_click = event.xdata
    if x_click is not None:
        index = find_nearest_index(x_click)
        if index is not None:
            meters = (index + 1) * distance_per_revolution
            speed = speeds[index]
            update_table(index)
            highlight_point(meters, speed)

def find_nearest_index(x_click):
    min_distance = float('inf')
    nearest_index = None
    for i in range(len(speeds)):
        x_value = (i + 1) * distance_per_revolution
        distance = abs(x_click - x_value)
        if distance < min_distance:
            min_distance = distance
            nearest_index = i
    return nearest_index

# Funzione per evidenziare il punto esatto sul grafico
def highlight_point(meters, speed):
    # Resetta tutti i marker nel grafico
    for line in ax.lines[1:]:
        line.remove()
    ax.axvline(x=meters, color='red', linestyle='-', linewidth=0.7)
    ax.axhline(y=speed, color='red', linestyle='-', linewidth=0.7)
    ax.plot(meters, speed, 'ro', markersize=4)
    # Aggiorna il grafico
    canvas.draw()
    for line in ax.lines[1:]:
        line.remove()

def update_table(index):
    # Ottieni tutti gli elementi della tabella
    items = table.get_children()
    if 0 <= index < len(items):
        item = items[index]
        table.selection_set(item)
        table.focus(item)
        table.see(item)

# Creazione della finestra principale
root = tk.Tk()
root.title("Tabella e Grafico Metri e Velocità")

# Creazione della barra dei menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Aggiunta del menu File
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)

# Creazione della tabella con bordi visibili alle celle
style = ttk.Style()
style.configure("Treeview", rowheight=30, font=('Arial', 12))
style.configure("Treeview.Heading", font=('Arial', 12))
style.configure("Treeview", highlightthickness=0, bd=1, relief='ridge')

table_frame = tk.Frame(root)
table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10, pady=10)

table = ttk.Treeview(table_frame, columns=("Metri", "Velocità"), show="headings", style="Treeview")
table.heading("Metri", text="meters")
table.heading("Velocità", text="Speed")

# Regola la larghezza delle colonne
table.column("Metri", width=150)
table.column("Velocità", width=150)

# Aggiunta del gestore di eventi per il click sulla tabella
table.bind('<ButtonRelease-1>', on_table_click)

# Creazione del grafico con griglia visibile
fig, ax = create_plot(speeds, distance_per_revolution)
ax.grid(True)

# Creazione del canvas per il grafico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Connette l'evento di click del mouse al grafico
cid = fig.canvas.mpl_connect('button_press_event', on_plot_click)

# Posizionamento della tabella nella finestra
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Avvio del loop principale di Tkinter
root.mainloop()
