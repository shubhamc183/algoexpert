#https://www.algoexpert.io/questions/Class%20Photos

## My first solution
def classPhotos(redShirtHeights, blueShirtHeights):
  redShirtHeights.sort()
	blueShirtHeights.sort()
	length_of_row = len(redShirtHeights)
	is_red_smaller, is_blue_taller = True, True
	is_red_taller, is_blue_shorter = True, True
	for i in range(length_of_row):
		if redShirtHeights[i] >= blueShirtHeights[i]:
			is_red_smaller = False
			is_blue_taller = False
		if blueShirtHeights[i] >= redShirtHeights[i]:
			is_red_taller = False
			is_blue_shorter = False
    return ( (is_red_smaller and is_blue_taller) or (is_red_taller and is_blue_shorter) )


## Algo Solution
def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	shirt_color_in_front = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	for i in range(len(redShirtHeights)):
		if shirt_color_in_front == 'RED':
			if redShirtHeights[i] >= blueShirtHeights[i]:
				return False
		else:
			if blueShirtHeights[i] >= redShirtHeights[i]:
				return False
	return True
