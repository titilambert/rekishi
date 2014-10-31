from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('rekishi',
    # Examples:
    # url(r'^$', 'rekishi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'/api/v1/', include('rekishi.api.urls')),
    url(r'/builder/', include('rekishi.builder.urls')),
)

