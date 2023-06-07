from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.foxtons.co.uk/properties-to-rent/london'

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
listings = soup.find('div', class_ = 'content_holder').find_all('div', class_ = 'property_holder')

info = pd.DataFrame()

for index, value in enumerate(listings):
    try:
        listing_name = listings[index].div.find('div', class_ = 'property_summary').h6.text
        zone = listings[index].div.find('div', class_ = 'property_summary').h6.a.span.text
        bedrooms = listings[index].div.find('div', class_ = 'property_summary').find('div', class_ = 'facilities_wrapper').find('span', class_ = 'bedrooms').text
        bathrooms = listings[index].div.find('div', class_ = 'property_summary').find('div', class_ = 'facilities_wrapper').find('span', class_ = 'bathrooms').text
        price_pw = listings[index].div.find('div', class_ = 'property_summary').find('h2', class_ = 'price price-from').strong.data.data.text
        link = listings[index].div.find('div', class_ = 'property_summary').h6.a.get('href')
        info.loc[len(info),['Name', 'Zone', 'Bedrooms','Bathrooms','Price_pw', 'Link']] = [listing_name, zone, bedrooms, bathrooms, price_pw, f'www.foxtons.co.uk{link}' ]
    except:
        pass

info.to_csv('info.csv')