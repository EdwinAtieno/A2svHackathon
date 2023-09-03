from apps.users.urls import urlpatterns as users_urls
from apps.authentication.urls import urlpatterns as auth_urls

urlpatterns = users_urls + auth_urls