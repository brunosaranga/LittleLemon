from django.urls import path, include
from rest_framework import routers
# from .views import MenuView, BookingView, UserViewSet
from .views import UserViewSet, BookingViewSet, MenuItemsView, SingleMenuItemView, home, about

from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name="about"),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),

    path('menu-items/', MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view()),
]

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('about/', views.about, name="about"),
#     path('book/', views.book, name="book"),
#     path('menu/', views.menu, name="menu"),
#     path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
#     path('bookings/', views.bookings, name="bookings"),
# ]