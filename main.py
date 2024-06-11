from ScraperClass import Scraper
import pandas as pd

# Uso de la clase
url = 'https://www.bbc.com/mundo/topics/c7zp57yyz25t'
scraper = Scraper(url)
news_links = scraper.run(100)


df = pd.read_csv("datos_noticias.csv", sep=",")
print(df)