import requests
from bs4 import BeautifulSoup
import os

def scrape_images(url, save_dir):
    # send a GET request to the URL
    response = requests.get(url)

    # parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # find all image tags on the page
    images = soup.find_all("img")

    # loop over each image
    for i, image in enumerate(images):
        # get the source URL of the image
        src = image.get("src")

        # send a GET request to download the image
        response = requests.get(src)

        # save the image to disk
        with open(f"{save_dir}/image_{i}.jpg", "wb") as f:
            f.write(response.content)

# specify the URL of the page you want to scrape
url = "https://www.example.com/images"

# specify the directory where you want to save the images
save_dir = "images"

# create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# call the scrape_images function
scrape_images(url, save_dir)
