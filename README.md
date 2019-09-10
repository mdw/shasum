## shasum.py - create and verify SHA1 file hashes
This was designed to operate much like the *shasum* program on OSX and freeBSD. 
That is to say, instead of using *sha1sum* or *sha256sum*, simply specify the algorithm to be used.
Hashes generated are displayed and also saved to file.algo (file.sha1, file.sha256, etc.)
Supported hashing algorithms: SHA1, SHA256, SHA512, SHA3, blake2

usage: shasum.py [-h] [-a {sha1,sha256,sha512,sha3}] [-c COMPARE [-s SIZE]] filename

hash a file or compare hash to file

positional arguments:
  filename              file to be hashed or compared

optional arguments:
  -h, --help            show this help message and exit
  -a {sha1,sha256,sha512,sha3,blake2}, --algorithm {sha1,sha256,sha512,sha3,blake2}
                        choose hashing algorithm: sha1 (default), sha256, sha512, sha3(256), blake2
  -c COMPARE, --compare COMPARE
                        provide a hash or file containing hash to compare
  -s SIZE, --size SIZE
						choose output size in bytes, 8, 16, 20, 24, 32, 40, 64 for blake2, default is 20 bytes,
						choose 32 or 64 bytes for SHA3, default is 64 bytes


### examples:

#### create SHA1 and write it to file.sha1
- $ ./shasum.py file.txt

#### compare SHA1(file.txt) to previous hash stored in text.sha1
- $ ./shasum.py file.txt -c file.sha1
- $ ./shasum.py file.txt -c 761f51bd951c41b98d6385e0751699bfb9acc0d0

#### create SHA256 hash of file.txt and write to disk as file.sha256
- $ ./shasum -a sha256 file.txt

#### compare SHA3 hash of file.txt to the checksum literal (or from file)
- $ ./shasum -a sha3 file.txt -c 171609e28789aa5d3a30b02d14bae27509dc5228318123c7fec96cab83749dcd
- $ ./shasum -a sha3 -s 32 file.txt -c file.sha3

#### create SHA256 hash of file.txt, save to file
- $ ./shasum -a sha256 checksumfile

#### compare SHA512 hash of file.txt with file.sha512
- $ ./shasum -a sha512 file.txt -c file.sha512

#### create 20-byte blake2 hash of file.txt 
- $ ./shasum -a blake2 file.txt 

#### compare 40-byte blake2 hash of file.txt to checksumfile 
- $ ./shasum -a blake2 -s 40 file.txt -c checksumfile

#### find size of hash stored in checksumfile and compare to hash of file.txt
note checksumfile contains hex chars, 2 hex chars for each byte
- $ wc -c checksumfile
- 128 checksumfile
- $ ./shasum.py -a blake2 -s 64 file.txt -c checksumfile

