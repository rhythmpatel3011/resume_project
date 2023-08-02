from django.shortcuts import render

# Create your views here.


def home(request):
    varr = {'home': 'active'}
    return render(request, "core/home.html", varr)


def contact(request):
    varr = {'contact': 'active'}
    return render(request, "core/contact.html", varr)
