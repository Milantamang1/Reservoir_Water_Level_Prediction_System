from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.water_level_prediction_view, name='predict_water_level'),
    path('', views.render_form, name='render_form'),
]
