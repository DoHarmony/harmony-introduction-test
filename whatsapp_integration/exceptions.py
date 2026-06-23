class WhatsAppError(Exception):
    """Base exception for all WhatsApp integration errors."""


class MessageSendError(WhatsAppError):
    """Raised when a message cannot be delivered to the API."""


class AuthenticationError(WhatsAppError):
    """Raised when the API token is invalid or expired."""


class RateLimitError(WhatsAppError):
    """Raised when the API rate limit is exceeded."""


class ContactNotFoundError(WhatsAppError):
    """Raised when the target phone number is not registered on WhatsApp."""
