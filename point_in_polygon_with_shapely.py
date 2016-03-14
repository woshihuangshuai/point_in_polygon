#!/usr/bin/env python
#coding:utf-8

import json
from shapely.geometry import asShape,Point

admin_level_2 = [] #国家

class area:
	def __init__(self):
		self.name = ''
		self.boundary = object
		self.next_level_list = []
		pass
	def __init__(self,name,boundary,next_level_list):
		self.name = name
		self.boundary = boundary
		self.next_level_list = next_level_list
	
		
def Get_area_list():
	print "Creat list of countrys'boundary..."
	with open('admin_level_2.geojson') as json_f:
		f = json.load(json_f)
	
	error_count = 0

	for feature in f['features']:
		try:
			polygon = asShape(feature["geometry"])
		except KeyError, e:
			error_count += 1
			continue
		try:
			if feature['osm_type'] == "relation":
				admin_area = area(feature['properties']['name:en'],polygon,[])
				admin_level_2.append(admin_area)	

		except KeyError, e:
			print KeyError
			error_count += 1
			print "error number:",error_count


	print "List of countrys'boundary has been created."

def point_in_polygon_with_shapely(lat,lon):
	point = Point(lat,lon)
	for area in admin_level_2:
		if area.boundary.intersects(point):#contains() or crosses() or equals() or touches() or within()
			print point,"is in %s"%area.name
			return True
	print "Point doesn't found"
	return False

if __name__ == '__main__':
	Get_area_list()
	point_in_polygon_with_shapely(116.3579936,39.9587666) #china
	point_in_polygon_with_shapely(-87.3857493,12.8596198) #nicaragua 
	point_in_polygon_with_shapely(10.4234469,51.0834196) #germany false
	point_in_polygon_with_shapely(-4.0239568,39.8560679) #spain false
	point_in_polygon_with_shapely(-2.2900239,16.3700359) #mali false
	point_in_polygon_with_shapely(2.3514992,48.8566101) #france


