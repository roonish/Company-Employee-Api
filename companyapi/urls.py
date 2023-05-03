from django.contrib import admin
from django.urls import include, path

from companyapi.views import home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_page),
    # 1 when we have initial req, this file runs first, from here it see api/v1 so go into api.urls
    path("api/v1/", include("api.urls")),
]
