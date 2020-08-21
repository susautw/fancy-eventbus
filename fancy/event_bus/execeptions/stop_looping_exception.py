from fancy.event_bus.execeptions import FancyEventBusException


class StopLoopingException(FancyEventBusException):
    def should_shutdown_immediately(self) -> bool:
        return True
