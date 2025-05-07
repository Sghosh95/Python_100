def turn_right():
    turn_left()
    turn_left()
    turn_left()
#//you will not need this
#    def jump():
#    if wall_in_front():
#        turn_left()
#        while wall_on_right():
#            move()
#        turn_right()
#        move()
#        turn_right()
#        while front_is_clear():
#            move()

#but you will need this, if there is nothing infront the robot 
#keeps on moving , so to eliminate the infinite loop 
#we have to make it hit a wall

while front_is_clear():
    move()
turn_left()

#now it has hit a wall

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
        
    

    