from django.urls import path
from . import views

urlpatterns = [
    path('test', views.Test, name='test'),
    path('login', views.Login_Attempt, name='Login_Attempt'),
    path('register', views.Register_Attempt, name='Register_Attempt'),
    path('authtoken/<auth_token>', views.VerifyAuthToken),
    path('forgetpass/', views.Forget_Pass_Attempt, name="Forget_Pass_Attempt"),
    path('resetokenpass/<forget_token>', views.VerifyPasswordToken, name="Verify_Password_Token"),

    
    
    

    
]
