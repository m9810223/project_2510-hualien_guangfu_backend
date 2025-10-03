from enum import StrEnum
from enum import unique


@unique
class TaskClaimStatus(StrEnum):
    claimed = 'claimed'
    started = 'started'
    completed = 'completed'
    cancelled = 'cancelled'
