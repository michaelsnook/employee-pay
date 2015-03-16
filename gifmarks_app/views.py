from django.shortcuts import render
from gifmarks_app.models import Giflink


# Create your views here.
def index(request):
    categories = Giflink.objects.values("category")

    return render(request, 'gifs/index.html', {
                    'categories': categories,
                })

def show_a_gif(request, gif_id):
    gif = Giflink.objects.get(pk=gif_id)

    return render(request, 'gifs/show_a_gif.html', { 'gif': gif })
