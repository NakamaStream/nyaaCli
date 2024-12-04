from rich.panel import Panel
from rich.table import Table
from rich import box

def create_search_table():
    table = Table(
        show_header=True,
        header_style="bold cyan",
        box=box.ROUNDED,
        border_style="cyan",
        title="Search Results",
        title_style="bold magenta"
    )
    
    table.add_column("#", style="dim", width=4)
    table.add_column("Name", style="green")
    table.add_column("Size", style="blue", justify="right")
    table.add_column("Seeds", style="red", justify="center")
    
    return table

def get_banner():
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
