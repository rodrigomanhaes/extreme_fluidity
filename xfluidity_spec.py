import unittest
from should_dsl import should
from fluidity import StateMachine, state, transition
from fluidity import InvalidTransition, GuardNotSatisfied
from xfluidity import StateMachineConfigurator

class Door(StateMachine):
    state('closed')
    state('open')
    state('broken')
    initial_state = 'closed'
    transition(from_='closed', event='open', to='open', guard='unlocked')
    transition(from_='closed', event='crack', to='broken')
    transition(from_='open', event='close', to='closed')

    def __init__(self, locked=False):
        StateMachine.__init__(self)
        self.locked = locked

    def unlocked(self):
        return not self.locked


class DoorWannabe(object):
    pass


class StateMachineConfiguratorSpec(unittest.TestCase):

    def setUp(self):
        self.door_wannabe = DoorWannabe()
        self.door = door = Door()
        configurator = StateMachineConfigurator(door)
        configurator.configure(self.door_wannabe)

    def it_makes_any_object_respond_to_state_machine_events(self):
        self.door_wannabe |should| respond_to('open')
        self.door_wannabe |should| respond_to('crack')
        self.door_wannabe |should| respond_to('close')

    def it_makes_any_object_change_its_state_like_a_state_machine(self):
        self.door_wannabe.open()
        self.door_wannabe.current_state() |should| equal_to('open')
        self.door_wannabe.crack |should| throw(InvalidTransition)
        self.door_wannabe.close()
        self.door_wannabe.current_state() |should| equal_to('closed')

    def it_makes_any_object_run_guard_when_an_event_occurs(self):
        self.door.locked = True
        self.door_wannabe.open |should| throw(GuardNotSatisfied)

