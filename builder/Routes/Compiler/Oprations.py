from .Crypto import Encrypt, Decrypt

def list_to_dic(Keys,Values):
    res = {}
    for key in Keys:
        for value in Values:
            res[key] = value
            Values.remove(value)
            break
    return res

def Diciters(obj,key,operation="en",type=list):
    temp = []
    dictemp = {}
    for i in obj:
        if isinstance(i, list):
            change = iters(i,key,operation,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),key,operation,tuple)
            temp.append(change)
        elif isinstance(i, str):
            return Encrypt(i,key)
        elif isinstance(i, set):
            change = iters(list(i),key,operation,set)
            temp.append(change)
        elif isinstance(i, dict):
            change = dict_type(i,key,operation)
            temp.append(change)
        else:
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #................................
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.append(str(i))
            elif ( operation == "org" ) :
                if i.isdigit():
                    temp.append(int(i))
                else:
                    temp.append(i)
                    
    if type is list:
        return temp
    elif type is tuple:
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp



def iters(obj,key,operation="en",type=list):
    temp = []
    dictemp = {}
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,operation,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,operation,tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = iters(list(i),key,operation,set)
                temp.append(change)
            elif isinstance(i, dict):
                change = dict_type(i,key,operation)
                temp.append(change)
            else:
                if ( operation == "en" ) :
                    temp.append(Encrypt(str(i),key)) #................................
                elif ( operation == "de" ) :
                    temp.append(Decrypt(str(i),key))
                elif ( operation == "str" ) :
                    temp.append(str(i))
                elif ( operation == "org" ) :
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
    elif isinstance(obj, tuple):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,operation,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,operation,tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = iters(list(i),key,operation,set)
                temp.append(change)
            elif isinstance(i, dict):
                change = dict_type(i,key,operation)
                temp.append(change)
            else:
                if ( operation == "en" ) :
                    temp.append(Encrypt(str(i),key)) #................................
                elif ( operation == "de" ) :
                    temp.append(Decrypt(str(i),key))
                elif ( operation == "str" ) :
                    temp.append(str(i))
                elif ( operation == "org" ) :
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
    elif isinstance(obj, set):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,operation,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,operation,tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = iters(list(i),key,operation,set)
                temp.append(change)
            elif isinstance(i, dict):
                change = dict_type(i,key,operation)
                temp.append(change)
            else:
                if ( operation == "en" ) :
                    temp.append(Encrypt(str(i),key)) #................................
                elif ( operation == "de" ) :
                    temp.append(Decrypt(str(i),key))
                elif ( operation == "str" ) :
                    temp.append(str(i))
                elif ( operation == "org" ) :
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
                    
    if type is list:
        return temp
    elif type is tuple:
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp

def setiters(obj,key,operation="en",type=set):
    temp = set()
    for i in obj:
        if isinstance(i, tuple):
            change = setiters(i,key,operation,tuple)
            temp.add(change)
        elif isinstance(i, set):
            change = setiters(i,key,operation,set)
            temp.add(change)
        else:
            if ( operation == "en" ) :
                temp.add(i) #................................
            elif ( operation == "de" ) :
                temp.add(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.add(str(i))
            elif ( operation == "org" ) :
                if i.isdigit():
                    temp.add(int(i))
                else:
                    temp.add(i) 
    if type is tuple:
        return tuple(temp)
    elif type is set :
        return set(temp)
    


def dict_type(obj,key,operation="en"):
    temp=[]
    temp1=[]
    keys = obj.keys()
    values = obj.values()
    for i in values:
        if isinstance(i, list):
            change = iters(i,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),tuple)
            temp.append(change)
        elif isinstance(i, set):
            change = iters(list(i),set)
            temp.append(change)
        else:
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.append(str(i))
            elif ( operation == "org" ) :
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
    for i in keys:
        if isinstance(i, list):
            change = iters(i,list)
            temp1.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),tuple)
            temp1.append(change)
        elif isinstance(i, set):
            change = iters(list(i),set)
            temp1.append(change)
        else:
            if(operation == "en" ):
                temp1.append(Encrypt(str(i),key)) # impartent..............
            elif(operation == "de" ):
                temp1.append(Decrypt(str(i),key))
            elif(operation == "str" ):
                temp1.append(str(i))
            elif ( operation == "org" ) :
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
    return list_to_dic(temp1,temp)



class array :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Arrays = []
        self.Key = Key
        self.obj = object
        temp = []
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Arrays = iters(object,Key)

    def add(self,element : object) :
        if isinstance(element, list):
            self.Arrays.append(iters(element,self.Key))
        elif isinstance(element, int):
            self.Arrays.append(Encrypt(str(element),self.Key))
        elif isinstance(element, str):
            self.Arrays.append(Encrypt(element,self.Key))
        elif isinstance(element,tuple):
            self.Arrays.append(tuple(iters(list(element),self.Key)))
        elif isinstance(element,set):
            self.Arrays.append(set(iters(list(element),self.Key)))
        elif isinstance(element,dict):
            self.Arrays.append(dict_type(element,self.Key))

    def extend(self,iterable):
        for i in iterable:
            self.add(i)
    
    def index(self,object):
        if isinstance(object, list):
            obj_string = iters(object,self.Key,"str")
        elif isinstance(object, int):
            obj_string = str(object)
        elif isinstance(object,tuple):
            obj_string = tuple(iters(list(object),self.Key,"str"))
        elif isinstance(object,set):
            obj_string = set(iters(list(object),self.Key,"str"))
        elif isinstance(object,dict):
            obj_string = dict_type(object,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        index_is = orginal.index(obj_string)
        return index_is

    def len(self):
        return len(self.Arrays)

    def clear(self):
        self.Arrays = []
        return self.Arrays
    
    def copy(self):
        return self.Arrays
    

    def to_pyarray(self,key):
        orginal = iters(self.Arrays,key,"de")
        orginal = iters(orginal,key,"org")
        return orginal

    def insert(self,index,object):
        if isinstance(object, list):
            self.Arrays.insert(index,iters(object,self.Key))
        elif isinstance(object, int):
            self.Arrays.insert(index,Encrypt(str(object),self.Key))
        elif isinstance(object, str):
            self.Arrays.insert(index,Encrypt(object,self.Key))
        elif isinstance(object,tuple):
            self.Arrays.insert(index,tuple(iters(list(object),self.Key)))
        elif isinstance(object,set):
            self.Arrays.insert(index,set(iters(list(object),self.Key)))
        elif isinstance(object,dict):
            self.Arrays.insert(index,dict_type(object,self.Key))

    def count(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        count_is = orginal.count(obj_string)
        return count_is
    
    def remove(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        orginal.remove(obj_string)
        self.Arrays = iters(orginal,self.Key,"en")
    
    def reverse(self):
        self.Arrays = self.Arrays[::-1]
    
    def sort(self,key=False,reverse=False):
        obj_string = self.to_pyarray(self.Key)
        if key and reverse :
            self.Arrays = obj_string.sort(key,reverse)
        elif reverse:
            self.Arrays = obj_string.sort(reverse)
        elif key:
            self.Arrays = obj_string.sort(key)
        else:
            self.Arrays = obj_string.sort()
    
    def pop(self,index):
        self.Arrays.pop(index)

    def __str__(self) -> str:
        return str(self.Arrays)

    def __repr__(self) -> str:
        return "CryptoArray"


class Dict :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Dict = dict()
        self.Key = Key
        self.obj = object
        temp = dict()
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Dict = dict_type(object,Key)
    
    def add(self,key,value):
        self.Dict[Encrypt(key,self.Key)] = Encrypt(value, self.Key)
    
    def clear(self):
        self.Dict = dict()
    
    def copy(self):
        return self.Dict
    
    def to_pyDict(self,key):
        orginal_str = dict_type(self.Dict,key,"de") 
        orginal = dict_type(orginal_str,key,"org")
        return orginal

    def get(self,key,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.get(key)
        else:
            return Encrypt(str(orginalDic.get(key)),self.Key)

    def items(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.items()
        else:
            return Diciters(orginalDic.items(),self.Key)
            
    def keys(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.keys()
        else:
            return Diciters(orginalDic.keys(),self.Key)
    
    def values(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.values()
        else:
            return Diciters(orginalDic.values(),self.Key)
    
    def setdefault(self,keyname, value, security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.setdefault(keyname,value)
        else:
            return Diciters(orginalDic.setdefault(keyname,value),self.Key)
    
    def popitem(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        org = list(orginalDic.popitem())
        self.Dict = dict_type(orginalDic,self.Key,"en")
        encry = iters(org,self.Key)
        if security_key and security_key == self.Key:
            return org
        else:
            return encry
        
    def pop(self,key_value,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        orginalDic.pop(key_value)
        self.Dict = dict_type(orginalDic,self.Key,"en")
    

    def from_keys(self,key,value=False,security_key=False):
        if value:
            fromdic_ = dict.fromkeys(key,value)
        else:
            fromdic_ = dict.fromkeys(security_key)
        returntype = dict_type(fromdic_,security_key)
        return returntype


    def __str__(self) -> str:
        return str(self.Dict)

    def __repr__(self) -> str:
        return "CryptoSet"
    
class Tuple :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Tuple = tuple()
        self.Key = Key
        self.obj = object
        temp = tuple()
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Tuple = tuple(iters(object,Key))
    
    def count(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Tuple,self.Key,"de")
        count_is = orginal.count(obj_string)
        return count_is
    
    def index(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Tuple,self.Key,"de")
        count_is = orginal.index(obj_string)
        return count_is

    def to_pytuple(self,key):
        orginal = iters(self.Tuple,key,"de")
        orginal = iters(orginal,key,"org")
        return tuple(orginal)

        
            
    def __str__(self) -> str:
        return str(self.Tuple)

    def __repr__(self) -> str:
        return "CryptoTuple"
    
class Set :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Set = set()
        self.Key = Key
        self.obj = object
        temp = set()
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Set = set(iters(object,Key))
    def copy(self):
        return self.Set
            
    def add(self,element : object) :
        if isinstance(element, list):
            self.Set.add(iters(element,self.Key))
        elif isinstance(element, int):
            self.Set.add(Encrypt(str(element),self.Key))
        elif isinstance(element, str):
            self.Set.add(Encrypt(element,self.Key))
        elif isinstance(element,tuple):
            self.Set.add(tuple(iters(list(element),self.Key)))
        elif isinstance(element,set):
            self.Set.add(set(iters(list(element),self.Key)))
        elif isinstance(element,dict):
            self.Set.add(dict_type(element,self.Key))
    
    def to_pyset(self,key):
        orginal = iters(self.Set,key,"de")
        orginal = iters(orginal,key,"org")
        return set(orginal)
    
    def clear(self):
        self.Set = set()
        return self.Set
    
    def remove(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Set,self.Key,"de")
        orginal.remove(obj_string)
        self.Set = iters(orginal,self.Key,"en")
    
    def discard(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = set(iters(self.Set,self.Key,"de"))
        orginal.discard(obj_string)
        self.Set = iters(orginal,self.Key,"en")

    def difference(self,sets,security_key=False):
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.difference(sets)
        else:
            return set(iters(orginal.difference(sets),self.Key))
    
    def symmetric_difference(self,sets,security_key=False): 
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.symmetric_difference(sets)
        else:
            return set(iters(orginal.symmetric_difference(sets),self.Key))
        
    def issuperset(self,sets,security_key=False): 
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.issuperset(sets)
        else:
            return iters(orginal.issuperset(sets),self.Key)
    
    def issubset(self,sets,security_key=False): 
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.issubset(sets)
        else:
            return iters(orginal.issubset(sets),self.Key)

    def isdisjoint(self,sets,security_key=False): 
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.isdisjoint(sets)
        else:
            return iters(orginal.isdisjoint(sets),self.Key)

    def intersection(self,*argv,security_key=False):
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        if security_key and security_key == self.Key:
            return orginal.intersection(argv)
        else:
            return set(iters(orginal.intersection(argv),self.Key))
        
    def difference_update(self,sets):
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        orginal.difference_update(sets)
        self.Set = set(iters(orginal,self.Key))
    
    def update(self,sets):
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        orginal.update(sets)
        self.Set = set(iters(orginal,self.Key))
    
    def symmetric_difference_update(self,sets):
        orginal = iters(self.Set,self.Key,"de")
        orginal = set(iters(orginal,self.Key,"org"))
        orginal.symmetric_difference_update(sets)
        self.Set = set(iters(orginal,self.Key))
    
    def pop(self):
        return self.Set.pop()
        
    def __str__(self) -> str:
        return str(self.Set)

    def __repr__(self) -> str:
        return "CryptoSet"


class String :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.String = str()
        self.Key = Key
        self.obj = object
        temp = str()
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.String = Encrypt(object,Key)
    
    def capitalize(self,security_key=False): 
        String = Decrypt(self.String,self.Key).capitalize()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
    
    def upper(self,security_key=False): 
        String = Decrypt(self.String,self.Key).upper()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def lower(self,security_key=False): 
        String = Decrypt(self.String,self.Key).lower()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def swapcase(self,security_key=False): 
        String = Decrypt(self.String,self.Key).swapcase()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
    
    def title(self,security_key=False): 
        String = Decrypt(self.String,self.Key).title()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def casefold(self,security_key=False): 
        String = Decrypt(self.String,self.Key).casefold()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def istitle(self,security_key=False): 
        String = Decrypt(self.String,self.Key).istitle()
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(str(String),self.Key)
        
    def zfill(self,len,security_key=False): 
        String = Decrypt(self.String,self.Key).zfill(len)
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def strip(self,character,security_key=False): 
        String = Decrypt(self.String,self.Key).strip(character)
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
        
    def center(self,length, character=False,security_key=False): 
        if character == True:
            String = Decrypt(self.String,self.Key).center(length, character)
        else:
            String = Decrypt(self.String,self.Key).center(length)
        if security_key and security_key == self.Key:
            return String
        else:
            return Encrypt(String,self.Key)
    def split(self,separator, maxsplit=False,security_key=False): 
        if maxsplit == True:
            String = Decrypt(self.String,self.Key).split(separator, maxsplit)
        else:
            String = Decrypt(self.String,self.Key).split(separator)
        if security_key and security_key == self.Key:
            return String
        else:
            return iters(String,self.Key) 
    
    def isalnum(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isalnum()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isalpha(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isalpha()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isascii(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isascii()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isdecimal(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isdecimal()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isdigit(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isdigit()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isidentifier(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isidentifier()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def islower(self,security_key=False): 
            String = Decrypt(self.String,self.Key).islower()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isnumeric(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isnumeric()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isprintable(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isprintable()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    def isspace(self,security_key=False): 
            String = Decrypt(self.String,self.Key).isspace()
            if security_key and security_key == self.Key:
                return String
            else:
                return Encrypt(str(String),self.Key)
    
    def find(self,value,start=False,end=False):
        if start == False and end == False :
            String = Decrypt(self.String,self.Key).find(value)
        elif end == False :
            String = Decrypt(self.String,self.Key).find(value,start)
        if start == False and end == False :
            String = Decrypt(self.String,self.Key).find(value,start,end)
        return String
    
    
    # def count(self,value, start=False, end=False,security_key=False): 
    #     str_ = 0
    #     if start and end :
    #         str_ = (Decrypt(self.String,self.Key)).count(value,start,end)
    #     elif start:
    #         str_ = (Decrypt(self.String,self.Key)).count(value,start)
    #     elif start:
    #         str_ = (Decrypt(self.String,self.Key)).count(value)
    #     print(Decrypt(self.String,self.Key))
    #     if security_key and security_key == self.Key:000
    #         return str_
    #     else:
    #         return Encrypt(str(str_),self.Key)

    def __str__(self) -> str:
        return str(self.String)

    def __repr__(self) -> str:
        return "CryptoString"
    

