from django.http import JsonResponse

from core.scripts.handler import download_scripts
from ScriptDownloader import settings


def load_process(request):
    if request.GET:
        try:
            sites = request.GET['sites'].split('\n')
            download_scripts(sites, settings.SCRIPTS_DIR)
            return JsonResponse(data={'is_successful': True})
        except Exception as e:
            return JsonResponse(data={'is_successful': False, 'errmsg': 'Exception was raised: ' + str(e)})
