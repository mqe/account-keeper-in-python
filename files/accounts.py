import csv
import sys
import math
import time

import collections

accounts_dict = {}

if __name__ == '__main__':
	# set arguments as variables
	if str(sys.argv[1]) == "add":
		account = sys.argv[2]
		name = sys.argv[3]
		hint = sys.argv[4]

		# create new or append existing csv to store data
		file = open("accounts" + ".csv", "a")
		file.write(account + ", " + name + ", " + hint + "\n")
		file.close()

		category = account[0]
		print "\n\n--------------------------------------\n"
		print "Category: " + category + "\n"
		print account + "\t\t" + name + "\t\t" + hint


	elif str(sys.argv[1]) == "all":
		category = "A"
		reader = csv.reader(open("accounts.csv", 'rU'), delimiter=',')
		for line in reader:
			#
			accounts_dict[line[0].upper()] = [line[1], line[2]]

		accounts_dict = collections.OrderedDict(sorted(accounts_dict.items()))
		print "-" * (23 + 34 + 22)
		print('{0:23} {1:34} {2:22}'.format("Accounts", "Name", "Hint"))
		print "-" * (23 + 34 + 22)
		for item in accounts_dict:
			#
			if item[0][0] != category:
				category = item[0][0].upper()
				print "-" * (23 + 34 + 22)

			print('{0:22} {1:34} {2:22}'.format(item, accounts_dict[item][0], accounts_dict[item][1]))
		
	print "-" * (23 + 34 + 22)
	print "Add new? -> accounts.py add 'account' 'name' 'hint'"
	print "\n"