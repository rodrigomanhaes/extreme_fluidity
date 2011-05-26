import new

class StateMachineConfigurator(object):

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def configure(self, objekt):
        machine = self.state_machine
        for transition in machine.__class__._class_transitions.values():
            def event(self, *args, **kwargs):
                getattr(machine, transition.event)(*args, **kwargs)
            event.__name__ = transition.event
            setattr(objekt, event.__name__,
                new.instancemethod(event, objekt, objekt.__class__))

