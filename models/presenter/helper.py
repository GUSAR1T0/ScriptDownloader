import os

from ScriptDownloader import settings


def load_scripts():
    scripts = {}
    for root, dirs, filenames in os.walk(settings.SCRIPTS_DIR):
        for filename in filenames:
            with open(os.path.join(root, filename), "r") as file:
                scripts[root.split('\\')[-1] + '/' + filename] = file.read()
    return scripts
