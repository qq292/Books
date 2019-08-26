from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='books'),

]
