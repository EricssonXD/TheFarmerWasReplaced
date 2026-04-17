from helpers import *

def xtill():
	if get_ground_type() == Grounds.Grassland:
		till()

def water():
	if get_water() < 0.75:
		use_item(Items.Water)

def auto_plant(plant_type):
	if plant_type == Entities.Carrot:
		pcarrot()

def pcarrot():
	xtill()
	water()
	plant(Entities.Carrot)
	
def ptree():
	if((get_pos_x()+get_pos_y())%2==0):
		plant(Entities.Tree)
		water()


# Size = 6 is the default size for pumpkins, 
# It would plant a megapumpkin of size 6 starting from the lower left corner of the pumpkin
def ppumpkin(size=6):
	
	start_x = get_pos_x()
	start_y = get_pos_y()
 
	def looppmpkin():
		xtill()
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
	
def psunflower():
	# init_x = get_pos_x()
	# init_y = get_pos_y()
	plist = []
	def loopsunflower():
		xtill()
		plant(Entities.Sunflower)
		p = measure()
		plist.append({"x": get_pos_x(), "y": get_pos_y(), "p": p})

	navigate_farm(loopsunflower, 3, 4)

	while num_items(Items.Power) < 1000:
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
