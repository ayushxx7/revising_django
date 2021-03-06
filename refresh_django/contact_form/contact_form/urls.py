from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Mandowara Impex Admin"
admin.site.site_title = "Mandowara Impex Admin Portal"
admin.site.index_title = "Welcome to Mandowara Impex"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
