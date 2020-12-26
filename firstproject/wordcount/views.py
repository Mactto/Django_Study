from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    dic = {}
    for w in words:
        if w in dic:
            dic[w]+=1
        else:
            dic[w]=1

    return render(request, 'result.html', {'fulltext':text, 'total_len': len(words), 'dictionary': dic.items()})