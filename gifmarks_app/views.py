from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from gifmarks_app.models import Giflink


# Create your views here.
def index(request):
    categories = Giflink.objects.values("category")

    return render(request, 'gifs/index.html', {
                    'categories': categories,
                })

def show_a_gif(request, gif_id):
    gif = get_object_or_404(Giflink, pk=gif_id)

    return render(request, 'gifs/show_a_gif.html', { 'gif': gif })

def add_a_gif(request):
    if request.method == 'GET':
        categories = Giflink.objects.values("category")
        return render(request, 'gifs/add_a_gif.html', { 'categories': categories })

    if request.method == 'POST':
        try:
            gif = Giflink.objects.get(href=request.POST['href'])
        except Giflink.DoesNotExist:
            gif = Giflink(
                href = request.POST['href'] if request.POST['href'] else None,
                title = request.POST['title'] if request.POST['title'] else None,
                category = request.POST['category'] if request.POST['category'] else None,
            )
            gif.save()

        return HttpResponseRedirect(reverse('gifmarks_app.views.show_a_gif', args=(gif.id,)))

def random_gif_from_category(request, category):
    gif_id = Null if category is None else  Giflink.objects.filter(category=category).order_by('?')[0].pk
    return HttpResponseRedirect(reverse('gifmarks_app.views.show_a_gif', args=(gif_id,)))
