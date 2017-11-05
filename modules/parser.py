import re

from html.parser import HTMLParser

from modules import utils

SCRIPT_TAG = "script"
SOURCE_ATTRIBUTE = "src"
PROTOCOL_PATTERN = re.compile(r"^https?://.*$")


class Parser(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.__url = url
        self.__scripts = dict()

    def handle_starttag(self, tag, attrs):
        if tag == SCRIPT_TAG:
            link = dict(attrs).get(SOURCE_ATTRIBUTE)
            if link:
                self.__scripts[link] = utils.load_content(
                    link
                    if PROTOCOL_PATTERN.search(link)
                    else utils.parse_protocol_and_domain(self.__url) + link
                )

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self.__scripts

    def error(self, message):
        pass


def parse(url):
    return Parser(url).feed(utils.load_content(url))
