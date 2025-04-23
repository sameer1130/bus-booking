from enum import Enum


class UserGroup(Enum):
    MASTER_ADMIN = "MASTER ADMIN"
    GROUP_ADMIN = "GROUP_ADMIN"
    CONSUMER = "CONSUMER"

    @classmethod
    def choices(cls):
        return [key.value for key in cls]
