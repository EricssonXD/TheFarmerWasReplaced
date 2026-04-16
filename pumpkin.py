from helpers import *


goto(0, 0)
while True:
	pcount = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			water()
			if get_ground_type() == Grounds.Grassland:
				till()
			if get_entity_type() == Entities.Pumpkin and can_harvest():
				pcount = pcount + 1
			else:
				harvest()

			plant(Entities.Pumpkin)
			move(North)
		move(East)
	if pcount == get_world_size() ** 2:
		harvest()
