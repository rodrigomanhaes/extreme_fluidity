import unittest
from should_dsl import should, should_not
from fluidity import StateMachine, state, transition
from fluidity import InvalidTransition, GuardNotSatisfied
from xfluidity import StateMachineConfigurator

class Door(StateMachine):
    state('closed', enter='exit_light', exit='enter_light')
    state('open')
    state('broken')
    initial_state = 'closed'
    transition(from_='closed', event='open', to='open', guard='unlocked')
    transition(from_='closed', event='crack', to='broken', action='boom')
    transition(from_='open', event='close', to='closed')

    def __init__(self, locked=False):
        StateMachine.__init__(self)
        self.locked = locked
        self.pass_light = False
        self.is_destroyed = False

    def unlocked(self):
        return not self.locked

    def exit_light(self):
        self.pass_light = False

    def enter_light(self):
        self.pass_light = True

    def boom(self):
        self.is_destroyed = True


class DoorWannabe(object):
    pass


class StateMachineConfiguratorSpec(unittest.TestCase):
    '''An object configured by StateMachineConfigurator'''

    def setUp(self):
        self.door_wannabe = DoorWannabe()
        self.door = door = Door()
        configurator = StateMachineConfigurator(door)
        configurator.configure(self.door_wannabe)

    def it_responds_to_state_machine_events(self):
        self.door_wannabe |should| respond_to('open')
        self.door_wannabe |should| respond_to('crack')
        self.door_wannabe |should| respond_to('close')

    def it_changes_its_state_like_according_to_the_templating_machine(self):
        self.door_wannabe.open()
        self.door_wannabe.current_state() |should| equal_to('open')
        self.door_wannabe.crack |should| throw(InvalidTransition)
        self.door_wannabe.close()
        self.door_wannabe.current_state() |should| equal_to('closed')

    def it_runs_guard_when_an_event_occurs(self):
        self.door.locked = True
        self.door_wannabe.open |should| throw(GuardNotSatisfied)

    def it_runs_enter_and_exit_actions_at_state_change(self):
        self.door_wannabe.open()
        self.door.pass_light |should| be(True)
        self.door_wannabe.close()
        self.door.pass_light |should| be(False)

    def it_runs_event_actions(self):
        self.door |should_not| be_destroyed
        self.door_wannabe.crack()
        self.door |should| be_destroyed

