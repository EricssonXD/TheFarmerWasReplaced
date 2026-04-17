def navigate_farm(loop_function, size = get_world_size()):
	for i in range(size):
		for j in range(size-1):
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
		

  