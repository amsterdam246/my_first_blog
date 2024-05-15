from django.shortcuts import render
from django.http import HttpResponse
from . models import Post  #viewing our models in the template 
from django.utils import timezone

#a view will request information from the model you created before and pass it to a template
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blogpost/blog_tmp.html', {'posts': posts})

def index(request):
    return HttpResponse('home page')
