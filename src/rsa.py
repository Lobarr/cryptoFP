from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from src.helpers import strToBytes, encodeBytes, decodeBytes

class RSA:
  """
  A class for encrypting and decrypting string data using RSA asymmetric encryption algorithm

  Parameters
  ----------
  data : str
    data to be encrypted 
  """
  def __init__(self, data: str=None):
    self.__private = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048,
      backend=default_backend()
    )
    self.__public = self.__private.public_key()
    self.__data = data
  """
  returns generated public key
  """
  def publicKey(self):
    return self.__public.public_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
  """
  returns generated private key
  """
  def privateKey(self):
    return self.__private.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.TraditionalOpenSSL,
      encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')
  """
  setter for data private variable
  """
  def setData(self, data):
    self.__data = data
  """
  Encrypts provided data

  Returns : bytes
  -------
  ciphertext of encrypted data
  """
  def encrypt(self) -> bytes:
    return encodeBytes(self.__public.encrypt(strToBytes(self.__data), padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    ))).decode('utf-8')
  """
  Decrypts provded ciphertext

  Parameters
  ----------
  ct : bytes
    ciphertext of encrypted data
  
  Returns : str
  -------
  decrypted data
  """
  def decrypt(self, ct):
    return self.__private.decrypt(decodeBytes(ct.encode('utf-8')), padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )).decode("utf-8")