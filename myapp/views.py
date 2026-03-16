from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST.get('text', '')
    if text:
        amount_of_words = len(text.split())
    else:
        amount_of_words = 0
    return render(request, 'counter.html', {'amount': amount_of_words})