import time
import threading
import random
import requests

endpoints = ("alderaan", "endor", "hoth", "coruscant", "yavin4", "dantooine", "corellia", "sullust", "ansion", "bastion", "gralle", "empire")

HOST = "http://rebels:5000/"


def run():
    while True:
         # Randomly select an endpoint from the endpoints list
        target = random.choice(endpoints)

        url = f"{HOST}{target}"
        
        try:
            # Make an HTTP GET request to the selected endpoint
            response = requests.get(url)

            # Print the response status code and URL for logging
            print(f"Firing at target: {url} | Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"An error occurred while firing at target: {url} | Error: {e}")

        # Sleep for a random interval to avoid rapid-fire requests
        time.sleep(random.uniform(1, 5))  # Random sleep between 1 and 5 seconds


if __name__ == "__main__":
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)
