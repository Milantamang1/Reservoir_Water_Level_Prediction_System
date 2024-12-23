from django.urls import include, path
from . import views

urlpatterns = [
     path('',views.dash_index,name='dash_index'),
     path('manage-post/',views.post_manage,name='manage-post'),
     path('post/',views.create_edit_post,name='post'),
     path('post/<int:post_id>/',views.create_edit_post,name='edit-post'),
     path('delete-post/<int:post_id>/',views.delete_post,name='delete-post'),
     path('prediction/',views.prediction,name='prediction'),
     path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
     path('Locate-Us/', views.Locate_Us, name='Locate_Us'),
]



