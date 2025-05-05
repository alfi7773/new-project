from django.urls import path
from .views import SignUpView, Login, CustomLogoutView, MainView, ProfileUser
from vmlr import views

urlpatterns = [
    path('main/', MainView.as_view(), name='home'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('buy/<int:id>/', views.buy_paket, name='buy_paket'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', SignUpView.as_view(), name='signup'),
]
