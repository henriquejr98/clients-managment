from django.contrib import admin
from django.urls import include, path
from clientes import urls as clientes_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from home import urls as home_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(clientes_urls) ),
    path('' , include(home_urls)),
    path('login/', auth_views.LoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
