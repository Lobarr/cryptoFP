import base64

"""
converts string data to bytes
"""
def strToBytes(string):
  return string.encode("utf-8")
"""
encodes bytes data to base64
"""
def encodeBytes(data):
  return base64.b64encode(data)
"""
decodes bytes data from base64
"""
def decodeBytes(data):
  return base64.b64decode(data)
