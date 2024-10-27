import time
import threading

endpoints = ("alderaan", "endor", "hoth", "coruscant", "yavin4", "dantooine", "corellia", "sullust", "ansion", "bastion", "gralle", "empire")

HOST = "http://rebels:5000/"


def run():
    while True:
        continue
        ########
        #
        # Insert your code 
        #
        ########


if __name__ == "__main__":
    for _ in range(4):
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)
