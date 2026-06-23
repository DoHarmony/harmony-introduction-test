from abc import ABC, abstractmethod
from typing import List, Optional

from .models import Contact, Conversation, Message, MessageStatus


class MessageSender(ABC):
    """Defines the contract for sending messages through any channel."""

    @abstractmethod
    def send_message(self, message: Message) -> MessageStatus:
        """Send a single message and return its final delivery status."""
        ...

    @abstractmethod
    def send_bulk(self, messages: List[Message]) -> List[MessageStatus]:
        """Send multiple messages and return a status for each one."""
        ...


class MessageReceiver(ABC):
    """Defines the contract for receiving and processing inbound messages."""

    @abstractmethod
    def receive_message(self, raw_payload: dict) -> Message:
        """Parse a raw inbound webhook payload into a Message object."""
        ...

    @abstractmethod
    def handle_status_update(self, raw_payload: dict) -> MessageStatus:
        """Parse a delivery/read-receipt webhook and return the updated status."""
        ...


class MessageStorage(ABC):
    """Defines the contract for persisting conversations and messages."""

    @abstractmethod
    def save_message(self, message: Message) -> None:
        """Persist a single message."""
        ...

    @abstractmethod
    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Retrieve a full conversation by its identifier."""
        ...

    @abstractmethod
    def get_messages_by_contact(self, phone_number: str) -> List[Message]:
        """Retrieve all messages exchanged with a given contact."""
        ...

    @abstractmethod
    def update_message_status(self, message_id: str, status: MessageStatus) -> None:
        """Update the delivery status of an existing message."""
        ...
