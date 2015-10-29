from django.conf.urls import patterns, include, url

from .views import ProxEndView

urlpatterns = patterns(
    '',
    url(r'^$', ProxEndView.as_view()),
)
