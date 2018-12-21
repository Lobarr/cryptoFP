from src.helpers import strToBytes, encodeBytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class Hasher:
  """
  A class for hashing string data

  Parameters
  ----------
  data : str
    data to be encrypted 
  """
  def __init__(self, data):
    self.__data = data
  """
  Returns : str
  -------
  SHA256 hash of data
  """
  def SHA256(self):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(strToBytes(self.__data))
    return encodeBytes(digest.finalize()).decode("utf-8")
  """
  Returns : str
  -------
  SHA512 hash of data
  """
  def SHA512(self):
    digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
    digest.update(strToBytes(self.__data))
    return encodeBytes(digest.finalize()).decode("utf-8")
  """
  Returns : str
  -------
  MD5 hash of data
  """
  def MD5(self):
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(strToBytes(self.__data))
    return encodeBytes(digest.finalize()).decode("utf-8")