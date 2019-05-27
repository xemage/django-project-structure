from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.misc.hello_universe_urls')),
    path('', include('apps.users.urls.auth')),
    path('admin/', admin.site.urls),
]

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)), )
