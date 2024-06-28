def read_speeds_from_file(file_path):
    speeds = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                speeds.append(float(line.strip()))
            except ValueError:
                continue
    return speeds

def populate_table(table, speeds, distance_per_revolution):
    # Rimuovi tutte le righe esistenti nella tabella
    for item in table.get_children():
        table.delete(item)
    
    for i, speed in enumerate(speeds):
        meters = (i + 1) * distance_per_revolution
        # Formatta i valori a 2 decimali
        meters_formatted = f"{meters:.2f}"
        speed_formatted = f"{speed:.2f}"
        table.insert('', 'end', values=(meters_formatted, speed_formatted))
