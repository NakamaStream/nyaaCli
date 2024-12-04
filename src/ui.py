from rich.panel import Panel
from rich.table import Table
from rich import box

HEADER_STYLE = "bold cyan"
BORDER_STYLE = "cyan"
TITLE_STYLE = "bold magenta"

def create_search_table():
    table = Table(
        show_header=True,
        header_style=HEADER_STYLE,
        box=box.ROUNDED,
        border_style=BORDER_STYLE,
        title="Search Results",
        title_style=TITLE_STYLE
    )
    
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="green")
    table.add_column("Size", style="blue", justify="right")
    table.add_column("Seeds", style="red", justify="center")
    
    return table

def get_banner():
    """
    Devuelve el banner de la aplicación.
    """
    return """
     ███▄    █▓██   ██▓ ▄▄▄       ▄▄▄       ▄████▄   ██▓     ██▓
     ██ ▀█   █ ▒██  ██▒▒████▄    ▒████▄    ▒██▀ ▀█  ▓██▒    ▓██▒
    ▓██  ▀█ ██▒ ▒██ ██░▒██  ▀█▄  ▒██  ▀█▄  ▒▓█    ▄ ▒██░    ▒██░
    ▓██▒  ▐▌██▒ ░ ▐██▓░░██▄▄▄▄██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██░    ▒██░
    ▒██░   ▓██░ ░ ██▒▓░ ▓█   ▓██▒ ▓█   ▓██▒▒ ▓███▀ ░░██████▒░██████▒
    ░ ▒░   ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░ ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▓  ░
    ░ ░░   ░ ▒░▓██ ░▒░   ▒   ▒▒ ░  ▒   ▒▒ ░  ░  ▒   ░ ░ ▒  ░░ ░ ▒  ░
       ░   ░ ░ ▒ ▒ ░░    ░   ▒     ░   ▒   ░          ░ ░     ░ ░   
             ░ ░ ░           ░         ░   ░ ░          ░  ░    ░  ░
               ░ ░                         ░                          
    """
