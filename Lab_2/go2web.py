from GoogleSearchApiHttpClient import GoogleSearchApiHttpClient
from HttpResponse import HttpResponse
from WebPageDisplayHttpClient import WebPageDisplayHttpClient
from bs4 import BeautifulSoup
import re

WELCOME_MESSAGE = "\nHi, welcome to go2web!\n" \

HELP_MESSAGE = "Usage:\n" \
               " go2web - u < URL >  # make an HTTP request to the specified URL and print the response \n " \
               "go2web - s < search - term >  # make an HTTP request to search the term using your favorite search " \
               "engine and print top 10 results \n " \
               "go2web ?  # show this help\n"

SEARCH_FLAG = "go2web -s"
DISPLAY_FLAG = "go2web -u"
HELP_COMMAND = "go2web ?"


def read_user_input():
    user_input = input(">>> ")
    parse_user_input(user_input)


def parse_user_input(user_input):
    if is_search_command(user_input):
        command_start_index = user_input.find(SEARCH_FLAG) + len(SEARCH_FLAG)
        command = user_input[command_start_index:].strip()
        process_search_command(command)

    if is_display_command(user_input):
        command_start_index = user_input.find(DISPLAY_FLAG) + len(DISPLAY_FLAG)
        command = user_input[command_start_index:].strip()
        process_display_command(command)

    if is_help_command(user_input):
        print(HELP_MESSAGE)

    else:
        print("Invalid command, use: go2web ? to view the list of available commands")


def is_help_command(user_input):
    return HELP_COMMAND == user_input


def is_search_command(user_input):
    return SEARCH_FLAG in user_input


def is_display_command(user_input):
    return DISPLAY_FLAG in user_input


def process_search_command(command):
    httpClient = GoogleSearchApiHttpClient()
    decoded = httpClient.send(command)
    httpClient.close_connection()

    response = HttpResponse(decoded)

    for item in response.body["items"]:
        print(f"{item['title']} -> {item['link']}")


def process_display_command(command):
    decoded = WebPageDisplayHttpClient().send(command)
    clean_message = remove_html_tags(decoded)
    print(clean_message)


def remove_html_tags(text):
    text = re.sub('<\!DOCTYPE.*?>', '', text, flags=re.IGNORECASE)

    soup = BeautifulSoup(text, 'html.parser')

    for tag in soup(['script', 'style']):
        tag.decompose()

    return soup.get_text()


print(WELCOME_MESSAGE)
print(HELP_MESSAGE)

while True:
    read_user_input()
