from django.contrib import admin
from django.urls import include, path
from linkary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),

    path('', views.LinkListView.as_view(), name='index'),
    path('link/<int:pk>/', views.LinkDetailView.as_view(), name='link_detail'),
    path('link/new/', views.LinkCreateView.as_view(), name='link_create'),
    path('link/<int:pk>/edit/', views.LinkUpdateView.as_view(), name='link_edit'),
    path('link/<int:pk>/delete/', views.LinkDeleteView.as_view(), name='link_delete'),

    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag/new/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_edit'),
]
