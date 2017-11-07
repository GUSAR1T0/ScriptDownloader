def _load(scripts: list) -> dict:
    from core.utilities.utils import load_content

    scripts_dict = dict()
    for script in scripts:
        scripts_dict[script] = load_content(script)
    return scripts_dict


def _save(scripts: dict, path_to_scripts: str) -> None:
    import os
    from core.utilities.parser import parse_domain
    from core.utilities.parser import parse_filename

    for script in scripts:
        directory = os.path.join(path_to_scripts, parse_domain(script))
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        path = os.path.join(directory, parse_filename(script))
        with open(path, 'w') as out:
            out.write(scripts[script])


def download_scripts(site_urls: list, path_to_scripts: str) -> None:
    from core.scripts.parser import ScriptParser

    scripts = ScriptParser.parse(site_urls)
    scripts_dict = _load(scripts)
    _save(scripts_dict, path_to_scripts)
