from fancy.event_bus import EventListener
from fancy.event_bus.scheduler import MultilevelFeedbackQueueScheduler, SchedulerBase


class EventScheduler:
    MULTILEVEL_FEEDBACK_QUEUE: SchedulerBase[EventListener] = MultilevelFeedbackQueueScheduler()
