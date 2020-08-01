# Imports
import copy

# Determine new coordinates for 1 equator clockwise(-) motion    
def equator_clockwise(current_state):                                         
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 90:
            if cord[1] == 0:
                cord[1] = 330
            else:
                cord[1]-=30
        new_state.append(cord)
    return new_state 

#-----------------------------------------------------------------------------#
# Determine new coordinates for 1 equator anti-clockwise(+) motion
def equator_anticlockwise(current_state):
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 90:
            cord[1] = (cord[1]+30)%360
        new_state.append(cord)
    return new_state 

#-----------------------------------------------------------------------------#
# Determine new coordinates for 1 longitude 0-180 clockwise(-) motion 
def long_0_clockwise(current_state):
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 0 and cord[1] == 0:
            cord[0] = 30
            cord[1] = 180
        elif cord[0] == 180 and cord[1] == 180:
            cord[0] = 150
            cord[1] = 0
        else:
            if cord[1] == 0:
                cord[0] -= 30
            elif cord[1] == 180:
                cord[0] += 30
        new_state.append(cord)
    return new_state 

#-----------------------------------------------------------------------------#
# Determine new coordinates for 1 longitude 0-180 anticlockwise(+) motion 
def long_0_anticlockwise(current_state):
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 150 and cord[1] == 0:
            cord[0] = 180
            cord[1] = 180
        elif cord[0] == 30 and cord[1] == 180:
            cord[0] = 0
            cord[1] = 0
        else:
            if cord[1] == 0:
                cord[0] += 30
            elif cord[1] == 180:
                cord[0] -= 30
        new_state.append(cord)
    return new_state 

#-----------------------------------------------------------------------------#
# Determine new coordinates for 1 longitude 90-270 clockwise(-) motion 
def long_90_clockwise(current_state):
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 0 and cord[1] == 0:
            cord[0] = 30
            cord[1] = 270
        elif cord[0] == 30 and cord[1] == 90:
            cord[0] = 0
            cord[1] = 0
        elif cord[0] == 180 and cord[1] == 180:
            cord[0] = 150
            cord[1] = 90
        elif cord[0] == 150 and cord[1] == 270:
            cord[0] = 180
            cord[1] = 180
        else:
            if cord[1] == 90:
                cord[0] -= 30
            elif cord[1] == 270:
                cord[0] += 30
        new_state.append(cord)
    return new_state

#-----------------------------------------------------------------------------#
# Determine new coordinates for 1 longitude 90-270 clockwise(+) motion 
def long_90_anticlockwise(current_state):
    current_state = copy.deepcopy(current_state)
    new_state = []
    for cord in current_state:
        if cord[0] == 0 and cord[1] == 0:
            cord[0] = 30
            cord[1] = 90
        elif cord[0] == 150 and cord[1] == 90:
            cord[0] = 180
            cord[1] = 180
        elif cord[0] == 180 and cord[1] == 180:
            cord[0] = 150
            cord[1] = 270
        elif cord[0] == 30 and cord[1] == 270:
            cord[0] = 0
            cord[1] = 0
        else:
            if cord[1] == 90:
                cord[0] += 30
            elif cord[1] == 270:
                cord[0] -= 30
        new_state.append(cord)
    return new_state