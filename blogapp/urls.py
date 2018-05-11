from django.urls import path
from . import views


urlpatterns = [
    path('<int:blog_pk>', views.detail, name='detail'),
    path('category/<int:category_pk>', views.category, name='category'),
]