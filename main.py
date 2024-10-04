from fetcher import fetch_content
from parser import scrape_headlines
from saver import save_as_json, save_as_csv

if __name__ == "__main__":
    base_url = 'https://www.cnbc.com/world/?region=world'
    url = f'{base_url}/latest-news'

    # Fetch the webpage content
    html_content = fetch_content(url)

    if html_content:
        # Scrape headlines & links
        headlines = scrape_headlines(html_content, base_url)
        
        # choose JSON or CSV
        output_format = 'json'
        
        # Save the data
        if output_format == 'json':
            save_as_json(headlines, 'headlines.json')
        elif output_format == 'csv':
            save_as_csv(headlines, 'headlines.csv')
