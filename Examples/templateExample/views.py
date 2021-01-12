from django.shortcuts import render

# Create your views here.
def ex1(request):
    name = "최세환"
    age = "23"
    return render(request, 'ex1.html', {'name':name, 'age':age})

def ex2(request):
    return render(request, 'ex2.html', {'n': range(10)})