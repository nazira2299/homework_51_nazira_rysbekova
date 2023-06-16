from django.shortcuts import render
from django.http import HttpResponseRedirect

from source.webapp.cat_stats_view import Cat

# Create your views here.

def index(request):
    return render(request, "index.html")

def cat_stats(request):
    if request.method == "GET":
        context = {
            'name': Cat.name,
            'age': Cat.age,
            'happiness': Cat.happiness,
            'satiety': Cat.satiety,
            'sleep': Cat.sleep
        }
        return render(request, 'cat_stats.html', context=context)

    Cat.add_name(request)
    Cat.add_action(request)
    return HttpResponseRedirect(request.path_info)