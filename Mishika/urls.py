"""
Project-level URL configuration.
App-specific routes live inside each app's own urls.py.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("", include("core.urls")),
    path("todo/", include("todo.urls")),

    # REST API — used by the future Telegram bot and any other client
    path("api/", include("Mishika.api_urls")),
    path("api-auth/", include("rest_framework.urls")),  # lets you log in/out of the browsable API
]

# Serve uploaded files (task attachments etc.) during development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)