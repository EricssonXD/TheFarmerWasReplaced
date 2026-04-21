from helpers import *

def tillx(tilled = True):
	if (get_ground_type() == Grounds.Grassland and tilled) or (get_ground_type() == Grounds.Soil and not tilled):
		till()

def harvestx():
	if can_harvest():
		harvest()

def water():
	while get_water() < 0.75:
		use_item(Items.Water)


def auto_plant(plant_type):
	if plant_type == Entities.Carrot:
		pcarrot()

def pcarrot():
	tillx()
	if can_harvest():
		harvest()
	water()
	plant(Entities.Carrot)
	
def ptree():
	tillx()
	if can_harvest():
		harvest()
	if((get_pos_x()+get_pos_y())%2==0):
		plant(Entities.Tree)
		water()


# Size = 6 is the default size for pumpkins, 
# It would plant a megapumpkin of size 6 starting from the lower left corner of the pumpkin
def ppumpkin(size=6):
	
	start_x = get_pos_x()
	start_y = get_pos_y()
 
	def looppmpkin():
		tillx()
		water()
		plant(Entities.Pumpkin)
  
	navigate_farm(looppmpkin, size, size)
	goto(start_x, start_y)

	# Mark the positions of the dead pumpkins so that we can replant them later
	dead_pumpkins = []
	
	def checkPumpkin():
		if get_entity_type() == Entities.Dead_Pumpkin:
			dead_pumpkins.append({"x": get_pos_x(), "y": get_pos_y()})
			plant(Entities.Pumpkin)

	navigate_farm(checkPumpkin, size, size)
 	
	if len(dead_pumpkins) == 0:
		goto(start_x, start_y)
		harvest()
 		
	while len(dead_pumpkins) > 0:
		for pumpkin in dead_pumpkins:
			goto(pumpkin["x"], pumpkin["y"])
			if can_harvest():
				dead_pumpkins.remove(pumpkin)
			elif get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				
	harvest()
	
def psunflower(size_x = 3, size_y = 4, target = 1000):
	plist = []
	def loopsunflower():
		tillx()
		plant(Entities.Sunflower)
		p = measure()
		plist.append({"x": get_pos_x(), "y": get_pos_y(), "p": p})
	
	navigate_farm(loopsunflower, size_x, size_y)

	while num_items(Items.Power) < target:
		maxp = 0
		for flower in plist:
			if flower["p"] > maxp:
				maxp = flower["p"]
				best_flower = flower
		goto(best_flower["x"], best_flower["y"])
		if can_harvest():
			harvest()
		plant(Entities.Sunflower)
		water()
		plist.remove(best_flower)
		plist.append({"x": get_pos_x(), "y": get_pos_y(), "p": measure()})

def pcactus(size_x = 6, size_y = 6):
	init_x = get_pos_x()
	init_y = get_pos_y()

	def loopcactus():
		tillx()
		water()
		plant(Entities.Cactus)
	navigate_farm(loopcactus, size_x, size_y)


	for orientation in range(2):
		# Settings for Row
		current_direction = East
		opposite_direction = West
		array_num = size_y
		array_len = size_x
		if orientation == 1:
			# Settings for Column
			current_direction = North
			opposite_direction = South
			array_num = size_x
			array_len = size_y

		# Sorting for each direction
		for i in range(array_num):
			sorted = False
			if orientation == 0:
				# Sort row first
				goto(init_x, init_y + i)
			else:
				# Then column
				goto(init_x + i, init_y)

			# For each array, we bubble sort
			c_size = measure()
			c_next = measure(current_direction)
			if c_next < c_size: # type: ignore
				swap(current_direction)
			while not sorted:
				# Back and forth through the array until sorted
				for direction in [current_direction, opposite_direction]:
					sorted = True
					for j in range(array_len-2):
						move(direction)
						c_size = measure()
						c_next = measure(current_direction)
						if c_next < c_size: # type: ignore
							swap(current_direction)
							sorted = False 
	harvest()
	goto(init_x, init_y)

def pweird():
	if can_harvest():
		use_item(Items.Weird_Substance)
		harvest()
	tillx(False)
	# plant(Entities.Carrot)
	water()
	rev_direction = {North: South, South: North, East: West, West: East}
	for i in [North, East, South, West]:
		move(i)
		if can_harvest():
			harvest()
		tillx(False)
		# plant(Entities.Tree)
		water()
		move(rev_direction[i])

def wait_for_harvest():
	while not can_harvest():
		continue
	harvest()

def polyculture():
	plant(Entities.Grass)
	last_planted_x = get_pos_x()
	last_planted_y = get_pos_y()
	companion = get_companion()
	ccord_x = 0
	ccord_y = 0
	if companion != None:
		ctype, (ccord_x, ccord_y) = companion
		goto(ccord_x,  ccord_y)
		tillx()
		plant(ctype)
		water()

	while True:
		# Get the current plant's companion
		companion = get_companion()
		if companion != None:
			# Go to the previous plant and harvest it (The current plant should be it's companion)
			goto(last_planted_x, last_planted_y)
			last_planted_x = ccord_x
			last_planted_y = ccord_y
			# spawn_drone(wait_for_harvest)
			while not can_harvest():
				use_item(Items.Fertilizer)
				continue
			harvest()
			# Goto and plant the current plant's companion
			ctype, (ccord_x, ccord_y) = companion
			goto(ccord_x, ccord_y)
			tillx()
			plant(ctype)
			spawn_drone(water)
		else:
			return