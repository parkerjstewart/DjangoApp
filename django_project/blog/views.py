from django.shortcuts import render
from .models import Post


# render still returns an HttpResponse 
# these functions always need to return an HttpResponse or an exception
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')



