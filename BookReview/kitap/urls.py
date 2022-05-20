from django.urls import path, include
from . import views

urlpatterns = [
    path('authentication', views.authentication, name="authentication"), 
    path('logout', views.logoutUser, name="logout"), 
    path('', views.index, name="index"), 
    path('about', views.about, name="about"),
    path('categories/', views.categories, name="categories"),
    path('profile', views.profile, name="profile"),
    path('faq', views.faq, name="faq"),
    path('categories/<slug:category_slug>', views.bookByCategory, name='bookByCategory'),
    path('book/<slug:book_slug>/',views.viewBook, name='book'),
]