import re

class Tamil:
    _str = ""
    _str_arr = []
    length = 0

    vallinam=0
    mellinam=0
    idayinam=0
    sanskrit=0
    uyir=0

    total_characters=0

    punctuators_count = 0
    digits_count = 0


    #uyir_list eluthu
    uyir_list = list('அஆஇஈஉஊஎஏஐஒஓஔஃ')

    #Mei eluthu
    mei_list = ["க","ங","ச","ஞ","ட","ண","த","ந","ப","ம","ய","ர","ல","வ","ழ","ள","ற","ன"]

    #vallinam_list
    vallinam_list = ["க","ச","ட","த","ப","ற"]

    #Mellinam
    mellinam_list = ["ங","ஞ","ண","ந","ம","ன"]

    #Idayinam
    idayinam_list = ["ய","ர","ல","வ","ழ","ள"]

    #Sanskrit letters in tamil
    sanskrit_list = ["ஸ","ஷ","ஜ","ஹ","க்ஷ","ஶ்ரீ","ஶ"]

    #Ascii values for the characters like "்", "ெ", "ோ", "ீ"
    asc = [3021,3006,3007,3008,3009,3010,3014,3015,3016,3018,3019,3020]


    def __init__(self,tamil_word) -> None:
        self._str = tamil_word

        #validate if it has proper tamil format encoding
        if not self.validate():
            raise ValueError("Not a proper Tamil encoding")
        
        #segregate
        self.count_segregate()

        self.total_characters = self.sanskrit+self.mellinam+self.uyir+self.vallinam+self.idayinam

        self.form_array()

        self.set_character_info()
    

    def form_array(self):
        count = 0

        for i in self._str:
            
            if ord(i) in self.asc:
                self._str_arr[count-1] += i
            else:
                self._str_arr.append(i)
                count += 1

        self.length = count


    def validate(self) -> bool:

        if len(self._str) == 0:
            return True

        prev = True if ord(self._str[0]) in self.asc else False

        if prev:
            return False
        
        for i in range(1,len(self._str)):
            if ord(self._str[i]) in self.asc:
                if prev:
                    return False
                prev = True
            
            else:
                prev = False

        return True


    def count_segregate(self):
      #character count
      for x in self._str:
          if x in self.uyir_list:
            self.uyir+=1

          elif x in self.vallinam_list:
            self.vallinam+=1

          elif x in self.mellinam_list:
            self.mellinam+=1

          elif x in self.idayinam_list:
            self.idayinam+=1

          elif x in self.sanskrit_list:
            self.sanskrit+=1


    def set_character_info(self):
        self.digits_count = len(re.findall('[0-9]',self._str))
        
        plist = [",",";",":","/","\\","(",")","[","]","{","}","*","+","-","_","=","@","#","$","%","^","&","*","|","/","~","`","?",".","<",">","'","\"","‘","’"]

        for i in self._str:
            if i in plist:
                self.punctuators_count += 1


    def remove_punctuators(self):
        self.punctuators_count = 0

        plist = [",",";",":","/","\\","(",")","[","]","{","}","*","+","-","_","=","@","#","$","%","^","&","*","|","/","~","`","?",".","<",">","'","\"","‘","’"]
        
        for p in plist:
            self._str = self._str.replace(p,"")

        self.form_array()
        
        return self._str
        

    def remove_digits(self):
        self.digits_count = 0

        nlist = ['0','1','2','3','4','5','6','7','8','9']

        for n in nlist:
            self._str = self._str.replace(n,"")

        self.form_array()
        
        return self._str


    def __str__(self):
        return self._str


    def __len__(self) -> int:
        return self.length


    def __getitem__(self,key):
        if key<self.length:
            return self._str_arr[key]
        else:
            raise ValueError("Index out of bound")


    def __setitem__(self,key,ch):
        #if empty ch remove the index
        if key<self.length:
            if len(ch)<=2:
                if len(ch)==1:
                    if ord(ch) in self.asc:
                        raise ValueError("Not a proper charcter")
                    else:
                        self._str_arr[key] = ch
                        self._str = "".join(self._str_arr)

                else:
                    if (ord(ch[0]) in self.asc and ord(ch[1]) in self.asc) or (ord(ch[0]) not in self.asc and ord(ch[1]) not in self.asc):
                        raise ValueError("Not a valid character")
                    
                    if ord(ch[0]) in self.asc:
                        raise ValueError("Not a valid Tamil Character")
                
                    self._str_arr[key] = ch
                    self._str = "".join(self._str_arr)
            else:
                raise ValueError("Only Character is allowed")
        else:
            raise ValueError("Index Out of Bound")


    def __iter__(self):
        
        for i in self._str_arr:
            yield i

