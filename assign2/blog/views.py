
from django.http import Http404
from django.shortcuts import render
from .models import B1

# Create your views here.
def show_blog(request):

    return render(request, "get_blog.html", {"blogs": B1.objects.all()})


def get_blog(request, blog_id):
    try:
        blog = B1.objects.get(id=blog_id)
        return render(request, "show_blog.html", {"blog": blog})
    except B1.DoesNotExist:
        raise Http404("We don't have any.")