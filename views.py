from django import HttpResponse

def index(request):
    return HttpResponse('index.html')

def login(request):
    return redirect('/index')
