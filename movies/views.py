from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Movie

def index(request):
    movies=Movie.objects.all()
    
    return render(request,'index.html',{'movies':movies})

def detail(request,movie_id):
    try:
        movie=Movie.objects.get(id=movie_id)
        return render(request, 'detail.html',{'movie': movie})
    except MovieDoesNotExist:
        raise Http404()