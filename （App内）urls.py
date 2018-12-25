//App内路由
from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^index/',views.index)
]
