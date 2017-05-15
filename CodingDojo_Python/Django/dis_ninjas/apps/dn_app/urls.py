from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninjas$', views.four_ninjas),
	url(r'^ninjas/(?P<id>\S+)$', views.colored_ninja)
]
