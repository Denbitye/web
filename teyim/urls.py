from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery2/', views.gallery2, name='gallery2'),
    path('gallery3/', views.gallery3, name='gallery3'),
    path('street/', views.street, name='street'),
    path('still/', views.still, name='still'),
    path('nature/', views.nature, name='nature'),
    path('portrait/', views.portrait, name='portrait'),
    path('about/', views.about, name='about'),
    path('contribute/', views.contribute, name='contribute'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^login/$', views.login_view, name="login"),
    re_path(r'^logout/$', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),

        
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)