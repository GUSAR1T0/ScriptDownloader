def parse_protocol_and_domain(url: str) -> str:
    from urllib import parse
    return '{uri.scheme}://{uri.netloc}'.format(uri=parse.urlparse(url))


def load_content(url: str) -> str:
    import requests
    return requests.get(url).text
