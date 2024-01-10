from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def menu(request):
    return render(request,'menu.html')
def about(request):
    return render(request,'about.html')
def table(request):
    return render(request,'table.html')
def contact(request):
    return render(request,'contact.html')
