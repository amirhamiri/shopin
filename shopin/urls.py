from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls"))
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=True,
)
