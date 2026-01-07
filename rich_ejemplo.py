from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def display_panel(message):
    panel = Panel(message, title='Información Importante', border_style='blue')
    console.print(panel)

def create_table(data):
    table = Table(title='Datos Relevantes')
    table.add_column('ID', style='cyan')
    table.add_column('Nombre', style='magenta')
    table.add_column('Valor', style='green')

    for item in data:
        table.add_row(str(item['id']), item['name'], str(item['value']))
    
    console.print(table)

def process_items(items):
    with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}')) as progress:
        task = progress.add_task('[cyan]Procesando...', total=len(items))
        for item in items:
            # Simulando procesamiento
            import time; time.sleep(1)  
            progress.update(task, advance=1)
            console.log(f'Procesado {item['name']}')
    console.log('[bold green]Todos los items han sido procesados.')

if __name__ == '__main__':
    console.print('[bold blue]Bienvenido al sistema de gestión!', style='bold yellow')

    data = [
        {'id': 1, 'name': 'Item A', 'value': 100},
        {'id': 2, 'name': 'Item B', 'value': 200},
        {'id': 3, 'name': 'Item C', 'value': 300},
    ]

    display_panel('A continuación se presentarán los datos.')
    create_table(data)
    process_items(data)
