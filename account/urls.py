from django.conf.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#re_path(r'^login/$', views.user_login, name = 'login'),
	re_path(r'^login/$', auth_views.LoginView.as_view(template_name='account/registration/login.html'), name='login'),
	re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/registration/logout.html'), name='logout'),
	re_path(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'), name='password_change'),
	re_path(r'^password-change/done$', auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'), name='password_change_done'),
	re_path(r'^$', views.dashboard, name='dashboard'),
	re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'), name='password_reset'),
	re_path(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'), name='password_reset_done'),
	re_path(r'^password-reset/confirm/$', auth_views.PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'), name='password_reset_confirm'),
	re_path(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'), name='password_reset_complete'),
	re_path(r'^register/$', views.register, name='register'),
	re_path(r'^edit/$', views.edit, name='edit'),
	]