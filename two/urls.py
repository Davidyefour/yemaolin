from two import views
from  django.conf.urls import url

urlpatterns = [
    url(r'^index',views.index),
    url(r'^add',views.add),
    url(r'^show',views.show),
    url(r'^update',views.update),
    url(r'search',views.search),
    url(r'respond',views.respond),

    url(r'form_post',views.form_post),
    url(r'post', views.post),
    url(r'demo',views.demo)
 ]