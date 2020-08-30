from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dbhdfnvmkbnlj/', admin.site.urls),
    path('', include('base.urls'))
]


# dbhdfnvmkbnlj - admin url
