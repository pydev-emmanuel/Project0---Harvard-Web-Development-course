from django.shortcuts import render


def search(request):
    return render(request, 'search/search.html')


def image_search(request):
    return render(request, 'search/image_search.html')


def advanced_search(request):
    return render(request, 'search/advanced_search.html')
