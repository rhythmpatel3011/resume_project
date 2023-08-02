from django.shortcuts import render

# Create your views here.


def services(request):
    varr = {'services': 'active'}
    return render(request, 'serv/services.html', varr)
