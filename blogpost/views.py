from django.shortcuts import render
from django.http import HttpResponse

#a view will request information from the model you created before and pass it to a template
# Create your views here.
def app_homeview(request):
    return render(request, 'blogpost/blog_tmp.html', {})

def blogpost(request):
    return HttpResponse("blogpost space")

