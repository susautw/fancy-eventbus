from typing import Callable

from fancy.event_bus import EventPriority, EventExecutor, EventListener
from fancy.event_bus.executor import ExecutorBase


class SubscribeEvent:
    priority: int
    executor: ExecutorBase

    def __init__(self, priority: int = EventPriority.NORMAL, executor: ExecutorBase = EventExecutor.MAIN):
        self.priority = priority
        self.executor = executor

    def __call__(self, method: Callable):
        return EventListener(method, priority=self.priority, executor=self.executor)
