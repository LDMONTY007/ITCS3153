class SimpleReflexAgent:
    # why does this method exist only to
    # take in a dictionary and give us
    # the exact same dictionary?
    # or am I supposed to have 3 params
    # here that are used to init the
    # dictionary? This just feels
    # redundant because I could
    # just declare the dictionary?
    # should I be calling decide in percieve?
    # I doubt that because they make me return
    # the state.
    # redundant method is redundant.
    def percieve(cleanliness, obstacle, occupied):
        # dictionary decleration.
        state = {'cleanliness': cleanliness, 'obstacle': obstacle, 'occupied': occupied}
        return state

    def decide_state(state):
        # do if else and figure out what
        # to do based on state.
        # 'clean': Clean the room.
        # 'avoid_obstacle': Avoid an obstacle.
        # 'wait': Wait for the room to be unoccupied.
        # 'move_to_next_room': Move to the next room.
        if state['cleanliness'] == 'dirty':
            perform_action('clean')
        if state['obstacle'] == 'True':
            perform_action('avoid_obstacle')
        if state['occupied'] == 'True':
            perform_action('wait')
        if state['cleanliness'] == 'clean' and state['obstacle'] == 'False' and state['occupied'] == 'False':
            perform_action('move_to_next_room')

    def perform_action(action):
        if action == 'clean':
            print('cleaned')
        elif action == 'avoid_obstacle':
            print('avoided obstacle')
        elif action == 'wait':
            print('waited')
        elif action == 'move_to_next_room':
            print('moved to next room')
            # probably prompt the user for the new
            # room info then call "percieve room"

    pass

class ModelBasedReflexAgent:

    # why does this method exist only to
    # take in a dictionary and give us
    # the exact same dictionary?
    # or am I supposed to have 3 params
    # here that are used to init the
    # dictionary? This just feels
    # redundant because I could
    # just declare the dictionary?
    # should I be calling decide in percieve?
    # I doubt that because they make me return
    # the state.
    # redundant method is redundant.
    def percieve(cleanliness, obstacle, occupied):
        # dictionary decleration.
        state = {'cleanliness': cleanliness, 'obstacle': obstacle, 'occupied': occupied}
        # add state to the history.
        history.append(state)
        return state



    def decide_state(state):
        shouldReturn = False

        for i in range(0, len(history) - 1):
            if history[i] == state:
                for key in action_history[i]:
                    # perform each action in the dictionary at
                    # i if it is the same as our current input
                    # and we have already done those actions
                    # before.
                    shouldReturn = True
                    perform_action(action_history[i][key])

        #if we used the model to
        #get our output then don't
        #do another caclulation.
        if (shouldReturn):
            return

        # declare dictionary
        actions = {}

        # do if else and figure out what
        # to do based on state.
        # 'clean': Clean the room.
        # 'avoid_obstacle': Avoid an obstacle.
        # 'wait': Wait for the room to be unoccupied.
        # 'move_to_next_room': Move to the next room.
        if state['cleanliness'] == 'dirty':
            perform_action('clean')
            # add action to actions.
            actions['cleanliness'] = 'clean'
        if state['obstacle'] == 'True':
            perform_action('avoid_obstacle')
            actions['obstacle'] = 'avoid_obstacle'
        if state['occupied'] == 'True':
            perform_action('wait')
            actions['occupied'] = 'wait'
        if state['cleanliness'] == 'clean' and state['obstacle'] == 'False' and state['occupied'] == 'False':
            perform_action('move_to_next_room')
            actions['move'] = 'move_to_next_room'

        # we don't actually care what the key is,
        # because we iterate over them anyway.
        action_history.append(actions)

def perform_action(action):
        if action == 'clean':
            print('cleaned')
        elif action == 'avoid_obstacle':
            print('avoided obstacle')
        elif action == 'wait':
            print('waited')
        elif action == 'move_to_next_room':
            print('moved to next room')
            # probably prompt the user for the new
            # room info then call "percieve room"

    # list of states for our history.
history = []
action_history = []

def __init__(self):
    #init.

    pass


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    #issues I have with this assignment:
    #1. I am not told to do anything other than
    #2. to use the methods and print the state
    # decided.
    #3. Am I supposed to edit the state to
    # match the decisions I make?
    # you don't tell me that if so.
    # Like, as in recursively update it's
    # state until we have reached the point
    # where we call perform_action('move_to_next_room')?
    # guidance would be appreciated, I'll have to send
    # an email.
if __name__ == '__main__':
    # state = percieve({'cleanliness': 'dirty', 'obstacle': False, 'occupied': False})
    # decide_state(state)
    #
    # simple_reflex_agent
    state = SimpleReflexAgent.percieve((input("Enter room cleanliness:")), (input("Is there an obstacle? (True/False):")), (input("Is the room occupied? (True/False):")))
    SimpleReflexAgent.decide_state(state)
    #
    # model_based_reflex_agent
    agent = ModelBasedReflexAgent
    state = agent.percieve((input("Enter room cleanliness:")), (input("Is there an obstacle? (True/False):")), (input("Is the room occupied? (True/False):")))
    agent.decide_state(state)

    state = agent.percieve((input("Enter room cleanliness:")), (input("Is there an obstacle? (True/False):")),
                           (input("Is the room occupied? (True/False):")))
    agent.decide_state(state)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/





