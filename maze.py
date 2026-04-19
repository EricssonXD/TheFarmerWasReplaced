from helpers import CONST_DIRECTIONS


def pmaze(size = 5):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	facing = 0 # 0: North, 1: East, 2: South, 3: West
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		# Try to turn right
		if can_move(CONST_DIRECTIONS[(facing + 1) % 4]):
			move(CONST_DIRECTIONS[(facing + 1) % 4])
			facing = (facing + 1) % 4
		# If can't turn right, try to move forward
		elif can_move(CONST_DIRECTIONS[facing]):
			move(CONST_DIRECTIONS[facing])
		# If can't move forward, try to turn left
		elif can_move(CONST_DIRECTIONS[(facing - 1) % 4]):
			move(CONST_DIRECTIONS[(facing - 1) % 4])
			facing = (facing - 1) % 4
		# If can't turn left, try to turn back
		else:
			move(CONST_DIRECTIONS[(facing + 2) % 4])
			facing = (facing + 2) % 4

def euclidean_distance(x1, y1, x2, y2):
	return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def maze_astar():
	# Use measure on the treasure to get its coordinates
	# treasure_x, treasure_y = measure()
	open_list = [(0, get_pos_x(), get_pos_y())]  # (f_score, x, y)
	closed_list = []