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
	dist_x = get_pos_x() - x
	dist_y = get_pos_y() - y
	world_size = get_world_size()
	half_world = world_size//2
	if abs(dist_x) > half_world:
		if dist_x>0:
			dist_x = dist_x - world_size
		else:
			dist_x = dist_x + world_size
	if abs(dist_y) > half_world:
		if dist_y>0:
			dist_y = dist_y - world_size
		else:
			dist_y = dist_y + world_size

	for i in range(abs(dist_x)):
		if dist_x>0:
			move(West)
		else:
			move(East)
	for i in range(abs(dist_y)):
		if dist_y>0:
			move(South)
		else:
			move(North)
		
def timer(func):
	start_time = get_tick_count()
	func()
	end_time = get_tick_count()
	print(end_time - start_time)

CONST_DIRECTIONS = [North, East, South, West]