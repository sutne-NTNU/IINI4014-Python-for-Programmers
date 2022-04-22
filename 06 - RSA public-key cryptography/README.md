# RSA public-key cryptography

## Assignment
Study the code in rsa.py. Your task in this assignment is to uncover the private key and recover the plaintext from the encrypted message. In order to help with this challenge, you are also given a short piece of the plaintext to use as a way to filter valid results.

You are given the public key and a snippet of the plaintext. Using only this information, recover the private key used to encrypt the message, along with the decrypted message.

Public key:
```console
(29815, 100127)
```
Snippet of the plaintext message:
```python
"h"...
```
Encrypted message:
```console
[84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
```


## Results
After examining the code and reading about RSA, i figured that if we know the public key, we would have all the information we need to generate the private key as well. Using this approach in `rsa-cracker.py` i was able to generate the `private key`
```console
(64327, 100127)
```
and with this decrypt and retrieve the following plaintext message from the cipher-text given in the assignment:
```console
https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA
```
This seems to be the correct message, both because the result is a valid url, and the url matches the snippet of the plaintext we were given (it starts with "h")

As we can see this implementation of RSA is not very secure, this is mostly attributed to the low range of prime numbers used (100), because the numbers are so small it is fairly quick for a computer to brute-force its way through all the possible combinations. In a more secure RSA implementation the primes are much, much larger which makes brute force an incredibly time consuming task, even for a computer.
