from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

class AnimeTorrentCLI:
    def __init__(self):
        self.base_url = "https://nyaa.si"
        self.console = Console()
        self.language = self.select_language()
        self.texts = self.get_language_texts()
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
            
    def get_language_texts(self):
        texts = {
            'en': {
                'searching': 'Searching...',
                'enter_anime': 'Enter anime name',
                'exit_text': "'exit' to quit",
                'thanks': 'Thanks for using the searcher!',
                'open_torrent': 'Do you want to open any torrent?',
                'number_cancel': "Number or 'n' to cancel",
                'opening': 'Opening magnet link...',
                'no_results': 'No results found.',
                'select_results': 'How many results do you want to see? (1-30)',
                'invalid_number': 'Please enter a valid number between 1 and 30'
            },
            'es': {
                'searching': 'Buscando...',
                'enter_anime': 'Ingresa el nombre del anime',
                'exit_text': "'exit' para salir",
                'thanks': '¡Gracias por usar el buscador!',
                'open_torrent': '¿Deseas abrir algún torrent?',
                'number_cancel': "Número o 'n' para cancelar",
                'opening': 'Abriendo enlace magnet...',
                'no_results': 'No se encontraron resultados.',
                'select_results': '¿Cuántos resultados quieres ver? (1-30)',
                'invalid_number': 'Por favor ingresa un número válido entre 1 y 30'
            }
        }
        return texts[self.language]
        
    def show_banner(self):
        banner = """
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
        self.console.print(Panel(banner, style="bold magenta", box=box.DOUBLE))
        
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

    def search_anime(self, query):
        try:
            self.console.print(f"[yellow]{self.texts['searching']}[/yellow]")
            search_url = f"{self.base_url}/?f=0&c=1_0&q={query}"
            response = requests.get(search_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            for row in soup.select('table tbody tr')[:self.max_results]:  # Usar max_results en lugar de 10
                name = row.select('td:nth-child(2) a')[-1].text
                size = row.select('td:nth-child(4)')[0].text
                seeds = row.select('td:nth-child(6)')[0].text
                magnet = row.select('td:nth-child(3) a')[1]['href']
                
                results.append([
                    name[:70] + "..." if len(name) > 70 else name,
                    size,
                    seeds,
                    magnet
                ])
            
            return results
            
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
            return []

    def show_results(self, results):
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

        for idx, result in enumerate(results):
            table.add_row(
                str(idx),
                result[0],
                result[1],
                result[2]
            )
            
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
            
        results = cli.search_anime(search)
        
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
