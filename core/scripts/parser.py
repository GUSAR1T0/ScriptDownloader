from html.parser import HTMLParser

from core.utilities.utils import get_absolute_link
from core.utilities.utils import load_content


class ScriptParser(HTMLParser):
    SCRIPT_TAG = 'script'
    SOURCE_ATTRIBUTE = 'src'

    def __init__(self, site_url: str):
        super().__init__()
        self.__site_url = site_url
        self.__scripts = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag == ScriptParser.SCRIPT_TAG:
            source_link = dict(attrs).get(ScriptParser.SOURCE_ATTRIBUTE)
            if source_link:
                self.scripts.append(get_absolute_link(source_link, self.__site_url))

    def error(self, message: str) -> None:
        pass

    @property
    def scripts(self) -> list:
        return self.__scripts

    @staticmethod
    def parse(site_urls: list) -> list:
        scripts = []
        for site_url in site_urls:
            parser = ScriptParser(site_url)
            data = load_content(site_url)
            HTMLParser.feed(parser, data)
            scripts.extend(parser.scripts)
        return scripts
