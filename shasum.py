#!/usr/bin/python3

import os
import argparse
import hashlib
from termcolor import cprint


class HashFile:
	""" hash a file or compare to a hash value to verify file integrity """

	def __init__(self):
		self.path = None

	@staticmethod
	def get_args():
		parser = argparse.ArgumentParser(description="hash a file or compare hash to file")
		parser.add_argument("filename", help="file to be hashed")
		parser.add_argument("-a", "--algorithm", default="sha1",
							choices=['sha1', 'sha256', 'sha512', 'sha3'],
							help="choose hashing algorithm: sha1 (default), sha256, sha512, sha3 (256)")
		parser.add_argument("-c", "--compare", help="provide a hash to compare")
		return parser.parse_args()


	def open_hash(self, hash_filename):
		hash = hash_filename
		if os.path.isfile(hash_filename):
			with open(hash_filename, 'r') as f:
				hash = f.read().splitlines()[0]
		return hash


	def compare_hash(self, old, new):
		if old == new:
			cprint(f"verified: {old}", 'green')
		else:
			cprint(f"DIGEST DOES NOT MATCH\nold {old}\nnew {new}", 'red')


	def write_hash_file(self, file, algo):
		"""write hash to a file with same name, sha extension"""
		file_name = file.split('.')[0] + '.' + algo
		with open(file_name, 'w') as f:
			f.write(self.compute_hash(file, algo))


	def compute_hash(self, file, algo):
		BUFF_SIZE = 65536
		if algo == 'sha256':
			digest = hashlib.sha256()
		elif algo == 'sha512':
			digest = hashlib.sha512()
		elif algo == 'sha3':
			digest = hashlib.sha3_256()
		else:
			digest = hashlib.sha1()

		with open(file, 'rb') as f:
			while True:
				# read in one chunk at a time
				data = f.read(BUFF_SIZE)
				if not data:
					break
				# keep updating digest until no more chunks of data
				digest.update(data)
		return digest.hexdigest()
		

	def main(self):
		args = self.get_args()
		self.filename = args.filename

		algo = 'sha1' if not args.algorithm else args.algorithm
		hash = self.compute_hash(self.filename, algo)
		
		if args.compare:
			old_hash = self.open_hash(args.compare)
			self.compare_hash(old_hash, hash)
		else:
			self.write_hash_file(self.filename, algo)
			cprint(hash, 'blue')



if __name__ == '__main__':
	hash_instance = HashFile()
	hash_instance.main()

