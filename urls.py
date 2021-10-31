from django.conf.urls import url

from plugins.mailchimp import views


urlpatterns = [
    url(r'^manager/$', views.manager, name='mailchimp_manager'),
    url(r'^signup/$', views.signup, name='mailchimp_add_contact'),
]
