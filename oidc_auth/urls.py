from django.conf.urls import patterns, url


urlpatterns = patterns('oidc_auth.views',
    url(r'^login/$', 'login_begin', name='oidc-login'),
    url(r'^complete/$', 'login_complete', name='oidc-complete'),
)
