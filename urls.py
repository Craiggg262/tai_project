from django.contrib import user
from django.urls import path

urlpatterns = [
    path('user/', user.site.urls),
]
