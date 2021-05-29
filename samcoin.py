#!/usr/bin/env python3

# Extremely primitive blockchain code for fun

# -- Raspberry pi pandas install instructions --
# sudo apt-get install libatlas-base-dev
# pip3 install pandas

import hashlib
import pandas as pd
import numpy as np
from tabulate import tabulate
import random
import datetime

class block:
	def __init__(self, index, time_stamp, data, previous_hash):
		self.index = index
		self.time_stamp = time_stamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calculate_hash()

	def __str__(self):
		return f'{self.index}, {self.time_stamp}, {self.data}, {self.previous_hash}, {self.hash}'

	#def __repr__(self):
	#	return [{self.index}, {self.time_stamp}] 

	def calculate_hash(self):
		to_hash = (str(self.index) + self.time_stamp + self.data + self.previous_hash).encode()
		return hashlib.sha256(to_hash).hexdigest()

class block_chain:
	def __init__(self):
		self.chain = [self.create_genesis_block()]

	def create_genesis_block(self):
		return block(0, "1/1/1970", "I am genesis block - fear me", "Not a hash - shrug")

	def get_latest_block(self):
		return self.chain[len(self.chain) - 1]

	def add_block(self, index, time_stamp, data):
		new_block = block(index, time_stamp, data, self.get_latest_block().hash)
		new_block.hash = new_block.calculate_hash()
		self.chain.append(new_block)

def header():
	print("SamCoin", datetime.datetime.now().year, "(c)\n\n\n")

def print_table():
	arr = np.transpose(str(samcoin.chain[0]).split(','))
	for i in range(1, len(samcoin.chain)):
		arr = np.vstack((arr, np.transpose(str(samcoin.chain[i]).split(','))))

	df = pd.DataFrame(arr)
	df_col_header = ['Index', 'Time Stamp', 'Data', 'Previous Block Hash', 'Current Block Hash']
	df.columns = df_col_header

	with open('samcoin_ledger.html', 'w') as f:
	    f.write(df.to_html())

	print(tabulate(arr, headers=df_col_header))

header()
try_to_cheat = 0

samcoin = block_chain()
for i in range(1,30):
	if(try_to_cheat == 1):
		if (i == 5):
			samcoin.add_block(i,  "05/" + str(i) + "/2021",  "sam to sam : 100000 samcoin")
		else:
			samcoin.add_block(i,  "05/" + str(i) + "/2021",  "sam to sam : 10 samcoin")
	else:
		samcoin.add_block(i,  "05/" + str(i) + "/2021",  "sam to sam : 10 samcoin")

print_table()
