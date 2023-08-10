from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



# swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="Push Notification Microservice API",
        default_version='v1',
        description="API to send push notifications to the users for their gas readings!",
        #terms_of_service="https://www.yourapp.com/terms/",
        #contact=openapi.Contact(email="contact@homefortenergy.com"),
        #license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ms/api/v1/', include("core.urls")),

    re_path(r'^ms/api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('ms/api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

