#!/usr/bin/python3

# MiddleSenior Task - NN
# Author: Matija Knezevic
# Version: 1.0


trademark_symbol = "®"


# get keywords into list

keywords_list = []
with open("Keywords.txt", "r", encoding="utf-8") as file:
	for keyword in file:

		# no new line
		current_place = keyword[:-1]
		keywords_list.append(current_place)


# read input file
with open("acme_docs.txt", "r", encoding="utf-8") as file:
	docs = file.read()

# replace keywords
for keyword in keywords_list:
	docs = docs.replace(keyword, keyword + trademark_symbol)
	with open("acme_docs.txt", "w", encoding="utf-8") as file:
		file.write(docs)