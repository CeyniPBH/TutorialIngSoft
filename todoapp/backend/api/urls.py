from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view(), name='list'),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view(), name='detail'),
    path('todos/<int:pk>/complete/', views.TodoToggleCompleteSerializer.as_view(), name='complete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]