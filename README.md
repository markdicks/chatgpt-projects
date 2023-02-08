# chatgpt-projects
In this repo, this will be all the files chatgpt and I work on. This will contain some files from other repos that chatgpt has assisted me on or just small files that I create to learn chatgpt. My goal is to get proficient in using and understanding ai.


-----Web scrapper-----
The code uses the requests and bs4 libraries to scrape images from a website. The script takes in three arguments: the URL of the page you want to scrape, the directory where you want to save the images, and the format in which you want to save the images (e.g. jpg, png, gif).

First, it sends a GET request to the URL using the requests.get function. If the request is successful (status code 200), it uses the BeautifulSoup class from the bs4 library to parse the HTML content of the page and find all the img tags.

Next, the code creates the specified save directory if it doesn't already exist. Then, it loops over each image and downloads the image by sending another GET request to the image URL and writing the image data to disk. The images are saved with filenames in the format image_{i}.{format}, where i is the index of the image and format is the specified image format (e.g. png).
If the initial GET request to the URL fails, the code outputs a message indicating that it failed to fetch the URL, along with the status code returned by the request.

---------------------
