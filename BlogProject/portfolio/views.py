from django.shortcuts import render


def pp(request):
    return render(request, 'portfolio.html')