#!/usr/bin/python3

# MiddleSenior Task - NN
# Author: Matija Knezevic
# Version: 1.0

trademark_symbol = "®"

# get keywords into list
keywords_list = []
with open("Keyword.txt", "r", encoding="utf-8") as keywords_file:
	for keyword in keywords_file:
		item = keyword.strip("\r\n")
		if len(item) > 0:
			keywords_list.append(item)

# remove duplicates
final_list = list(dict.fromkeys(keywords_list)) 

# read input file
with open("Acme_docs.txt", "r", encoding="utf-8") as acme_file:
	docs = acme_file.read()

# replace keywords and write changes
for keyword in final_list:
	docs = docs.replace(keyword, keyword + trademark_symbol)
	with open("Output_file.txt", "w", encoding="utf-8") as output_file:
		output_file.write(docs)




