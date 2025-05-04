from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from .models import Pakets


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('profile')
    
    # def get_success_url(self):
    #     return '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.get_form()  
        return context
    
    

class CustomLogoutView(LogoutView):
    next_page = '/' 
 

class MainView(ListView):
    template_name = 'index.html'
    queryset = Pakets.objects.all()
    context_object_name = 'pakets'


# class ProfileUser(LoginRequiredMixin, View):
#     template_name = 'profile/profile.html'
#     model = User
#     form_class = UserUpdateForm
#     success_url = reverse_lazy('home')

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['user'] = self.request.user
#     #     context['user_form'] = self.form_class(instance=self.request.user)
#     #     context['password_form'] = PasswordChangeForm(self.request.user)
#     #     return context
    
#     def get(self, request, *args, **kwargs):
#         user_form = self.form_class(instance=request.user)
#         password_form = PasswordChangeForm(request.user)
#         context = {
#             'user_form': user_form,
#             'password_form': password_form
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         user_form = self.form_class(request.POST, instance=request.user)
#         password_form = PasswordChangeForm(request.user, request.POST)
        
#         if 'user_form' in request.POST:
#             if user_form.is_valid():
#                 user_form.save()
#                 return redirect('profile')
#         elif 'password_form' in request.POST:
#             if password_form.is_valid():
#                 password_form.save()
#                 update_session_auth_hash(request, password_form.user) 
#                 return redirect('profile')
        
#         context = {
#             'user_form': user_form,
#             'password_form': password_form
#         }
        
#         return render(request, self.template_name, context)


    

# Create your views here.
