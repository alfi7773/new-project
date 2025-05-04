from django.urls import path
from .views import SignUpView, Login, CustomLogoutView, MainView
from vmlr import views

urlpatterns = [
    path('main/', MainView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', SignUpView.as_view(), name='signup'),
]
