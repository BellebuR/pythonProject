import requests

def get_random_cat_image_url():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['url']
        return None
    except requests.RequestException:
        return None