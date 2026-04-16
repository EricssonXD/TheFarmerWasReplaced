from helpers import *
from planting import *

def hey_tree_carrot():
	water()
	if can_harvest():
		harvest()
	if(get_pos_x()>=6):
		pcarrot()
	else:
		ptree()

goto(0,0)
while True:
	navigate_farm(hey_tree_carrot)
			