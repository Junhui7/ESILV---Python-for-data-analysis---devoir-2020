
from django.urls import path

from junhui import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predict', views.predict, name="predict"),
    path('resultat', views.resultat, name="resultat"),
    path('resultat_hyper', views.hyper_score, name="resultat_hyper"),
    path('hyper_parameter', views.hyper_parameter, name="hyper_parameter")

]
