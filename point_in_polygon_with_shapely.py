#!/usr/bin/env python
#coding:utf-8

import json
from shapely.geometry import asShape,Point

admin_level_6 = [] #区
admin_level_8 = [] #街道

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
	json_f = open('beijing.json')
	f = json.load(json_f)

	error_count = 0

	for feature in f['features']:
		try:
			polygon = asShape(feature["geometry"])
		except KeyError, e:
			error_count += 1
			continue
		if feature['properties']['tags'] != None:
			tag_list =  feature['properties']['tags'].split('\"',)
			for tag in tag_list:
				if tag == 'admin_level':
					admin_area = area(tag_list[tag_list.index("name:en")+2],polygon,[])
					if tag_list[tag_list.index(tag)+2] == '6':
						admin_level_6.append(admin_area)
					elif tag_list[tag_list.index(tag)+2] == '8':
						admin_level_8.append(admin_area)

def point_in_polygon_with_shapely(lat,lon):
	point = Point(lat,lon)
	for area in admin_level_6:
		if area.boundary.contains(point) or area.boundary.touches(point):
			print "This point is in %s"%area.name
			return True
	print "Point doesn't found"
	return False

if __name__ == '__main__':
	Get_area_list()
	lat = input("Input latitude:")
	lon = input("Input longitude:")
	point_in_polygon_with_shapely(lat,lon)
	#point_in_polygon_with_shapely(116.3579936,39.9587666)

