from rich.console import Console
from rich.panel import Panel
from rich import box
import webbrowser
import time

from src.config import LANGUAGE_TEXTS
from src.ui import create_search_table, get_banner
from src.scraper import search_anime

class AnimeTorrentCLI:
    def __init__(self):
        self.console = Console()
        self.language = self.select_language()
        self.texts = LANGUAGE_TEXTS[self.language]
        self.max_results = self.select_max_results()
        
    def select_language(self):
        self.console.clear()
        self.console.print(Panel.fit(
            "[bold]Select Language / Seleccionar Idioma[/bold]\n\n" +
            "1. English\n2. Español", 
            style="cyan"
        ))
        while True:
            choice = self.console.input("\n[bold yellow]Choose/Elegir (1/2): [/bold yellow]")
            if choice in ['1', '2']:
                return 'en' if choice == '1' else 'es'

    def select_max_results(self):
        self.console.clear()
        self.console.print(Panel.fit(
            f"[bold]{self.texts['select_results']}[/bold]", 
            style="cyan"
        ))
        while True:
            choice = self.console.input("\n[bold yellow]> [/bold yellow]")
            try:
                num = int(choice)
                if 1 <= num <= 30:
                    return num
                else:
                    self.console.print(f"[red]{self.texts['invalid_number']}[/red]")
            except ValueError:
                self.console.print(f"[red]{self.texts['invalid_number']}[/red]")

    def show_banner(self):
        self.console.print(Panel(get_banner(), style="bold magenta", box=box.DOUBLE))

    def show_results(self, results):
        table = create_search_table()
        for idx, result in enumerate(results):
            table.add_row(str(idx), result[0], result[1], result[2])
        self.console.print(table)

def main():
    cli = AnimeTorrentCLI()
    
    while True:
        cli.console.clear()
        cli.show_banner()
        
        search = cli.console.input(f"\n[bold yellow]{cli.texts['enter_anime']}[/bold yellow] ([red]{cli.texts['exit_text']}[/red]): ")
        
        if search.lower() == 'exit':
            cli.console.print(Panel.fit(f"\n{cli.texts['thanks']}\n", 
                                      style="bold green", 
                                      box=box.DOUBLE))
            break
            
        results = search_anime(search, cli.max_results)
        
        if results:
            cli.show_results(results)
            
            option = cli.console.input(f"\n[bold yellow]{cli.texts['open_torrent']}[/bold yellow] ({cli.texts['number_cancel']}): ")
            if option.isdigit() and 0 <= int(option) < len(results):
                cli.console.print(f"[green]{cli.texts['opening']}[/green]")
                webbrowser.open(results[int(option)][3])
                time.sleep(2)
        else:
            cli.console.print(f"[red]{cli.texts['no_results']}[/red]")
            time.sleep(2)

if __name__ == "__main__":
    main()
