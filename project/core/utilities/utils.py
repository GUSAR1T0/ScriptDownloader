def load_content(url: str) -> str:
    import requests
    return requests.get(url).text


def get_absolute_link(source_link: str, site_url: str) -> str:
    import re
    from project.core.utilities.parser import parse_protocol_and_domain

    protocol_pattern = re.compile(r'^https?://.*$')
    if protocol_pattern.search(source_link):
        return source_link
    else:
        return parse_protocol_and_domain(site_url) + ('/' if source_link[0] != '/' else '') + source_link
