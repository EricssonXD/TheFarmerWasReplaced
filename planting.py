def auto_plant(plant_type):
	if plant_type == Entities.Carrot:
		pcarrot()


def pcarrot():
	if get_ground_type() == Grounds.Grassland:
		till()
	plant(Entities.Carrot)
	
def ptree():
	if((get_pos_x()+get_pos_y())%2==0):
		plant(Entities.Tree)