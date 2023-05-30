# import json
# import string
#
# import requests
# from bs4 import BeautifulSoup
#
# # url = input("Input the URL:")
# url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
# response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# # data = response.json()
# # quote = data.get('content')
# webpage_content = response.content
# soup = BeautifulSoup(webpage_content, 'html.parser')
# # a = soup.find('div', {"class": "article__teaser"}).text
# articles = soup.findAll('article')
# # with open("file.txt", "wb") as file:
# #     for article in articles:
# #         file.write(str(article).encode('utf-8'))
# # if response.status_code == 200 and quote is not None:
# #     print(data.get('content'))
# # else:
# #     print("Invalid quote resource!")
# # soup = BeautifulSoup(webpage_content, 'html.parser')
# # if 'articles' not in url:
# #     print("Invalid page!")
# # else:
# #     output = {"title": soup.find('title').get_text(),
# #               "description": soup.find('meta', attrs={'name': 'description'}).get('content')}
# # if response.status_code == 200:
# #     with open('source.html', 'wb') as file:
# #         file.write(webpage_content)
# #         print("Content saved.")
# # else:
# #     print(f"The URL returned {response.status_code}!")
# #     # print(output)
# articles = soup.findAll('article')
#
# for article in articles:
#     # Find the article type
#     article_type = article.find('span', attrs={'data-test': 'article.type'})
#     if article_type is None or article_type.text != 'News':
#         continue
#
#     # Find the article link
#     article_link = article.find('a', attrs={'data-track-action': 'view article'})
#     if article_link is None:
#         continue
#
#     # Get the article title and clean it for the filename
#     article_title = article_link.text.strip()
#     for punctuation in string.punctuation:
#         article_title = article_title.replace(punctuation, "")
#     article_title = article_title.replace(" ", "_")
#
#     # Retrieve the article page
#     article_url = "https://www.nature.com" + article_link['href']
#     article_response = requests.get(article_url)
#     if article_response.status_code != 200:
#         continue
#
#     # Parse the article page
#     article_soup = BeautifulSoup(article_response.content, "html.parser")
#
#     # Find the article body
#     article_body = article_soup.find('p', attrs={'class': 'article__teaser'})
#     if article_body is None:
#         continue
#
#     # Generate the filename for the article
#     file_name = f"{article_title}.txt"
#
#     # Remove punctuation marks from the filename
#     file_name = file_name.translate(str.maketrans("", "", string.punctuation))
#
#     # Replace whitespaces in the filename with underscores
#     file_name = file_name.replace(" ", "_")
#
#     # Save the article body to the file
#     with open(file_name, "w", encoding="utf-8") as file:
#         file.write(article_body.text.strip())
#
# import requests
# from bs4 import BeautifulSoup
# import string
#
#
# # URL of the webpage to scrape
# url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
#
# # Send a GET request to fetch the webpage content
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Find all articles on the page
#     articles = soup.find_all('article')
#
#     #Loop over each article
#     for article in articles:
#         # Find the article type
#         article_type = article.find('span', attrs={'data-test': 'article.type'})
#         if article_type is None or article_type.text != 'News':
#             continue
#
#         # Find the article link
#         article_link = article.find('a', attrs={'data-track-action': 'view article'})
#         if article_link is None:
#             continue
#
#         # Get the article title and clean it for the filename
#         article_title = article_link.text.strip()
#         for punctuation in string.punctuation:
#             article_title = article_title.replace(punctuation, "")
#         article_title = article_title.replace(" ", "_")
#
#         # Retrieve the article page
#         article_url = "https://www.nature.com" + article_link['href']
#         article_response = requests.get(article_url)
#         if article_response.status_code != 200:
#             continue
#
#         # Parse the article page
#         article_soup = BeautifulSoup(article_response.content, "html.parser")
#
#         # Find the article body
#         article_body = article_soup.find('p', attrs={'class': 'article__teaser'})
#         if article_body is None:
#             continue
#
#         # Save the article body to a text file
#         file_name = f"{article_title}.txt"
#         with open(file_name, "w", encoding="utf-8") as file:
#             file.write(article_body.text.strip())
#
#         print(f"Saved article: {file_name}")
# else:
#     print("Failed to retrieve the webpage content.")

import requests
from bs4 import BeautifulSoup
import os
import string

def save_articles(pages, article_type):
    # Base URL of the webpage to scrape
    base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="

    # Loop over each page
    for page in range(1, pages + 1):
        page_directory = f"Page_{page}"
        os.makedirs(page_directory, exist_ok=True)

        # URL of the webpage for the current page
        url = base_url + str(page)

        # Send a GET request to fetch the webpage content
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all articles on the page
            articles = soup.find_all('article')

            # Loop over each article
            for article in articles:
                # Find the article type
                article_type_elem = article.find('span', attrs={'data-test': 'article.type'})
                if article_type_elem is None or article_type_elem.text != article_type:
                    continue

                # Find the article link
                article_link = article.find('a', attrs={'data-track-action': 'view article'})
                if article_link is None:
                    continue

                # Get the article title and clean it for the filename
                article_title = article_link.text.strip()
                for punctuation in string.punctuation:
                    article_title = article_title.replace(punctuation, "")
                article_title = article_title.replace(" ", "_")

                # Retrieve the article page
                article_url = "https://www.nature.com" + article_link['href']
                article_response = requests.get(article_url)
                if article_response.status_code != 200:
                    continue

                # Parse the article page
                article_soup = BeautifulSoup(article_response.content, "html.parser")

                # Find the article body
                article_body = article_soup.find('p', attrs={'class': 'article__teaser'})
                if article_body is None:
                    continue

                # Save the article body to a text file in the respective page directory
                file_name = f"{article_title}.txt"
                file_path = os.path.join(page_directory, file_name)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(article_body.text.strip())

                print(f"Saved article: {file_path}")

        else:
            print(f"Failed to retrieve the webpage content for page {page}.")

# User input for number of pages and article type
num_pages = int(input())
article_type = input()

# Call the function to save the articles
save_articles(num_pages, article_type)
