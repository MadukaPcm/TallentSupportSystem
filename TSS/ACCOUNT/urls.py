from django.urls import path
from . import views

#paths for account app.
urlpatterns = [
    path('',views.HomeView, name='home_url'),
    path('contact/',views.ContactView, name="contact_url"),
    path('about/',views.AboutView, name="about_url"),

    path('login/',views.LoginView, name='login_url'),
    path('logout/', views.SignoutView, name='logout_url'),
    path('register/',views.RegisterView, name='register_url'),
    path('registerfunction/',views.RegisterFunctionView, name='RegisterFunction_url'),
    path('forgotpassword/',views.ForgotPasswordView, name="forgotpassword_url"),

    
]