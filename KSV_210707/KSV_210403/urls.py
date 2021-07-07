from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:entity>/graph/', views.get_graph),
    # path('addnode/', views.add_node, name="addnode"),
    # path('addnode/post/', views.add_node_api, name="add_node_api"),
]