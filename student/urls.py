from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:student_id>/', views.detail, name='detail'),
    path('detail/<int:student_id>/update/', views.update, name='update'),
    path('detail/<int:student_id>/delete/', views.delete, name='delete'),
    path('detail/<int:student_id>/score/add', views.add_score, name='add_score'),
    path('score/delete/<int:score_id>', views.delete_score, name="delete_score"),
]
