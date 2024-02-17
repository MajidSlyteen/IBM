import yfinance as yf
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Question 1: Use yfinance to Extract Tesla Stock Data
tesla_data = yf.Ticker('TSLA').history(period='max')
tesla_data.reset_index(inplace=True)
print("Question 1: Tesla Stock Data")
print(tesla_data.head())

# Question 2: Use Webscraping to Extract Tesla Revenue Data
tesla_revenue_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_response = requests.get(tesla_revenue_url)
tesla_soup = BeautifulSoup(tesla_response.text, "html.parser")

tesla_revenue_table = tesla_soup.find("table", class_="historical_data_table")
if tesla_revenue_table:
    tesla_revenue_data = tesla_revenue_table.find_all("tr")[1:]

    tesla_revenue = []
    for row in tesla_revenue_data:
        cols = row.find_all("td")
        if len(cols) >= 2:  # Ensure there are at least two columns
            revenue = cols[1].text.strip()
            tesla_revenue.append(revenue)

    print("\nQuestion 2: Tesla Revenue Data")
    print(tesla_revenue[-5:])
else:
    print("Revenue table not found on the webpage.")

# Question 3: Use yfinance to Extract GameStop Stock Data
gme_data = yf.Ticker('GME').history(period='max')
gme_data.reset_index(inplace=True)
print("\nQuestion 3: GameStop Stock Data")
print(gme_data.head())

# Question 4: Use Webscraping to Extract GameStop Revenue Data
gme_revenue_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_response = requests.get(gme_revenue_url)
gme_soup = BeautifulSoup(gme_response.text, "html.parser")

gme_revenue_table = gme_soup.find("table", class_="historical_data_table")
if gme_revenue_table:
    gme_revenue_data = gme_revenue_table.find_all("tr")[1:]

    gme_revenue = []
    for row in gme_revenue_data:
        cols = row.find_all("td")
        if len(cols) >= 2:  # Ensure there are at least two columns
            revenue = cols[1].text.strip()
            gme_revenue.append(revenue)

    print("\nQuestion 4: GameStop Revenue Data")
    print(gme_revenue[-5:])
else:
    print("Revenue table not found on the webpage.")

# Question 5: Plot Tesla Stock Graph
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.show()

make_graph(tesla_data, "Tesla Stock Graph")

# Question 6: Plot GameStop Stock Graph
make_graph(gme_data, "GameStop Stock Graph")