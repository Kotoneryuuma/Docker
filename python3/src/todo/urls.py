from django.conf.urls import url
from . import views
                    
urlpatterns = [
     url(r'^$', views.index),
     url(r'^addTodo$', views.add),
     url(r'^edit/(?P<idr>\d+)/process$', views.edit_process),
     url(r'^deleteTodo/(?P<idr>\d+)$', views.delete),
     url(r'^editTodo/(?P<idr>\d+)$', views.edit),
]