from . import views
from django.urls import include, path

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('bulkmail/', views.bulkmail, name='bulkmail'),
]
