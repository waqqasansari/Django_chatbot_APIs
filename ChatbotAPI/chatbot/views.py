from django.shortcuts import render
from rest_framework import generics, status
from django.http import JsonResponse
from .chatbot_logic import Chatbot
from .models import ChatMessage
from .serializers import ChatMessageSerializer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        chatbot = Chatbot()  # Create an instance of your chatbot logic
        response = chatbot.generate_response(message)

        # Save user message and chatbot response to the database
        ChatMessage.objects.create(user_message=message, chatbot_response=response)  # Django model that represents a table named "yourapp_modelclassname" = "chatbot_chatmessage"

        return JsonResponse({'message':message, 'response': response})
    return render(request, 'chatbot.html')

class ChatHistoryView(generics.ListAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer