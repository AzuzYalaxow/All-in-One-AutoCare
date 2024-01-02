import requests
import os

def download_car_image(api_key, query, count=1, save_path='images'):
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}

    subscription_id = "6ff9b415-6d17-44bf-b27c-9135f48e4715"
    resource_group = "CarImageDownloader-RG"
    account_name = "cars"

    params = {
        'q': query,
        'count': count,
        'imageType': 'Photo',
    }

    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for i, image in enumerate(data['value']):
            image_url = image['contentUrl']
            image_extension = image_url.split('.')[-1]
            image_filename = f"{query}_{i + 1}.{image_extension}"
            image_path = os.path.join(save_path, image_filename)

            image_content = requests.get(image_url).content

            with open(image_path, 'wb') as f:
                f.write(image_content)

            print(f"Image {i + 1} downloaded: {image_path}")
    else:
        print(f"Error {response.status_code}: {data['error']['message']}")


bing_api_key = '9588495c445641cdac8906e3fbf9810c'
search_query = 'audi rs7 black'

download_car_image(bing_api_key, search_query)