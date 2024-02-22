from blog_post import BlogPost
import requests
from bs4 import BeautifulSoup

def scrape_blog_title(blog_url):
    try:
        # Send a GET request to the blog URL
        response = requests.get(blog_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the blog title (replace this with your actual scraping logic)
            title = soup.find('h1').text.strip()

            return title
        else:
            print(f"Failed to fetch data from {blog_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None