from random import choice
from data.Create import Datas
import string
import base64
from typing import NewType,Union

# auto encode and decode

# NewTyping
EncryptedStr : NewType = NewType('EncryptedStr',str)
DecryptedStr : NewType = NewType('DecryptedStr',str)

def Encrypt( String : str, key : str ) -> EncryptedStr :
    count : int = 0
    Encrypt : str = str()
    EncryptedString : str = str()
    KeyString : str = key + '#' + String
    for i in KeyString :
        EndSymbols : list = ['#','^']
        SymbolSetOne : list = ['~','!']
        SymbolSetTwo : list = ['^','$','&','_','+']
        Randoms : int = choice([ x for x in range(8) ])
        Encrypt : list = Datas.get(i)
        ran : int = choice([ i for i in range(len(Encrypt))])
        if(Randoms > 9):
            EncryptedString : EncryptedStr = EncryptedString + choice(SymbolSetOne) + str(Randoms)+Encrypt[ran]
        else:
            EncryptedString : EncryptedStr = EncryptedString + choice(SymbolSetTwo) + str(Randoms)+Encrypt[ran]
    return EncryptedString


def Decrypt(Encrypted,key) -> DecryptedStr :
    SymbolSetOne : list = ['#','~','!']
    SymbolSetTwo : list = ['^','$','&','_','+']
    encoded : list = []
    count : int = 0
    clue : list = []
    index_ : list = []
    MagicKeys = list(string.ascii_letters + string.digits + """@%*`!# }{[])(~//|?><,.:;~$^&=+-_'" """)
    #fetching Length of clue string
    for i,x in enumerate(Encrypted):
        if(x in SymbolSetTwo):
            encoded.append(int(Encrypted[i+1]))
        elif(x in SymbolSetOne):
            encoded.append(int(Encrypted[i+1:i+3]))
    #Finding main symboles index
    for i,x in enumerate(list(Encrypted)):
        if(x in SymbolSetTwo or x in SymbolSetOne):
            index_.append(i)
            count : int = count + 1
    #spliting finded index
    parts : list = [Encrypted[i:j] for i,j in zip(index_, index_[1:]+[None])]

    # Fetching datas from clue
    for i,x in enumerate(parts):
        length : int = len(str(encoded[i]))
        clue.append(x[length+1:])
    String : str = ""
    for i in clue :
        for j in MagicKeys:
            if i in Datas.get(j):
                String : str = String + j
    SplitHash : str = String.split("#")
    if(SplitHash[0] == key):
        return String.split("#")[-1]


def KeyEncrypt(String : str) -> EncryptedStr :
    count : int = 0
    Key : list = []
    Encrypt : str = str()
    EncryptedString : str = str()
    for i in String :
        SymbolSetOne : list[str] = ['#','~','!']
        SymbolSetTwo : list[str] = ['^','$','&']
        Randoms : list[int] = choice([ x for x in range(8) ])
        Encrypt : list[str] = Datas.get(i)
        ran : int = choice([ i for i in range(len(Encrypt))])
        if(Randoms > 9):
            EncryptedString : EncryptedStr = EncryptedString + choice(SymbolSetOne) +str(Randoms)+Encrypt[ran]
        else:
            EncryptedString : EncryptedStr  = EncryptedString + choice(SymbolSetTwo) +str(Randoms)+Encrypt[ran]
    for i,x in enumerate(EncryptedString):
        if(x in SymbolSetTwo or x in SymbolSetOne):
            Key.append(str(i))
            count : int = count + 1
    return EncryptedString, "".join(Key)

def Keydecrypt(Encrypted,key) -> DecryptedStr :
    SymbolSetOne = ['#','~','!']
    SymbolSetTwo = ['^','$','&']
    encoded = []
    count = 0
    clue = []
    index_ = []
    MagicKeys = list(string.ascii_letters + string.digits + """@%*`!# }{[])(~//|?><,.:;~$^&=+-_'" """)
    #fetching Length of clue string
    for i,x in enumerate(Encrypted):
        if(x in SymbolSetTwo):
            encoded.append(int(Encrypted[i+1]))
        elif(x in SymbolSetOne):
            encoded.append(int(Encrypted[i+1:i+3]))
    #Finding main symboles index
    for i,x in enumerate(list(Encrypted)):
        if(x in SymbolSetTwo or x in SymbolSetOne):
            index_.append(i)
            count=count+1
    #spliting finded index
    parts = [Encrypted[i:j] for i,j in zip(index_, index_[1:]+[None])]

    # Fetching datas from clue
    for i,x in enumerate(parts):
        length = len(str(encoded[i]))
        clue.append(x[length+1:])
    KeyCheck = False
    strindex = [str(i) for i in index_]
    String = ''
    cluekey="".join(strindex)
    if key == cluekey:
        String = ""
        for i in clue :
            for j in MagicKeys:
                if i in Datas.get(j):
                    String = String + j
    return String



#encode
def FileEncrypt(FilePath : str,Key : str, FileToSave : str = False ) -> Union[str,EncryptedStr] :
    ReadFile : file = open(FilePath,"rb")
    B64encoded  = base64.b64encode(ReadFile.read())
    Cryptted  = ''
    KeyValue = sum([ ord(x) for x in Key ])
    EncodeTo = choice([1,2,3])
    for i in str(B64encoded):
        if(EncodeTo == 1):
            Cryptted = Cryptted + hex(ord(i)+KeyValue)
        elif(EncodeTo == 2):
            Cryptted = Cryptted + oct(ord(i)+KeyValue)
        elif(EncodeTo == 3):
            Cryptted = Cryptted + bin(ord(i)+KeyValue)
    if FileToSave:
        with open(FileToSave + FilePath.split('\/')[-1]) as file :
            file.write(Cryptted)
        file.close()
    else:
        return Cryptted
#decode
def FileDecrypt(Encrypted : str,Key : str, FileToSave : str ) -> DecryptedStr :
    convertKey = 0
    if(Encrypted[0:2] == '0x' ):
        convertKey = 0
        decode = ("~0x".join(Encrypted.split('0x'))).split("~")[1:]
    elif(Encrypted[0:2] == '0o' ):
        convertKey = 1
        decode = ("~0o".join(Encrypted.split('0o'))).split("~")[1:]
    elif(Encrypted[0:2] == '0b' ):
        convertKey = 2
        decode = ("~0b".join(Encrypted.split('0b'))).split("~")[1:]
    img=''
    KeyValue = sum([ ord(x) for x in Key ])
    try:
        for i in decode:
            if(convertKey == 0):
                img = img + chr(int(i,16)-KeyValue)
            elif(convertKey == 1):
                img = img + chr(int(i,8)-KeyValue)
            elif(convertKey == 2):
                img = img + chr(int(i,2)-KeyValue)

        with open(FileToSave,"wb") as img1:
            img1.write(base64.b64decode(bytes(img,'utf-8')[2:-1]))
        img1.close()
    except:
        print("Key is invalid")

#============================================================================================================

def BaseEncrypt(String : str,Key : str, Base : int):
    Choice = choice([1,2,3,4])
    Cryptted = str()
    for i in str(String+Key+str(len(Key))):
       if(Base == 16):
           Cryptted = Cryptted + hex(ord(i) + Choice)
       elif(Base == 8):
           Cryptted = Cryptted + oct(ord(i) + Choice)
       elif(Base == 2):
           Cryptted = Cryptted + bin(ord(i) + Choice)
    return Cryptted


def easyEncrypt(String : str, Key : str,OnlyNormalChar = False) -> EncryptedStr :
    Choice = choice([1,2,3])
    encrypt = str()
    type_ = ""
    if not OnlyNormalChar :
        if Choice == 1 :
            len_of_str = choice([1,2,3,4])
            for i in String[::-1]:
                if (i.isdigit()):
                    encrypt = encrypt + "~" + chr(ord(i)+len_of_str) +"~"
                else:
                    encrypt = encrypt + chr(ord(i)+len_of_str)
            type_ = "\l"+str(len_of_str)
        elif Choice == 2 :
            len_of_str = choice([1,2,3,4])
            for i in String:
                if (i.isdigit()):
                    encrypt = encrypt + "~" + chr(ord(i)+len_of_str) +"~"
                else:
                    encrypt = encrypt + chr(ord(i)+len_of_str)
            type_ = "\q"+str(len_of_str)
            
        elif Choice == 3 :
            len_of_str = choice([1,2,3,4])
            for i in String:
                if (i.isdigit()):
                    encrypt = encrypt + "~" + chr(ord(i)-len_of_str) +"~"
                else:
                    encrypt = encrypt + chr(ord(i)-len_of_str)
            type_ = "\s"+str(len_of_str)
            
            
        encrypt_len = choice([ x for x in range(len(encrypt))])
        find_clue = ["\l","\q","\s","\h"]
        encrypt = encrypt[:encrypt_len]+ type_ +encrypt[encrypt_len:]
        return encrypt

    else :
        len_of_str = len(Key)
        for i in String:
            encrypt = encrypt + chr(ord(i)+Choice)
        return encrypt + "~"*Choice

def easyDectypt( Encryptedobj : object, Key ):
    output = ""
    find_clue = ["\l","\q","\s","\h"]
    find_clue_1 = ["\\l","\\q","\\s","\\h"]
    clue_is = 0
    for i,x in enumerate(find_clue_1):
        if x in Encryptedobj:
            clue_is = i
    find_str = Encryptedobj.split(find_clue_1[clue_is])
    clue = find_str[0] + find_str[1][1:]
    L_trigger = False
    if "~" in clue:
        split_sy = clue.split("~")
        for j in split_sy:
            if j.isdigit():
                if(find_clue[clue_is] == "\l"):
                    L_trigger = True
                    length = int(find_str[1][0])
                    output = output + chr(ord(j)-length)
                elif(find_clue[clue_is] == "\s"):
                    length = int(find_str[1][0])
                    output = output + chr(ord(j)+length)
                elif(find_clue[clue_is] == "\q"):
                    length = int(find_str[1][0])
                    output = output + chr(ord(j)-length)
            else:
                if(find_clue[clue_is] == "\l"):
                    clue = j
                    length = int(find_str[1][0])
                    for i in clue:
                        output = output + chr(ord(i)-length)
                elif(find_clue[clue_is] == "\q"):
                    clue = j
                    length = int(find_str[1][0])
                    for i in clue:
                        output = output + chr(ord(i)-length)
                elif(find_clue[clue_is] == "\s"):
                    clue = j
                    length = int(find_str[1][0])
                    for i in clue:
                        output = output + chr(ord(i)+length)
    else:
        if(find_clue[clue_is] == "\s"):
            length = int(find_str[1][0])
            for i in clue:
                output = output + chr(ord(i)+length)
            
        elif(find_clue[clue_is] == "\q"):
            length = int(find_str[1][0])
            for i in clue:
                output = output + chr(ord(i)-length)
            
        elif(find_clue[clue_is] == "\l"):
            clue = clue[::-1]
            length = int(find_str[1][0])
            for i in clue:
                output = output + chr(ord(i)-length)
    if L_trigger:
        return output[::-1]
    else:
        return output



# print(easyEncrypt("hello","keys",True))
# print(BaseEncrypt("hello","key",8))
