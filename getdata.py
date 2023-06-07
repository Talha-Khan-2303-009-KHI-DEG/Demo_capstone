import requests

def get_data(urls):
    response = requests.get(urls)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {urls}. Status code: {response.status_code}")
    return None
    
# Define the URLs of the APIs
urls = {
    "PC-Key":"https://xloop-dummy.herokuapp.com/patient_councillor",
    "App-Key":"https://xloop-dummy.herokuapp.com/appointment",
    "Rating-key":"https://xloop-dummy.herokuapp.com/rating",
    "councilor-key":"https://xloop-dummy.herokuapp.com/councillor"
}
