from django.urls import path
from todolist.views import show_todolist
from todolist.views import show_xml 
from todolist.views import show_json
from todolist.views import show_json_by_id
from todolist.views import show_xml_by_id
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
]