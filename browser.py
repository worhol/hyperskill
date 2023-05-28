import argparse
import encodings
import os
import sys
from collections import deque

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

parser = argparse.ArgumentParser()
parser.add_argument("dir")
args = parser.parse_args()
if not os.access(args.dir, os.F_OK):
    os.mkdir(args.dir)
backlist = deque()
# or user_input != "nytimes.com" or user_input != "bloomberg.com"
while True:
    user_input = input()
    if ('.' not in user_input) and user_input != "exit" and user_input != "back":
        print("Invalid URL")
    if user_input == "exit":
        break
    if user_input == "back":
        if len(backlist) == 0:
            pass
        else:
            name = backlist.pop()
            print(name)
    # if user_input == "nytimes.com":
    #     name = user_input[:-4]
    #     file_path = os.path.join(os.path.abspath(args.dir), name)
    #     with open(file_path, 'w') as file:
    #         file.write(nytimes_com)
    #     backlist.appendleft(nytimes_com)
    #     print(nytimes_com)
    # if user_input == "bloomberg.com":
    #     name = user_input[:-4]
    #     file_path = os.path.join(os.path.abspath(args.dir), name)
    #     with open(file_path, 'w') as file:
    #         file.write(bloomberg_com)
    #     backlist.appendleft(bloomberg_com)
    #     print(bloomberg_com)

    name = user_input[:-4]
    # print(name)
    if '.' in user_input:
        r = requests.get("https://" + user_input)
        soup = BeautifulSoup(r.content, 'html.parser')
        allowed_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
        text_content = []
        output=''
        for tag in soup.find_all(allowed_tags):
            if tag.name == 'a':
                link_text = f"{Fore.BLUE}{tag.get_text()}{Style.RESET_ALL}"
                text_content.append(link_text)
            else:
                text_content.append(tag.get_text())
        output = '\n'.join(text_content)
        file_path = os.path.join(os.path.abspath(args.dir), name[:4])
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(output)
        # backlist.appendleft(nytimes_com)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            print(file_content)
