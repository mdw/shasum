## shasum.py - create and verify SHA1 file hashes
This was designed to operate much like the *shasum* program on OSX and freeBSD. 
That is to say, instead of using *sha1sum* or *sha256sum*, simply specify the algorithm to be used.
Hashes generated are displayed and also saved to file.algo (file.sha1, file.sha256, etc.)
Supported hashing algorithms: SHA1, SHA256, SHA512, SHA3

usage: shasum.py [-h] [-a {sha1,sha256,sha512,sha3}] [-c COMPARE] filename

hash a file or compare hash to file

positional arguments:
  filename              file to be hashed

optional arguments:
  -h, --help            show this help message and exit
  -a {sha1,sha256,sha512,sha3}, --algorithm {sha1,sha256,sha512,sha3}
                        choose hashing algorithm: sha1 (default), sha256,
                        sha512, sha3 (256)
  -c COMPARE, --compare COMPARE
                        provide a hash to compare


### examples:

#### create SHA1 and write it to file.sha1
$ ./shasum.py file.txt

#### compare SHA1(file.txt) to previous hash stored in text.sha1
$ ./shasum.py file.txt -c file.sha1
$ ./shasum.py file.txt -c 761f51bd951c41b98d6385e0751699bfb9acc0d0

#### create SHA256 hash of file.txt and write to disk as file.sha256
$ ./shasum -a sha256 file.txt

#### compare SHA3 hash of file.txt to the checksum literal (or from file)
$ ./shasum -a sha3 file.txt -c 171609e28789aa5d3a30b02d14bae27509dc5228318123c7fec96cab83749dcd
$ ./shasum -a sha3 file.txt -c file.sha3

#### create SHA256 hash of file.txt, save to file
$ ./shasum -a 256 checksumfile

#### compare SHA512 hash of file.txt with file.sha512
$ ./shasum -a 512 file.txt -c file.sha512

