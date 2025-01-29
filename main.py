import json
import random
import requests
from util import start_a_nodes,node_retry,start_all_nodes,start_health_monitor,MAX_PORTS
import subprocess

from content import check_if_exists_and_print_html

from generate_urls import make_urls, get_random_url

from make_graph_function import make_graph_from_adjacency_list

URLS = []

number_of_ports = int(input("Enter number of nodes : "))

if number_of_ports > MAX_PORTS:
	print("only "+MAX_PORTS+" nodes created")
	URLS.extend(make_urls(MAX_PORTS))

else:
	URLS.extend(make_urls(number_of_ports))

if len(URLS)==0:
	raise Exception('configuration error')

print(URLS)

try:
	start_all_nodes(number_of_ports)
	start_health_monitor(number_of_ports)
except Exception as e:
	print('inital node starting failed')
	print(e)
	raise e
	

gateway_storage_dict = {}


while True:
	command = input("=> Enter Command : ")

	if command == "end":
		break
	elif command == "crawl":
		website = input("Enter Website : ")
		levels = int(input("Enter levels : "))
		
		#choose any random url
		[random_index, random_url] = get_random_url(URLS)
		# this url is of the format : http://localhost::5000/ 
		# now we need to add "crawl" in it
		
		url = random_url + "crawl"

		params = {
			'website' : website,
			'levels' : levels,
		}
		try:

			r = requests.get(url=url, params = params)
			print("Crawling has returned")
			print(r.text)
		except:
			print("Crawling operation did not Complete")
		continue

	elif command == "make_graph":
		website = input("Enter Website : ")
		depth = int(input("Enter depth : "))
		response_dict = {}
		# check if the node has searched it. If it has, carry on forward. If it has not, then, come back with a NULL
		for url in URLS:
			# send a search party in the url
			url = url + "make_graph"
			params = {
			'website' : website,
			'depth' : depth,
			}
			# the response that we get from each will be put into a dictionary
			# Then it will be sent for further processing in a different file
			# From there, a line graph will be generated
			r = requests.get(url=url, params=params)
			data = json.loads(r.text)

			for key in data.keys():
				if key not in response_dict:
					response_dict[key] = data[key]
				else:
					non_redundant_child_list = list(set(data[key] + response_dict[key]))
					response_dict[key] = non_redundant_child_list

		# print(response_dict)
		
		make_graph_from_adjacency_list(response_dict)

		continue
	elif command == "show_html":
		website = input("Enter Website : ")
		name = "storage/" + website.replace('/', '') + ".txt"
		print(name)
		check_if_exists_and_print_html(name)
		continue
	elif command == 'exit':
		exit(0)
	else:
		print("Invalid Command . Try Again")
		continue

	