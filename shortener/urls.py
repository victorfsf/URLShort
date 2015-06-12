from django.conf.urls import patterns, include, url

from shortener.views import StoreURL, GenerateURL, RedirectURL

urlpatterns = [
    url('^$', StoreURL.as_view(), name='index'),
    url('^success/', GenerateURL.as_view(), name='success'),
    url('^l/(?P<short_id>[a-zA-Z0-9-]+)', RedirectURL.as_view(), name='redirect'),
]