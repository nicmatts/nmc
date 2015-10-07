from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views

#from . import views

urlpatterns = [
    # Examples:
    #url(r'^$', 'articles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^panel/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^contact/$', views.contact, name='contact'),
    #url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)