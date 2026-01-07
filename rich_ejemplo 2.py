from rich.console import Console
from rich.table import Table

console = Console()

data = [
    ["Producto", "Precio", "Stock"],
    ["Manzanas", 1.50, 50],
    ["Plátanos", 0.75, 100],
    ["Naranjas", 1.20, 25],
    ["Uvas", 3.00, 10],
]

table = Table(title="Inventario")

for column in data[0]:
    table.add_column(column)

for row in data[1:]:
    precio = row[1]
    stock = row[2]
    precio_color = "green" if precio < 2 else "red"
    stock_color = "yellow" if stock < 30 else "blue"
    table.add_row(row[0], f"[{precio_color}]{precio}[/]", f"[{stock_color}]{stock}[/]")

console.print(table)