def load_content(url: str) -> str:
    import requests
    return requests.get(url).text


def parse_protocol_and_domain(url: str) -> str:
    from urllib import parse
    return '{uri.scheme}://{uri.netloc}'.format(uri=parse.urlparse(url))


def parse_domain(url: str) -> str:
    from urllib import parse
    return '{uri.netloc}'.format(uri=parse.urlparse(url))


def parse_filename(url: str) -> str:
    filename = url.split('/')[-1]
    return filename.split('?')[0]


def get_absolute_link(source_link: str, site_url: str) -> str:
    import re

    protocol_pattern = re.compile(r'^https?://.*$')
    if protocol_pattern.search(source_link):
        return source_link
    else:
        return parse_protocol_and_domain(site_url) + ('/' if source_link[0] != '/' else '') + source_link
