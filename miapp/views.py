from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def fort(request):
    return render(request, 'fort.html')
