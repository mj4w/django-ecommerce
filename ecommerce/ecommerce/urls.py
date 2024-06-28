from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from ecommerce.product import views

from .sentry import trigger_error

router = DefaultRouter()
router.register(r"category", views.CategoryView)
router.register(r"brand", views.BrandView)
router.register(r"product", views.ProductView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("sentry-bug/", trigger_error),
]
