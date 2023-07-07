from django.shortcuts import render


posts = [
    {
        'author': "coreyMS", 
        'title': 'post 1', 
        'content': 'first post content', 
        'date_posted': "August 27th, 2018"
    }, 
    {
        'author': "Parker S.", 
        'title': 'post 2', 
        'content': 'second post content', 
        'date_posted': "August 27th, 2018"
    }, 
    {
        'author': "RandUser3", 
        'title': 'post 3', 
        'content': 'third post content', 
        'date_posted': "August 27th, 2018"
    }, 
]


# render still returns an HttpResponse 
# these functions always need to return an HttpResponse or an exception
def home(request):
    context = {
        'posts': posts,
        'title': 'Testing'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')



