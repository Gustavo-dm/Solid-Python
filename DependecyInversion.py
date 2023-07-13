from abc import ABC, abstractmethod


# Abstraction
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


# Low-level module
class EmailService(NotificationService):
    def send_notification(self, message):
        print("Sending email notification:", message)


# Low-level module
class SMSService(NotificationService):
    def send_notification(self, message):
        print("Sending SMS notification:", message)


# High-level module
class NotificationManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_notification(self, message):
        self.notification_service.send_notification(message)
