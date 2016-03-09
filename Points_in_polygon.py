#!/usr/bin/env python
#coding:utf-8

import collections
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET

admin_level_4 = []
admin_level_5 = []
admin_level_6 = []

def Get_area_list():
	nodes = collections.OrderedDict()
	ways = collections.OrderedDict()

	try:
		element_tree = ET.parse("beijing_china.osm")
		root = element_tree.getroot()
	except Exception, e: 
  		print "Error:cannot parse albany_new-york.osm"
  		sys.exit(1) 

	for node in root.findall("node"):
		nodes[node.get("id")] = [node.get("lat"),node.get("lon")]

	for way in root.findall("way"):
		nodes_of_way = []
		for nd in way.findall("nd"):
			nodes_of_way.append(nodes[nd.get("ref")])
		ways[way.get("id")] = nodes_of_way

	for area in root.findall("relation"):
		tag_list =  area.findall("tag")
		boundary = []	
		for tag in tag_list:
			if (tag.get("k") == "admin_level")&(tag.get("v") == "4"):
				for tag in tag_list:
					if(tag.get("k") == "name:en"):
						for member in area.findall("member"):
							if member.get("type") == "way":
								boundary.extend(ways[member.get("ref")])
							elif member.get("type") == "node":
								boundary.extend(nodes[member.get("ref")])
						admin_level_4.append([tag.get("v"),boundary,[]])

			elif (tag.get("k") == "admin_level")&(tag.get("v") == "5"):
				for tag in tag_list:
					if(tag.get("k") == "name:en"):
						for member in area.findall("member"):
							if member.get("type") == "way":
								boundary.extend(ways[member.get("ref")])
							elif member.get("type") == "node":
								boundary.extend(nodes[member.get("ref")])
						admin_level_5.append([tag.get("v"),boundary,[]])

			elif (tag.get("k") == "admin_level")&(tag.get("v") == "6"):
				for tag in tag_list:
					if(tag.get("k") == "name:en"):
						for member in area.findall("member"):
							if member.get("type") == "way":
								boundary.extend(ways[member.get("ref")])
							elif member.get("type") == "node":
								boundary.extend(nodes[member.get("ref")])
						admin_level_6.append([tag.get("v"),boundary,[]])

	admin_level_4[1][2].append(admin_level_5)
	admin_level_4[0][2].append(admin_level_6)

	for a in admin_level_4:
		print a		

if __name__ == '__main__':
	Get_area_list()
	pass