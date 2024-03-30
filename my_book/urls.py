

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('kitoblar/', views.kitoblar, name='kitoblar'),
    path('kitob/<slug:kitob_slug>/', views.sotuv, name='sotuv'),
    path('janr/<slug:janr_slug>/', views.janr, name='janr'),
    path('kitoblar/<slug:guruh_slug>/', views.show_group, name='group'),
    path('cat/<slug:cat_slug>/', views.cat, name='cat'),
    path('register/', views.Register, name='category'),
    path('login/', views.Login, name='category'),
    path('yuklash/', views.Yuklash, name='category'),
    path('logout/', views.Logout, name='category'),
    path('send-msg/', views.SendMsg),
]
