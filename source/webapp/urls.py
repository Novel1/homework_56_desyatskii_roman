from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inform/<int:pk>', views.product_view, name='product_view'),
    path('add/', views.add_view, name='add_view'),
    path('inform/<int:pk>/update/', views.update_view, name='update_view'),
    path('inform/<int:pk>/delete/', views.delete_view, name='delete_view'),
    path('inform/<int:pk>/confirm_dalete/', views.confirm_delete, name='confirm_delete')
    ]