def _load(scripts: list) -> dict:
    from modules.utils import load_content

    scripts_dict = dict()
    for script in scripts:
        scripts_dict[script] = load_content(script)
    return scripts_dict


def _save(scripts: dict) -> None:
    import os
    from modules.utils import parse_domain
    from modules.utils import parse_filename

    for script in scripts:
        directory = 'scripts/' + parse_domain(script)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        path = directory + '/' + parse_filename(script)
        with open(path, 'w') as out:
            out.write(scripts[script])


def get_scripts(site_urls: list) -> None:
    from modules.scripts.parser import ScriptParser

    scripts = ScriptParser.parse(site_urls)
    scripts_dict = _load(scripts)
    _save(scripts_dict)
