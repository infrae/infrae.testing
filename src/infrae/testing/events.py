
from zope.component import getGlobalSiteManager
from zope.component.eventtesting import clearEvents as clear_events
from zope.component.eventtesting import getEvents as get_events


def get_event_names():
    """Return the names of the triggered events.
    """
    called = map(lambda e: e.__class__.__name__, get_events())
    clear_events()
    return called



class assertTriggersEvents(object):
    """Context manager that check that some events are triggered.
    """

    def __init__(self, *names, **opts):
        self.names = names
        self.msg = opts.get('msg')
        self.triggered = []

    def __enter__(self):
        getGlobalSiteManager().registerHandler(
            self.triggered.append, (None,))

    def __exit__(self, exc_type, exc_val, exc_tb):
        getGlobalSiteManager().unregisterHandler(
            self.triggered.append, (None,))
        if exc_type is None and exc_val is None and exc_tb is None:
            self.verify(map(lambda e: e.__class__.__name__,  self.triggered))

    def verify(self, triggered):
        for name in self.names:
            msg = self.msg
            if msg is None:
                msg = "block didn't trigger event %s, got %s" % (
                    name, ', '.join(triggered))
            assert name in triggered, msg


class assertNotTriggersEvents(assertTriggersEvents):
    """Context manager that check that events are not triggered.
    """

    def verify(self, triggered):
        for name in self.names:
            msg = self.msg
            if msg is None:
                msg = "block triggered event %s, got %s" % (
                    name, ', '.join(triggered))
            assert name not in triggered, msg
