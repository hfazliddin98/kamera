from django.urls import path
from bolim.views import home


urlpatterns = [
    path('', home, name='home'),
]