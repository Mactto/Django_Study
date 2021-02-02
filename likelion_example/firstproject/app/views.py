from django.shortcuts import render

# Create your views here.
def getInfo(request):
    return render(request, 'index.html')

def hello(request):
    userName = request.GET['name']
    return render(request, 'hello.html', {'name': userName})