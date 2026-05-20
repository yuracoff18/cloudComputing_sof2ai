from enum import Enum

class PostStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"