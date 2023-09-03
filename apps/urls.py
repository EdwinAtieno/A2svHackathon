from apps.users.urls import urlpatterns as users_urls
from apps.chat.urls import urlpatterns as chat_urls


urlpatterns = users_urls + chat_urls
