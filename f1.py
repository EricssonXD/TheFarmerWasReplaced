from helpers import *
from planting import *
goto(6,6)
change_hat(Hats.Traffic_Cone)
do_a_flip()
clear()

def dfunction():
	goto(6,6)
	psunflower(3,4,100000000)
# spawn_drone(dfunction)
set_world_size(5)
polyculture()
