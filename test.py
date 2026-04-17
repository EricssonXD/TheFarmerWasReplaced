from planting import *
from helpers import *
from maze import pmaze
clear()

goto(0,0)
def dronefunction():
	init_x = get_pos_x()
	init_y = get_pos_y()

	wait_harvest = 0
	while wait_harvest < 5:
		if can_harvest():
			harvest()
			wait_harvest += 1

	while True:
		goto(init_x, init_y)
		pmaze(5)

for i in [[2,2], [7,2], [12,2], [2,7], [7,7], [12,7], [2,12], [7,12], [12,12]]:
	goto(i[0], i[1])
	if not spawn_drone(dronefunction):
		dronefunction()