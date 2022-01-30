
from django.contrib import admin
from django.urls import path, include
from todolist import views as todolistViews

urlpatterns = [
    path('', todolistViews.index, name='index_page'),
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),
    path('accounts/', include('users_app.urls')),
    path('contact/', todolistViews.contact, name = 'contact_page'),
    path('about/', todolistViews.about, name = 'about_page'),
   

]
