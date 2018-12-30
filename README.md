# pwnedpasscheck

***pwnedpasscheck*** s for pwned passwords from [haveibeenpwned.com](https://haveibeenpwned.com/API/v2#PwnedPasswords) v2 API by using the [pwnedpasswords](https://github.com/lionheart/pwnedpasswords) library.

How to use:
---

```shell
python pwnedpasscheck.py -h
  
usage: pwnedpasscheck.py [-h] [-p PASSWORD] [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        The password you want to test
  -f FILE, --file FILE  Load a file with multiple passwords to check
  ```
  
  You can also execute it directly from shell
  
  ```shell
  ./pwnedpasscheck.py
  ```
  or with arguments.
  
  Examples
  ---
  
  ```shell
  ./pwnedpasscheck.py -p password1
  ```
  
  ```shell
  ./pwnedpasscheck.py -f FileWithOnePasswordPerRow
  ```
