from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homePage"),
    path('sculpture/', views.sculpture_page, name="sculpturePage"),
    path('painting/', views.painting_page, name="paintingPage"),
    path('painter/', views.painter_page, name="painterPage"),
    path('painterprofile/', views.painter_info, name="painterinfo"),
    path('create_painter/', views.createpainter_form, name="createpainterPage"),
    path('update_painter/<int:pk>/', views.updatePainter, name="updatePage"),
    path('delete_painter/<int:pk>/', views.deletePainter, name="DeletePainter")
    
    


]