# chatgpt-projects
In this repo, this will be all the files chatgpt and I work on. This will contain some files from other repos that chatgpt has assisted me on or just small files that I create to learn chatgpt. My goal is to get proficient in using and understanding ai.


-----Web scrapper-----
The code uses the requests and bs4 libraries to scrape images from a website. The script takes in three arguments: the URL of the page you want to scrape, the directory where you want to save the images, and the format in which you want to save the images (e.g. jpg, png, gif).

First, it sends a GET request to the URL using the requests.get function. If the request is successful (status code 200), it uses the BeautifulSoup class from the bs4 library to parse the HTML content of the page and find all the img tags.

Next, the code creates the specified save directory if it doesn't already exist. Then, it loops over each image and downloads the image by sending another GET request to the image URL and writing the image data to disk. The images are saved with filenames in the format image_{i}.{format}, where i is the index of the image and format is the specified image format (e.g. png).
If the initial GET request to the URL fails, the code outputs a message indicating that it failed to fetch the URL, along with the status code returned by the request.


-----Budget Calculator-----
This code uses Streamlit to create a web page with inputs for adding income and expenses, and displays the current balance and list of transactions. You can run this code using the Streamlit command-line tool to start a local web server, and the web page will be accessible in your web browser.


-------Digital clock-------
This Python code creates an impressive digital clock using the tkinter module for creating the graphical user interface and the datetime module for getting the current time. The clock displays the live time in a 24-hour format and includes some cool features such as the ability to toggle the display of seconds and milliseconds. The clock is updated every 100 milliseconds using the after method, and is displayed in a large font on a black background. The clock can be run as a standalone application, and is designed to be customizable and extensible for further development.


---------------------
