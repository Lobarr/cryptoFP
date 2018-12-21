import argparse
from src.aes import AES
from src.caesar import Caesar
from src.hasher import Hasher
from src.rsa import RSA
from src.ecdsa import ECDSA
from src.desc import DESC

if __name__ == "__main__":
  with open("banner.txt") as f:
    print(f.read())
  rsa = RSA()
  ecdsa = ECDSA()
  aes = AES()
  while True:
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument("cmd", choices=["quit", "help", "aes", "caesar", "hasher", "rsa", "ecdsa"], help='Command to execute', type=str)
    parser.add_argument("-a", "--arg", help="data to be encrypted", default=None)
    parser.add_argument("-o", "--operation", choices=["encrypt", "decrypt", "verify", "sign", "sha256", "sha512", "md5"], help="operation to perform", default=None)
    parser.add_argument("-k", "--key", choices=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'], help="key/offset for caesar", default=None)
    parser.add_argument("-e", "--extended", help="extended info on function", default=None)
    
    print('\nEnter mode and arguments:\n  Input format: <mode> --a -<arg> --o -<operation> --k -<key for caesar> --e -<y/n>')
    results = parser.parse_args(str(input("> ")).split(' -')) 
    
    if results.cmd == "quit":
      print("Quitting program...")
      break
    elif results.cmd == 'help':
      print(
        "\n\nHelp:\n"
        "----------------------------------------\n"
        "Options for <mode>:\n"
        " - \'quit\'  : quits program\n"
        " - \'help\'  : outputs help info\n"
        " - \'aes\'   : initiates aes \n"
        " - \'caesar\': initiates caesar cipher\n"
        " - \'hasher\': initiates hasher\n"
        " - \'rsa\'   : initiates rsa\n"
        " - \'ecdsa\' : initiates ecdsa\n"
        "----------------------------------------\n"
        "Options for --a -<arg>:\n"
        " - str : any input, converts to string\n"
        "----------------------------------------\n"
        "Options for --o -<operation>:\n"
        " - \'encrypt\' : for aes, caesar, and rsa\n"
        " - \'decrypt\' : for aes, caesar, and rsa\n"
        " - \'sha256\'  : for hasher\n"
        " - \'sha512\'  : for hasher\n"
        " - \'md5\'     : for hasher\n"
        " - \'sign\'    : for ecdsa\n"
        " - \'verify\'  : for ecdsa\n"
        "----------------------------------------\n"
        "Options for --k -<key>:\n"
        " - int, range 1 - 26 : offset for caesar\n"
        "----------------------------------------\n"
        "Options for --e -<y/n>:\n"
        " - \'y\' : prints extended info of <mode>\n"
        " - \'n\' : omits extended info of <mode>\n"
        "----------------------------------------\n"
      )      
    elif results.cmd == "aes":
      if results.operation == "encrypt" and results.arg != None:
        aes.setData(results.arg)       
        aes_desc = DESC(operation=results.operation, extended=results.extended, extdata1=aes.get_key(), extdata2=aes.get_iv(), extdata3=results.arg, extdata4=aes.encrypt())
        aes_desc.AES()
      elif results.operation == "decrypt" and results.arg != None:
        aes_desc = DESC(operation=results.operation, extended=results.extended, extdata1=aes.get_key(), extdata2=aes.get_iv(), extdata3=results.arg, extdata4=aes.decrypt(results.arg))
        aes_desc.AES()
      else:
        print("Please pass data to be encrypted / decrypted in the --arg argument") 
    elif results.cmd == "caesar":
      if results.operation == "encrypt" and results.arg != None:
        caesar = Caesar(ct=results.arg,key=int(results.key))        
        caesar_desc = DESC(operation=results.operation, extended=results.extended, extdata1=caesar.get_key(), extdata3=results.arg, extdata4=caesar.encrypt())
        caesar_desc.Caesar()
      elif results.operation == "decrypt" and results.arg != None:
        caesar = Caesar(ct=results.arg,key=int(results.key))        
        caesar_desc = DESC(operation=results.operation, extended=results.extended, extdata1=caesar.get_key(), extdata3=results.arg, extdata4=caesar.decrypt())
        caesar_desc.Caesar()
      else:
        print("Please pass data to be encrypted / decrypted in the --arg argument and a valid key in the --key argument")
    elif results.cmd == "hasher":
      if results.operation == "sha256" and results.arg != None:
        hasher = Hasher(data=results.arg)        
        hash_desc = DESC(operation=results.operation, extended=results.extended,extdata3=results.arg,extdata4=hasher.SHA256())
        hash_desc.Hasher()
      elif results.operation == "sha512" and results.arg != None:
        hasher = Hasher(data=results.arg)        
        hash_desc = DESC(operation=results.operation, extended=results.extended,extdata3=results.arg,extdata4=hasher.SHA512())
        hash_desc.Hasher()
      elif results.operation == "md5" and results.arg != None:
        hasher = Hasher(data=results.arg)        
        hash_desc = DESC(operation=results.operation, extended=results.extended,extdata3=results.arg,extdata4=hasher.MD5())
        hash_desc.Hasher()
      else:
        print("Please pass data to be hashed in the --arg argument and a valid operation in the --operation argument")
    elif results.cmd == "rsa":
      if results.operation == "encrypt" and results.arg != None:
        rsa.setData(results.arg)     
        rsa_desc = DESC(operation=results.operation, extended=results.extended,extdata1=rsa.publicKey(),extdata2=rsa.privateKey(),extdata3=results.arg,extdata4=rsa.encrypt())
        rsa_desc.RSA()
      elif results.operation == "decrypt" and results.arg != None:     
        rsa_desc = DESC(operation=results.operation, extended=results.extended,extdata1=rsa.publicKey(),extdata2=rsa.privateKey(),extdata3=results.arg,extdata4=rsa.decrypt(results.arg))
        rsa_desc.RSA()
      else:
        print("Please pass data to be encrypted / decrypted in the --arg argument")
    elif results.cmd == "ecdsa":
      if results.operation == "sign" and results.arg != None:
        ecdsa.setMessage(results.arg)       
        ecdsa_desc = DESC(operation=results.operation,extended=results.extended,extdata1=ecdsa.publicKey(),extdata2=ecdsa.privateKey(),extdata3=results.arg,extdata4=ecdsa.sign())
        ecdsa_desc.ECDSA()
      elif results.operation == "verify" and results.arg != None:    
        ecdsa_desc = DESC(operation=results.operation,extended=results.extended,extdata1=ecdsa.publicKey(),extdata2=ecdsa.privateKey(),extdata3=results.arg,extdata4=ecdsa.verify(results.arg))
        ecdsa_desc.ECDSA()
      else:
        print("Please pass data to be signed / verified in the --arg argument")