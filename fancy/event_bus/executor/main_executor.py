from fancy.event_bus import EventListener
from fancy.event_bus.executor import ExecutorBase


class MainExecutorBase(ExecutorBase):
    def execute(self, event_listener: EventListener) -> bool:
        return event_listener(event_listener.event)
