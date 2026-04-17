def pmaze(size = 5):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
	facing = North
	to_right = {North: East, East: South, South: West, West: North}
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		if can_move(to_right[facing]):
			move(to_right[facing])
			facing = to_right[facing]
		elif can_move(facing):
			move(facing)
		elif can_move(to_right[to_right[facing]]):
			move(to_right[to_right[to_right[facing]]])
			facing = to_right[to_right[to_right[facing]]]
		else:
			move(to_right[to_right[facing]])
			facing = to_right[to_right[facing]]
