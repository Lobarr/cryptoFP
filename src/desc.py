#Sources referenced:
"""
INFR-3600U Notes
https://thebestvpn.com/advanced-encryption-standard-aes/
https://datalocker.com/what-is-the-difference-between-ecb-mode-versus-cbc-mode-aes-encryption/
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm
"""

class DESC():
    """
    A class for providing information on each cryptographic function

    Parameters
    ----------
    mode : str
        function to be explained
    operation : str
        function operation (encrypy/decrypt)
    extended : chr
        show extended information
    extdata(1-4) : str
        external data from other objects to be shown
    """
    def __init__(self, operation, extended, extdata1: str=None, extdata2: str=None, extdata3: str=None, extdata4: str=None):        
        self.__operation = operation
        self.__extended = extended
        #External data
        self.__extdata1 = extdata1 #Ex. for AES = key
        self.__extdata2 = extdata2 #Ex. for AES = iv
        self.__extdata3 = extdata3 #Ex. for AES = results.arg
        self.__extdata4 = extdata4 #Ex. for AES = aes.encrypt() or .decrypt()
    """
    Provides information about AES
    """
    def AES(self):
        print( #General info
            "\nAES:\n"
            "---------------------------------------------------------------------------------------------------\n"
            "The Advanced Encryption Standard, or AES, is a symmetric block cipher.\n" 
            "AES comprises 3 block ciphers: AES-128, AES-192, and AES-256.\n"
            "Each cipher encrypts and decrypts data in blocks of 128 bits using keys of 128, 192, and 256 bits.\n"
            "Symmetric ciphers use the same key for encrypting and decrypting.\n"
            "There are 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys.\n"
            "A round consists of several processing steps that include substitution, transposition and mixing of\n"
            "the input plaintext to transform it into the final output of ciphertext.\n"
            "---------------------------------------------------------------------------------------------------\n"
            "Cipher Blocker Chaning, or CBC, is an advanced form of block cipher encryption.\n"
            "Each ciphertext block is dependent on all plaintext blocks processed up to that point.\n"
            "---------------------------------------------------------------------------------------------------"
        )
        if self.__operation == "encrypt":
            print( #Encryption info
                self.__extdata3 ,"has been encrypted:", self.__extdata4, "\n"
            )
        elif self.__operation == "decrypt":
            print( #Decryption info
                self.__extdata3 ,"has been decrypted:", self.__extdata4, "\n"
            )
        
        if self.__extended == 'y':
            print( #Extended info
                "Extended Information:\n"
                "Key:", self.__extdata1, "Initialization Vector:", self.__extdata2, "\n\n"
                "The key is used to define the mapping between plaintext and ciphertext.\n"
                "The initialization vector is a fixed-size input to a cryptographic primitive.\n"
                "Each message is made unique through this initialziation vector.\n"
                "---------------------------------------------------------------------------------------------------\n"
            )
    """
    Provides information about Caesar Cipher
    """
    def Caesar(self):
        print( #General info
            "\nCaesar Cipher:\n"
            "---------------------------------------------------------------------------------------------------------------\n"
            "Caesar Cipher is the simplest and earliest known use of a substitution cipher originally used by Julius Caesar.\n"
            "Each letter is replaced with the letter standing three places further down the alphabet.\n"
            "The alphabet is wrapped around so that the letter following Z is A.\n"
            "---------------------------------------------------------------------------------------------------------------"
        )
        if self.__operation == "encrypt":
            print( #Encryption info
                self.__extdata3 ,"has been encrypted:", self.__extdata4, "\n"
            )
        elif self.__operation == "decrypt":
            print( #Decryption info
                self.__extdata3 ,"has been decrypted:", self.__extdata4, "\n"
            )
        
        if self.__extended == 'y':
            print( #Extended info
                "Extended Information:\n"
                "Key:", self.__extdata1, "\n\n"
                "The key is used to define the starting point of the alphabet in which each letter is shifted.\n"
                "---------------------------------------------------------------------------------------------------------------\n"
            )
    """
    Provides information about hasher
    """
    def Hasher(self):
        print( #General info
            "\nHasher:\n"
            "-----------------------------------------------------------------------------------------------------------------\n"
            "A hash function H accepts a variable-length block of data M as input and produces a fixed-size hash value: h=H(M)\n"
            "Cryptographic hash functions are computationally infeasible to find:\n"
            "   (A) a data object that maps to a pre-specified hash result (one-way property) or\n"
            "   (B) two data objects that map to the same hash result (collision-free property)\n"
            "Because of these characteristics, hash functions may be used to determine data integrity.\n"
            "-----------------------------------------------------------------------------------------------------------------"
        )
        if self.__operation == "sha256":
            print( #SHA256 info
                self.__extdata3 ,"has been hashed using SHA256:", self.__extdata4, "\n"
            )
        elif self.__operation == "sha512":
            print( #SHA512 info
                self.__extdata3 ,"has been hashed using SHA512:", self.__extdata4, "\n"
            )
        elif self.__operation == "md5":
            print( #MD5 info
                self.__extdata3 ,"has been hashed using MD5:", self.__extdata4, "\n"
            )
        
        if self.__extended == 'y':
            print( #Extended info
                "Extended Information:\n"
                "No extended information available.\n"
                "-----------------------------------------------------------------------------------------------------------------\n"
            )
    """
    Provides information about RSA
    """
    def RSA(self):
        print( #General info
            "\nRSA:\n"
            "-------------------------------------------------------------------------------------------\n"
            "RSA ia an asymmetric algorithm, which uses two different keys: a public and private key.\n"
            "Keys are generated through these steps:\n"
            "   (1) Two different large random prime numbers p and q are chosen\n"
            "   (2) The modulus of the public and private keys n is computed through p*q\n"
            "   (3) The totient of n is computed through (p-1)*(q-1)\n"
            "   (4) An integer e is selected such that 1 < e < totient(n)\n"
            "       - e is released as the public key exponent\n"
            "   (5) A value d is computed to satisfy the congruence relation d*e ≡ 1 (modulus totient(n))\n"
            "       - d is kept as the private key exponent\n"
            "The public key is made of n^e and the private key is made of n^d.\n"
            "-------------------------------------------------------------------------------------------"
        )
        if self.__operation == "encrypt":
            print( #Encryption info
                self.__extdata3 ,"has been encrypted:", self.__extdata4, "\n"                
        )
        elif self.__operation == "decrypt":
            print( #Decryption info
                self.__extdata3 ,"has been decrypted:", self.__extdata4, "\n"               
        )
    
        if self.__extended == 'y':
            print( #Extended info
                "Extended Information:\n"
                "Public Key:", self.__extdata1, "Private Key:", self.__extdata2, "\n\n"
                "These keys are used in encryption/decryption through RSA.\n"
                "For encryption, message M is turned into a number m smaller than n by using an agreed-upon\n"
                "reversible protocol known as a padding scheme. Ciphertext c is computed as c=m^e mod n\n"   
                "For decryption, m can by recovered from c using private key d: m=c^d mod n\n"
                "With m, the original distinct prime numbers can be recovered: m^e*d ≡ m mod p*q\n"
                "So, c^d ≡ m mod n\n"
                "-------------------------------------------------------------------------------------------\n"   
        )
    """
    Provides information about ECDSA
    """
    def ECDSA(self):
        print( #General info
            "\nECDSA:\n"
            "----------------------------------------------------------------------------------------------------\n"
            "ECDSA, or Elliptic Curve Digital Signature Algorithm, is a variant of Digital Signature Algorithm\n"
            "which uses elliptic curve cryptography. To sign a message, three parameters must be established:\n"
            "   (1) curve : the elliptic curve field and equation used\n"
            "   (2) g : elliptic curve base point, a generator of the elliptic curve with large prime order n\n"
            "   (3) n : integer order of G, n * G = O, where O is the identity element (must be prime)\n"
            "A key pair consisting of dₐ and Qₐ are created:\n"
            "   dₐ : randomly selected in the interval [1, n-1]\n"
            "   Qₐ : public key curve point Qₐ = dₐ x G (x denotes elliptic curve point multiplication by scalar)\n"
            "----------------------------------------------------------------------------------------------------"

        )
        if self.__operation == "sign":
            print ( #Signature info
                self.__extdata3 ,"has been signed:", self.__extdata4, "\n"
            )
        elif self.__operation == "verify":
            print( #Verification info
                self.__extdata3 ,"is verified:", self.__extdata4, "\n"
            )
        
        if self.__extended == 'y':
            print( #Extended info
                "Extended Information:\n"
                "Public Key:", self.__extdata1, "Private Key:", self.__extdata2, "\n\n"
                "To sign a message m:\n"
                "   (1) Calculate e = hash(m)\n"
                "   (2) Let z be the Lₙ leftmost bits of e, where Lₙ is the bit length of the group order n\n"
                "   (3) Choose a cryptographycally secure random integer k from [1, n-1]\n"
                "   (4) Calculate curve point (x1, y1) = k x G\n"
                "   (5) Calculate r = x1 mod n (If r = 0, go to step 3)\n"
                "   (6) Calculate s = k^-1(z + r*dₐ) mod n (If s = 0, go to step 3)\n"
                "   (7) The signature is the pair (r,s)\n"
                "To verify a signature:\n"
                "   (1) Verify r and s are integers in [1, n-1]\n"
                "   (2) Calculate e = hash(m)\n"
                "   (3) Let z be the Lₙ leftmost bits of e\n"
                "   (4) Calculate w = s^-1 mod n\n"
                "   (5) Calculate u1 = z*w mod n and u2 = r*w mod n\n"
                "   (6) Calculate the curve point (x1,y2) = u1 x G + u2 x Qₐ (if (x1,y2) = O, signature is invalid)\n"
                "   (7) The signature is only valid if r ≡ x1 (mod n)\n"
                "----------------------------------------------------------------------------------------------------\n"
            )