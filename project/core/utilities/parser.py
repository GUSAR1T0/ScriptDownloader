def parse_protocol_and_domain(url: str) -> str:
    from urllib import parse
    return '{uri.scheme}://{uri.netloc}'.format(uri=parse.urlparse(url))


def parse_domain(url: str) -> str:
    from urllib import parse
    return '{uri.netloc}'.format(uri=parse.urlparse(url))


def parse_filename(url: str) -> str:
    filename = url.split('/')[-1]
    return filename.split('?')[0]
