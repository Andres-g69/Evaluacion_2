from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def publicacion(request):
    return render(request, 'publicacion.html')
def ranking(request):
    return render(request, 'ranking.html')