from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # 127.0.0.1:8000/admin/
    path("polls/", include("polls.urls")), # 127.0.0.1:8000/polls/
    # 127.0.0.1:8000/polls/
    path("accounts/",include("accounts.urls")), #127.0.0.1:8000/accounts/
    path("accounts/", include("django.contrib.auth.urls")),
]   

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

