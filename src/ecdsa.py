from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
from src.helpers import encodeBytes, decodeBytes, strToBytes

class ECDSA:
  """
  A class for digital signature using Elliptic curve cryptography

  Parameters
  ----------
  message : str
    message to be signed / verified
  """
  def __init__(self, message: str=None):
    self.__message = message
    self.__private = ec.generate_private_key(
     ec.SECP384R1(), default_backend()
    )
    self.__public = self.__private.public_key()
  """
  Getter for private and public keys
  """
  def publicKey(self):
    return self.__public.public_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
  def privateKey(self):
    return self.__private.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.TraditionalOpenSSL,
      encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')
  def setMessage(self, message):
    self.__message = message
  """
  Returns : str
  -------
  signature of a message
  """
  def sign(self) -> str:
    return encodeBytes(self.__private.sign(strToBytes(self.__message), ec.ECDSA(hashes.SHA256()))).decode("utf-8")

  """
  Parameters
  ----------
  sig : str
    signature to verify

  Returns : bool
  -------
  True of False depending if verification passes
  """
  def verify(self, sig: str) -> bool:
    try:
      self.__public.verify(decodeBytes(sig.encode("utf-8")), strToBytes(self.__message), ec.ECDSA(hashes.SHA256()))
      return True
    except InvalidSignature:
      return False 