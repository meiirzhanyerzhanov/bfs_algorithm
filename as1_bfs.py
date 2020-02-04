#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		for tr in traversed:
			try:
				queue.remove(tr)

			except:
				pass
		if(len(queue)>0):
			node = queue.pop(0)
			traversed.append(node)
			leaves = tree[node]
			for leaf in leaves:
				queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		'''
			You implement the path finder from here
		'''
		traversed = queue.pop(0)
		node = traversed[-1]
		if(node == goal):
			return traversed
		leaves = tree[node]
		for leaf in leaves:
			queue2 = list(traversed)
			queue2.append(leaf)
			queue.append(queue2)

	return "No such path exists"
