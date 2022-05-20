from django.urls import path
from . import views

urlpatterns = [
    path('authentication', views.authentication, name="authentication"),
    path('logout', views.logoutUser, name="logout"),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('categories', views.categories, name="categories"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path('edit_profile/<int:pk>', views.edit_profile, name="edit_profile"),
    path('faq', views.faq, name="faq"),
]