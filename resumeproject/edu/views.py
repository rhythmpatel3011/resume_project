from django.shortcuts import render

# Create your views here.


def skill(request):
    varr = {'skill': 'active'}
    return render(request, 'edu/skill.html', varr)
