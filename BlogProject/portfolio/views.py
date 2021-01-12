from django.shortcuts import render
from .models import Portfolio

def pp(request):
    pp = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': pp})