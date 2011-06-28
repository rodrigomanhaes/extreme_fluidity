import new

class StateMachineConfigurator(object):

    def __init__(self, state_machine):
        self.state_machine = state_machine

    def configure(self, objekt):
        machine = self.state_machine
        for transition in machine.__class__._class_transitions.values():
            event_name = transition.event
            def generate_event(name):
                def event(self, *args, **kwargs):
                    getattr(machine, name)(*args, **kwargs)
                return event
            event = generate_event(event_name)
            event.__name__ = event_name
            setattr(objekt, event_name,
                new.instancemethod(event, objekt, objekt.__class__))

        def current_state(self):
            return machine.current_state
        setattr(objekt, 'current_state',
            new.instancemethod(current_state, objekt, objekt.__class__))

    def deconfigure(self, objekt):
        machine = self.state_machine
        for transition in machine.__class__._class_transitions.values():
            try:
                objekt.__delattr__(transition.event)
            except AttributeError:
                pass

