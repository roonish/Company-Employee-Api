from django.urls import include, path
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

# make router helps to register viewset from route
router = routers.DefaultRouter()
# 3 Comppany urls can be found from routers int CompanyViewSet. Company view set contain create, read, update all feature
router.register(r"companies", CompanyViewSet)
router.register(r"employees", EmployeeViewSet)


urlpatterns = [
    # 2 here in / blank , we get all router.urls.
    path("", include(router.urls))
]
