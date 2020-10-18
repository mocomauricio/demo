from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import IndexView, CardsView, ChartsView, TablesView, NavbarView


urlpatterns = [
    # Todo el sistema de autenticación con las vistas genéricas que ya provee Django
    # para más información: https://docs.djangoproject.com/en/3.1/topics/auth/default/
    url('login/', auth_views.LoginView.as_view(template_name='registro/login.html', redirect_authenticated_user=True), name="login"),
    url('logout/', auth_views.LogoutView.as_view(), name="logout"),
    url('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'), name='password_change_done'),
    url('password_change/', auth_views.PasswordChangeView.as_view(template_name='registro/password_change.html'), name='password_change'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'), name='password_reset_confirm'),
    url('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'), name='password_reset_done'),
    url('password_reset/', auth_views.PasswordResetView.as_view(template_name='registro/password_reset.html'), name='password_reset'),    
    url('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'), name='password_reset_complete'),


    #templates de ejemplo
    url('cards/', CardsView.as_view(), name="cards"),
    url('charts/', ChartsView.as_view(), name="charts"),
    url('tables/', TablesView.as_view(), name="tables"),
    url('navbar/', NavbarView.as_view(), name="navbar"),

    # La template del Dashboard 
    url('', IndexView.as_view(), name="index"),

]
