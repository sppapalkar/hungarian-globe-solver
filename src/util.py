#imports

# Checks if state 1 and state 2 coordinates are equal 
def is_equals(state1,state2):
    for i in range(0,30):
        if state1[i] != state2[i]:
            return False
    return True

#-----------------------------------------------------------------------------#
#Convert final path notation to actual path
# 1 represents - Equator Clockwise(-)
# 2 represents - Equator Anti Clockwise(+)
# 3 represents - 0-180 Longitude Clockwise(-)
# 4 represents - 0-180 Longitude Anti-Clockwise(+)
# 5 represents - 90-270 Longitude Clockwise(-)
# 6 represents - 90-270 Longitude Anti-Clockwise(+)    
def display_path(moves):
    final_path = "Initial"
    for move in moves:
        if move == 1:
            final_path += ' -> Equator Clockwise(-)'
        elif move == 2:
            final_path += ' -> Equator Anti-Clockwise(+)'
        elif move == 3:
            final_path += ' -> 0-180 Longitude Clockwise(-)'
        elif move == 4:
            final_path += ' -> 0-180 Longitude Anti-Clockwise(+)'
        elif move == 5:
            final_path += ' -> 90-270 Longitude Clockwise(-)'
        elif move == 6:
            final_path += ' -> 90-270 Longitude Anti-Clockwise(+)'
    return final_path

#-----------------------------------------------------------------------------#