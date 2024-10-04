from bs4 import BeautifulSoup
import re

def scrape_headlines(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Define the structure
    headlines_data = []
    
    for headline in soup.find_all(['h2', 'h3']):
        try:
            link_tag = headline.find('a')
            if link_tag and link_tag['href']:
                headline_text = headline.get_text(strip=True)
                headline_url = link_tag['href']
                
                if not re.match(r'^https?://', headline_url):
                    headline_url = f"{base_url}/{headline_url.lstrip('/')}"
                
                headlines_data.append({
                    'headline': headline_text,
                    'url': headline_url
                })
        except (AttributeError, KeyError) as e:
            print(f"Skipping malformed element: {e}")
            continue
    
    return headlines_data
