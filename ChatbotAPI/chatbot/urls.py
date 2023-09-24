from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.chatbot, name='chatbot'),
    path('api/chat/history/', views.ChatHistoryView.as_view(), name='chat_history'),
]