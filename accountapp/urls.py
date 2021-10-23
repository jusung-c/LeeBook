from django.urls import path

from accountapp.views import hello_world

# accountapp:hello_world (app_name:name)으로 바로 라우팅할 수 있도록
app_name = "accountapp"

urlpatterns = [
    # account/hello_world/
    path('hello_world/', hello_world, name='hello_world')
]