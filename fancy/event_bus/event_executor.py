from fancy.event_bus.executor import MainExecutorBase
from fancy.event_bus.executor.thread_executor import ThreadExecutorBase


class EventExecutor:
    MAIN = MainExecutorBase()
    THREAD = ThreadExecutorBase()
