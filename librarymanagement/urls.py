"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),
    path('Clientclick', views.Clientclick_view),


    path('adminsignup', views.adminsignup_view),
    path('addClient', views.addClient_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('Clientlogin', LoginView.as_view(template_name='library/Clientlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),
    path('client<int:pk>delete', views.ClientDelete, name='Client_delete'),
    path('client<int:pk>Update', views.ClientUpdate, name='Client_update'),

    path('clientupdateby',views.ClientUpdatebyClient,name='Client_updateb'),
    #path('client<int:pk>Update', views.ClientUpdatee, name='Client_updatee'),


    path('addbook', views.addbook_view),
    path('book<int:pk>update', views.BookUpdate, name='book_update'),
    path('book<int:pk>delete', views.BookDelete, name='book_delete'),
    path('book<int:pk>Return', views.Return, name='Return'),
    #path('book<int:pk>return', views.Bookreturn, name='book_return'),
    path('viewBookbyClient', views.viewbookbyClient_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewClient', views.viewClient_view),
    path('viewissuedbookbyClient', views.viewissuedbookbyClient),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    path('search_b', views.search_b, name="search_b"),
    path('search_c', views.search_c, name="search_c"),
    path('search_bby', views.search_bby, name="search_bby")
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
