from .views import ImageProcessView
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Создайте представление схемы с пользовательскими настройками.

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Описание вашего API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="License Name"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('process-image/', ImageProcessView.as_view(), name='process_image'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


