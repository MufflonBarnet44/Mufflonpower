import requests
from bs4 import BeautifulSoup

# URL till sidan vi vill skrapa
url = "https://sv.wikipedia.org/wiki/Web_scraping"

# Skicka en HTTP-förfrågan till sidan
response = requests.get(url)

# Kontrollera att sidan kunde hämtas
if response.status_code == 200:
    # Skapa ett BeautifulSoup-objekt
    soup = BeautifulSoup(response.text, 'html.parser')

    # Hämta sidans titel
    title = soup.find('h1').text

    print("Sidtitel:", title)
else:
    print("Misslyckades att hämta sidan. Statuskod:", response.status_code)
