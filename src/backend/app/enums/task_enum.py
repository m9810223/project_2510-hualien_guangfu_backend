from enum import IntEnum
from enum import StrEnum
from enum import unique


@unique
class TaskType(StrEnum):
    excavation = '鏟土'
    transportation = '搬運'


@unique
class TaskStatus(StrEnum):
    preparing = '準備中'
    working = '工作中'
    done = '已完成'


@unique
class TaskUrgency(IntEnum):
    low = 10
    medium = 20
    high = 30


@unique
class TaskDangerLevel(IntEnum):
    normal = 10
    medium = 20
    dangerous = 30


@unique
class TaskClaimStatus(StrEnum):
    claimed = 'claimed'
    started = 'started'
    completed = 'completed'
    cancelled = 'cancelled'
