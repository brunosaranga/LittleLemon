from django.urls import path, include
from rest_framework import routers
# from .views import MenuView, BookingView, UserViewSet
from .views import UserViewSet, BookingViewSet, MenuItemsView, SingleMenuItemView

from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),

    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view()),
]