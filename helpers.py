def navigate_farm(loop_function):
	for i in range(get_world_size()):
		for j in range(get_world_size()-1):
			loop_function()
			if i%2==0:
				move(North)
			else:
				move(South)
		loop_function()
		move(East)
		

def goto(x,y):
	for i in range(abs(get_pos_x()-x)):
		if get_pos_x()-x>0:
			move(West)
		else:
			move(East)
	for i in range(abs(get_pos_y()-y)):
		if get_pos_y()-y>0:
			move(South)
		else:
			move(North)
		
def water():
	if get_water() < 0.5:
		use_item(Items.Water)
  