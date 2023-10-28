from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.authentication.urls import urlpatterns as auth_urls
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="A2SvHackathon API",
        default_version="v1",
        description="A2SvHackathon API documentation",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.urls")),
    path("auth/", include(("apps.authentication.urls", "authentication"), namespace="auth")),
    path(
        "docs/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "docs/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path(
            "docs/swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]

# Serve static and media files in development only
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
