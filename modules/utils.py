def parse_protocol_and_domain(url: str):
    from urllib import parse
    return '{uri.scheme}://{uri.netloc}'.format(uri=parse.urlparse(url))


def load_content(url: str):
    import requests
    return requests.get(url).text
