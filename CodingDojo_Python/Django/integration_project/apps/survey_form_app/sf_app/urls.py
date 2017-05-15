from django.conf.urls import url   
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^sf_info$', views.process),
	url(r'^result$', views.result),
	url(r'^go_back$', views.back)
]
