import re
import nltk
import string
import os

# nltk.download('punkt')


class Tamil:
    _str = ""
    _str_arr = []
    length = 0

    vall=0
    mel=0
    idai=0
    sans=0
    uyirE=0


    #uyir eluthu
    uyir = list('அஆஇஈஉஊஎஏஐஒஓஔஃ')

    #Mei eluthu
    mei = ["க","ங","ச","ஞ","ட","ண","த","ந","ப","ம","ய","ர","ல","வ","ழ","ள","ற","ன"]

    #vallinam
    vallinam = ["க","ச","ட","த","ப","ற"]

    #Mellinam
    mellinam = ["ங","ஞ","ண","ந","ம","ன"]

    #Idayinam
    idayinam = ["ய","ர","ல","வ","ழ","ள"]

    #Sanskrit letters in tamil
    sanskrit = ["ஸ","ஷ","ஜ","ஹ","க்ஷ","ஶ்ரீ","ஶ"]

    #Ascii values for the characters like "்", "ெ", "ோ", "ீ"
    asc = [3021,3006,3007,3008,3009,3010,3014,3015,3016,3018,3019,3020]


    def __init__(self,tamil_word) -> None:
        self._str = tamil_word
        #validate if it has proper tamil format encoding
        if not self.validate():
            raise ValueError("Not a proper Tamil encoding")
        
        #segregate
        self.count_segregate()

        #separating charcters
        count = 0

        for index,i in enumerate(self._str):
            
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


    #incomplete
    def replace(self,ch,new_ch):
        self._str = self._str.replace(ch,new_ch)
        #handle self._str_arr

        return self._str


    def count_segregate(self):
      #character count
      for x in self._str:
          if x in self.uyir:
            self.uyirE+=1

          elif x in self.vallinam:
            self.vall+=1

          elif x in self.mellinam:
            self.mel+=1

          elif x in self.idayinam:
            self.idai+=1

          elif x in self.sanskrit:
            self.sans+=1


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

#Punctuators, signs and symbols and digits
tamil_input= Tamil("ஏதென்சு மிகவும்")

print(tamil_input)
