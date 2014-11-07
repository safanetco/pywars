# Example responses:
#
# Move to the right:
#   return {'ACTION': 'MOVE', 'WHERE': 1}
#
# Move to the left:
#   return {'ACTION': 'MOVE', 'WHERE': -1}
#
# Shooting projectile:
#   return {'ACTION': 'SHOOT', 'VEL': 100, 'ANGLE': 35}
#   # 'VEL' should be an integer > 0 and < 100
#   # 'ANGLE' should be an integer > 0 and < 90
#
#
# Do nothing:
#   return None

class Bot(object):

    def evaluate_turn(self, arena_array, feedback, life):
        '''
        :param arena_array:  a Python array with players location. Ie:
        arena_array = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0] # (where the number is the player location)
        :param feedback: the result of the previous turn, ie: for the move action 'SUCCESS' is returned when the enemy
            received a hit, or 'FAILED' when missed the shot.
        :param life: Current life level, An integer between between 0-100.
        :return: see the comments above
        '''
        return None