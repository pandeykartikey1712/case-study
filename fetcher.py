import requests

def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to retrieve page with status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
