import requests
from bs4 import BeautifulSoup
from src.config import BASE_URL

def search_anime(query, max_results):
    try:
        search_url = f"{BASE_URL}/?f=0&c=1_0&q={query}"
        response = requests.get(search_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for row in soup.select('table tbody tr')[:max_results]:
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
        return []
