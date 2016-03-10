#!/usr/bin/env python
""" 
point in polygon 
Such an elegant language T_T 
USE space! Space!! is fxxking good!! Fxxk good. 
""" 

# concave polygon 
POLYGON = ((0, 0), (2, 5), (15, 22), 
(18, 19), (7, 10), (20, 0)) 

def pointInPolygon(x, y): 
	# the result 
	bInside = False 

	# start point of the line 
	polyStartX, polyStartY = POLYGON[0] 

	# judge the two lines is acrossed or not 
	for polyEndX, polyEndY in POLYGON: 
		if(y > min(polyStartY, polyEndY) 
		and y <= max(polyStartY, polyEndY) 
		and x <= max(polyStartX, polyEndX)): 
			if polyStartY != polyEndY: 
				xIntercept = \
				(y-polyStartY)*(polyEndX-polyStartX)/(polyEndY-polyStartY)\
				+polyStartX 
			if polyStartX == polyEndX or x <= xIntercept: 
				bInside = not bInside 
		polyStartX, polyStartY = polyEndX, polyEndY 

	# print result 
	if True == bInside: 
		print "Inside" 
	else: 
		print "Outside" 

	return bInside 


if __name__ == "__main__": 
	x = input("Enter x:") 
	y = input("Enter y:") 
	pointInPolygon(x, y) 
	print("----------Finish---------") 
	raw_input() 
