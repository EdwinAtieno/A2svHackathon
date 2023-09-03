from apps.users.urls import urlpatterns as users_urls
# from apps.chat.urls import urlpatterns as chat_urls


urlpatterns = users_urls # + chat_urls

from apps.authentication.urls import urlpatterns as auth_urls

urlpatterns = users_urls + auth_urls # + chat_urls
