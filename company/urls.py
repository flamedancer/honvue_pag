from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^games$', views.games, name='games'),
    url(r'^news$', views.news, name='news'),
    url(r'^business$', views.business, name='business'),
    url(r'^joinUs$', views.joinUs, name='joinUs'),
    url(r'^aboutUs$', views.aboutUs, name='aboutUs'),
    url(r'^gameDetail$', views.gameDetail, name='gameDetail'),
]
