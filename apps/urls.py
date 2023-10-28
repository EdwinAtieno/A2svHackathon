<<<<<<< HEAD
from apps.users.urls import urlpatterns as users_urls
from apps.authentication.urls import urlpatterns as auth_urls
from apps.chat.urls import urlpatterns as chat_urls

urlpatterns = users_urls + auth_urls + chat_urls
=======
from apps.users.urls import urlpatterns as users_urls
# from apps.chat.urls import urlpatterns as chat_urls
from apps.profiles.urls import urlpatterns as profiles_urls
from apps.authentication.urls import urlpatterns as auth_urls

urlpatterns = users_urls + auth_urls + profiles_urls
>>>>>>> 75c18a1 (feat profiles)
