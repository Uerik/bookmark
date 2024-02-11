from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_new_item, name='addNew'),
    path('delete<int:id>', views.delete_item, name='delete_item'),
    path('update<int:id>', views.update_item, name='update_item'),
]
