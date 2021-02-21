"""
Name: Aviv
ID: 316266683
Group: 01
Assignment: 7
"""
import csv
import json
"""
Function Name: crawler
Input: file, dict
output: dict
Function Operation: fills adictionary with the links that are inside the input
"""
def crawler(file, dict):
	with open(file, 'r') as f:
		lines = f.readlines()
		reffs = []
		parser(lines, reffs, file)
		#checks for keys in the dictionary
		for i in reffs:
			if i not in dict.keys():
				crawler(i, dict)
		return dict

	"""
Function Name: parser
Input: lines, dict, file
output: none
Function Operation: fills adictionary with the links that are inside the input
"""
def parser(lines, reffs, file):
	#checks for "href=" in the file
		for l in lines:
			if "href=" in l:
				start = l.find('"')
				start = start + 1
				end = l.find('"',start)
				reffs.append(l[start:end])
				reffs.sort()
		dict[file] = reffs

print("enter source file:")
file = input()
dict = {}
crawler(file, dict)
with open("results.csv", 'w', newline='') as f:
	writer = csv.writer(f)
	#fills a list with the dict keys and values
	for d in dict:
		lst = [d]
		lst.append(dict.get(d))
		writer.writerow(lst)
print("enter file name:")
inp = input()
print(dict.get(inp))
