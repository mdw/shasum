## shasum.py - create and verify SHA1 file hashes

#### create SHA1 hash of a *file.ext* and write it to *file.sha1*

#### :create SHA1 and write it to file.sha1
$ ./shasum.py file.txt

#### compare SHA1(file.txt) to previous hash stored in text.sha1
$ ./shasum.py file.txt -c file.sha1
$ ./shasum.py file.txt -c 761f51bd951c41b98d6385e0751699bfb9acc0d0
$ ./shasum.py file.txt -c "761f51bd951c41b98d6385e0751699bfb9acc0d0"
$ ./shasum.py file.txt -c $(cat file.sha1)

