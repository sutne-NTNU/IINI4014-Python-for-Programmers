# reusing fucntions from rsa, as these aren't secret, just math operations
from rsa import PrimeGen, multiplicative_inverse, decrypt

# infomration given in the assignment
public_key = (29815, 100127)
encrypted_message = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020,
                     70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020,
                     70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175,
                     54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175,
                     81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243,
                     81327, 81444, 32170, 53121]
start_of_plaintext = "h"


def main():
    # from the public key we can get the following information
    e = public_key[0]
    n = public_key[1]

    # we know that n will be equal to p * q, which are the primes used the generate the keypair,
    # we can then go through primenumbers until we find the two primes that create this product
    # (there can only be one pair with this exact product)
    p = q = 0
    primes = PrimeGen(100)
    for p_test in primes:
        for q_test in primes:
            if p_test * q_test == n:
                p = p_test
                q = q_test
                break

    # now we can simply find phi with
    phi = (p - 1) * (q - 1)

    # this is used to generate the private key with:
    d = multiplicative_inverse(e, phi)

    # we have now "found" the private key:
    private_key = (d, n)
    print("Private Key:", private_key)

    # now we can use this to decrypt our message
    message = decrypt(private_key, ciphertext=encrypted_message)
    print("Plaintext Message:", message)


if __name__ == "__main__":
    main()
