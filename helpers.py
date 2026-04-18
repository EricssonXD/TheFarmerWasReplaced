def navigate_farm(loop_function, sizex = get_world_size(), sizey = get_world_size()):
	for i in range(sizex):
		for j in range(sizey-1):
			loop_function()
			if i%2==0:
				move(North)
			else:
				move(South)
		loop_function()
		if i != sizex-1:
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
		
def timer(func):
    start_time = get_tick_count()
    func()
    end_time = get_tick_count()
    print(end_time - start_time)