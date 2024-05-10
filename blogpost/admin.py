from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)     #after applying the models in database regitster them in the admin panel
                            #to see how they look like j