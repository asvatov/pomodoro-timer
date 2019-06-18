from copy import copy

FSM_STATE_IDLE = 0
FSM_STATE_RUN = 1
FSM_STATE_BREAK = -1
FSM_STATE_LONG_BREAK = -2
FSM_STATE_PAUSED = -3
FSM_STATE_CONTINUE = -4

EVENT_START = "StartEvent"
EVENT_PAUSE = "PauseEvent"
EVENT_RESET = "ResetEvent"
EVENT_START_BREAK = "StartBreakEvent"
EVENT_CONTINUE = "ContinueEvent"


class State(object):
    state_code = None
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self, session):
        self.session = session

    def run(self):
        pass

    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def copy(self):
        return copy(self)

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__


class IdleState(State):
    """
    The state which indicates that there are limited device capabilities.
    """
    state_code = FSM_STATE_IDLE

    def run(self):
        self.session.set_default_session_params()


class RunState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """
    state_code = FSM_STATE_RUN

    def run(self):
        self.session.start_work_session()
        # self.session.play_sound_work_session_started()
        # self.session.get_notification_work_session_started().show()


class PauseState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """
    state_code = FSM_STATE_PAUSED

    def run(self):
        self.session.pause_session()


class BreakState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """
    state_code = FSM_STATE_BREAK

    def run(self):
        self.session.start_break_session()
        # self.session.play_sound_break_session_started()
        # self.session.get_notification_break_session_started().show()


class ContinueState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """
    state_code = FSM_STATE_CONTINUE

    def run(self):
        pass


class Event:
    _name = None

    def __init__(self):
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.get_name()

    def get_name(self):
        return self._name


class StartEvent(Event):
    _name = EVENT_START


class PauseEvent(Event):
    _name = EVENT_PAUSE


class ResetEvent(Event):
    _name = EVENT_RESET


class StartBreakEvent(Event):
    _name = EVENT_START_BREAK


class ContinueEvent(Event):
    _name = EVENT_CONTINUE


GRAPH = {
    (FSM_STATE_IDLE, EVENT_START): RunState,
    (FSM_STATE_RUN, EVENT_PAUSE): PauseState,
    (FSM_STATE_RUN, EVENT_RESET): IdleState,
    (FSM_STATE_RUN, EVENT_START_BREAK): BreakState,
    (FSM_STATE_BREAK, EVENT_START): RunState,
    (FSM_STATE_BREAK, EVENT_PAUSE): PauseState,
    (FSM_STATE_BREAK, EVENT_RESET): IdleState,
    (FSM_STATE_PAUSED, EVENT_START): RunState,
    (FSM_STATE_PAUSED, EVENT_RESET): IdleState,
    (FSM_STATE_PAUSED, EVENT_START_BREAK): BreakState,
    (FSM_STATE_PAUSED, EVENT_CONTINUE): ContinueState
}


class TimerFSM(object):
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """
    init_state_class = IdleState

    def __init__(self, session):
        """ Initialize the components. """

        self.session = session

        # Start with a default state.
        self.run_state(self.init_state_class)

    def get_state_code(self):
        return self.state.state_code

    def get_prev_state_code(self):
        return self.prev_state.state_code

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        prev_state = self.state.copy()
        state_class = GRAPH.get((self.state.state_code, event.get_name()), None)
        if state_class is None:
            self.state = prev_state
        elif prev_state.state_code == state_class.state_code:
            return
        elif state_class == ContinueState:
            self.run_state(self.prev_state.__class__)
        else:
            self.run_state(state_class)

    def run_state(self, state_class):
        if "state" in dir(self):
            self.prev_state = self.state.copy()
        else:
            self.prev_state = self.init_state_class(self.session)

        self.state = state_class(self.session)
        self.state.run()
