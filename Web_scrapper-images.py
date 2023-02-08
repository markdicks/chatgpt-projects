import os
import requests
from bs4 import BeautifulSoup

# Create a list of the websites to scrape
websites = ["https://stock.adobe.com/za/search/images?k=cats%20and%20dogs"]

# Specify the directory to save the images
save_dir = "images"

# Specify the format to save the images in
img_format = "png"

# Make the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Loop over each website
for website in websites:
    # Send a GET request to the website
    response = requests.get(website)
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all the img tags
        images = soup.find_all("img")
        
        # Loop over each image
        for i, image in enumerate(images):
            # Get the source URL of the image
            src = image.get("src")
            
            # If the source URL is not None
            if src is not None:
                # Send a GET request to download the image
                img_response = requests.get(src)
                
                # If the request was successful
                if img_response.status_code == 200:
                    # Save the image to disk
                    with open(f"{save_dir}/image_{i}.{img_format}", "wb") as f:
                        f.write(img_response.content)
    # If the request was not successful
    else:
        # Print a message indicating that the request failed
        print(f"Failed to fetch URL: {website} (status code {response.status_code})")
