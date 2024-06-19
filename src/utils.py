def read_speeds_from_file(file_path):
    speeds = []
    with open(file_path, 'r') as file:
        for line in file:
            speed_kmh = float(line.strip().replace(",", "."))
            speeds.append(speed_kmh)
    return speeds


def populate_table(table, speeds, distance_per_revolution):
    for i, speed in enumerate(speeds):
        meters = (i + 1) * distance_per_revolution
        table.insert("", "end", values=(round(meters, 3), round(speed, 3)))
