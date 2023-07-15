
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls', )),
    path('accounts/', include('accounts.urls')),
    path('letters/', include('letters.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
]

