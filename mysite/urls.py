import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    url(r'^site/(?P<path>.*)$', serve,
	    {'document_root': SITE_ROOT, 'show_indexes': True},
	    name='site_path'
    ),
]
