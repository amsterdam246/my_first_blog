from django.urls import path
from . import views

#Each app in your Django project can have its own set of
# URLs that point to different functionalities within that app.

urlpatterns = [
    path('', views.post_list),
  
]

