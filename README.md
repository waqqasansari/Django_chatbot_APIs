# Django_chatbot_APIs

This is a Django-based chatbot API project that allows users to interact with a chatbot via API endpoints. Users can send messages to the chatbot, and the chatbot responds with generated text. The project also maintains a chat history.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- **Django Web Framework**: The project is built using Django, a powerful Python web framework.
- **Django REST Framework**: RESTful API endpoints are implemented using Django REST framework.
- **Hugging Face Transformers**: The chatbot logic uses the Hugging Face Transformers library for natural language generation.
- **PostgreSQL Database**: PostgreSQL is used as the database to store chat history.
- **User Interaction**: Users can send messages to the chatbot and receive responses.
- **Chat History**: The project maintains a chat history with timestamps.

## Prerequisites

Before running the project, you need to have the following installed:

- Python 3.x
- Django
- Django REST framework
- PostgreSQL
- Hugging Face Transformers

## Getting Started

1. Clone this repository:

   ```bash
   git clone 'https://github.com/waqqasansari/Django_chatbot_APIs.git'
   ```

   **Configure your database settings in **ChatbotAPI/settings.py**. Use PostgreSQL or your preferred database**

    <!-- ```bash
   cd ChatbotAPI
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ``` -->

   Goto ChatbotAPI folder

   ```bash
   cd ChatbotAPI
   ```

   Install all the required requirements

   ```bash
   pip install -r requirements.txt
   ```

   Run migrations to create the database tables

   ```bash
   python manage.py migrate
   ```

   Start the development server

   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the chat interface at `http://127.0.0.1:8000/api/chat/` in your web browser.
2. Interact with the chatbot by entering messages in the input field.
3. If you are using it first time then it will download **microsoft/DialoGPT-large** pre-trained model.
4. Access the chat history at `http://127.0.0.1:8000/api/chat/`

## API Endpoints

- `/api/chat/`: POST endpoint for sending messages to the chatbot.
- `/api/chat/history/`: GET endpoint to retrieve chat history from the database.
