import logging

from faker import Faker
from ollama import chat, ChatResponse


class ChatCreationError(Exception):
    pass


class SendMessageError(Exception):
    pass


class Chat:
    chat = None
    messages = []
    faker = None

    def __init__(self, model="llama3", name=None):
        self.model = model
        self.faker = Faker()
        if name:
            self.name = name
        else:
            self.name = self.faker.name()
        self.create_chat()

    def create_chat(self):
        try:
            self.chat = chat(self.model)
        except Exception as e:
            logging.error(f"Failed to create chat with model {self.model}: {e}")
            raise ChatCreationError(f"Failed to create chat with model {self.model}")

    def send_message(self, role="user", message=""):
        try:
            self.messages.append(
                {'role': role, 'content': message}
            )
            response: ChatResponse = chat(
                model=self.model,
                messages=self.messages
            )
            logging.info(f"Message sent successfully: {response}")
            self.messages.append(
                { "role": response.message.role, "content": response.message.content }
            )
            return response.message.content
        except Exception as e:
            raise SendMessageError(f"Failed to send message: {e}")
