from django.contrib import admin
from django.urls import path
from linkary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LinkListView.as_view(), name='index'),
    path('link/<int:pk>/', views.LinkDetailView.as_view(), name='link_detail'),
    path('link/new/', views.LinkCreateView.as_view(), name='link_create'),
]
