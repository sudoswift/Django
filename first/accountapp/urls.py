from accountapp.views import hello_world
from django.urls.conf import include, path

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]