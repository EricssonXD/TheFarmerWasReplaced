from helpers import *

def tillx(tilled = True):
	if (get_ground_type() == Grounds.Grassland and tilled) or (get_ground_type() == Grounds.Soil and not tilled):
		till()

def harvestx():
	if can_harvest():
		harvest()

def water():
	if get_water() < 0.75:
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

	# Sort row
	for i in range(size_y):
		sorted = False
		while not sorted:
			sorted = True
			goto(init_x, init_y + i)
			for j in range(size_x-1):
				c_size = measure()
				c_next = measure(East)
				if c_next < c_size: # type: ignore
					swap(East)
					sorted = False
				move(East)
		goto(init_x, init_y + i)

	# Sort Column
	for i in range(size_x):
		sorted = False
		while not sorted:
			sorted = True
			goto(init_x + i, init_y)
			for j in range(size_y-1):
				c_size = measure()
				c_next = measure(North)
				if c_next < c_size: # type: ignore
					swap(North)
					sorted = False
				move(North)
		goto(init_x + i, init_y)

	goto(init_x, init_y)
	harvest()

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

	