
from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path('',include('polls.urls')),
    path('admin/', admin.site.urls),
]
