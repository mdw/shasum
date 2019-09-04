## shasum.py - create and verify SHA1 file hashes
This was designed to operate much like the *shasum* program on OSX and freeBSD. 
That is to say, instead of using sha1sum or sha256sum, simply specify the algorithm to be used.
Hashes generated are displayed and also saved to file.algo (file.sha1, file.sha256, file.sha512)

#### create SHA1, SHA256 or SHA512 hash of a file and write it to a file
#### compare SHA1, SHA256 or SHA512 hash of a file with a hash or file containing a hash

### examples:

#### create SHA1 and write it to file.sha1
$ ./shasum.py file.txt

#### compare SHA1(file.txt) to previous hash stored in text.sha1
$ ./shasum.py file.txt -c file.sha1
$ ./shasum.py file.txt -c 761f51bd951c41b98d6385e0751699bfb9acc0d0

#### create SHA256 hash of file.txt, save to file
$ ./shasum -a 256 checksumfile

#### compare SHA512 hash of file.txt with file.sha512
$ ./shasum -a 512 file.txt -c file.sha512

