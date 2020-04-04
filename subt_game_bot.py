class NimGame:
  
    def __init__(self, n):
      
        self.n = n

    def startState(self):
        return self.n

    def isEnd(self, state):
        return True if state == 0 else False

    def utility(self, state, player):
      
        if state == 0:
            if player == 1:
                return float('-inf')
            else:
                return float('+inf')

    def actions(self, state):
        if state >= 3:
            return [1,2,3]
        return range(1, state+1)

    def successor(self, state, action):
      
        if action > state:
            return 0
        return state - action


def minimaxPolicy(game, state, player):
   
    def recurse(state, player):
       
        if game.isEnd(state) == True:
            return (game.utility(state, player), None)
        if cache.has_key((state, player)):
            return cache[(state, player)]

               choices = [(recurse(game.successor(state, action), -1*player)[0], action) for action in game.actions(state)]

       
        if player == +1:
            val = max(choices)
        else:
            val = min(choices)
        cache[(state, player)] = val
        return val

    
    value, action = recurse(state, player)
    return (value, action)

cache = {}

if __name__ == "__main__":
    game = NimGame(18)

    state = game.startState()
    while (state > 0):
        turn = 1
        print "current state is", state
        if turn == 1 :
               val1, act1 = minimaxPolicy(game, state, 1)
               state -= act1
               turn = -1;
               print "computer1 moves state to", state

        if state == 0:
           print "computer1 won!"
           break
        print "current state is", state
        if turn == -1 :
            val2, act2 = minimaxPolicy(game, state, 1)
            state -= act2
            turn = 1;
            print "computer2 moves state to", state
        if state == 0:
           print "computer2 won!"
