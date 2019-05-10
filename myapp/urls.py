from myapp.views.home import home
from django.urls import path

app_name = 'myapp'
urlpatterns = [
    # ex: /myapp/
    path('', home, name='home'),
]
