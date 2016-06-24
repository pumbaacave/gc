from django.conf.urls import url
from . import views


app_name = 'showroom'
urlpatterns = [
    # ex:/showroom/
    url(r'^$', views.TopPageView.as_view(), name='toppage'),
]