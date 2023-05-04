from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),

    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('exit', views.exit_user, name='exit'),


    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

