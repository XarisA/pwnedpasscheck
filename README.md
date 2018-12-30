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
  
 
Security Note from [lionheart/pwnedpasswords](https://github.com/lionheart/pwnedpasswords)
---

*No plaintext passwords ever leave your machine using pwnedpasswords.
How does that work? Well, the Pwned Passwords v2 API has a pretty cool k-anonymity implementation.*

*From https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/:*

    Formally, a data set can be said to hold the property of k-anonymity, if for every record in a released table, there are k − 1 other records identical to it.

*This allows us to only provide the first 5 characters of the SHA-1 hash of the password in question. The API then responds with a list of SHA-1 hash suffixes with that prefix. On average, that list contains 478 results.
People smarter than I am have used math to prove that 5-character prefixes are sufficient to maintain k-anonymity for this database.*

In short: your plaintext passwords are protected if you use this library. You won't leak enough data to identity which passwords you're searching for.
