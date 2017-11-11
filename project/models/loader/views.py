from django.shortcuts import render


def loader_view(request):
    return render(request, 'loader.html')
