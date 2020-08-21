from threading import Thread

from fancy.event_bus import EventListener
from fancy.event_bus.executor import ExecutorBase


class ThreadExecutorBase(ExecutorBase):
    def execute(self, event_listener: EventListener) -> bool:
        Thread(target=event_listener, args=(event_listener.event,), daemon=True).start()
        return True
