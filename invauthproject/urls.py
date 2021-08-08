
from django.contrib import admin
from django.urls import path, include,re_path # added the include keyword
from company import views 
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView # new line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/company/', include('company.urls')), # new line
    path(('users/'), include('users.urls')),
    
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
