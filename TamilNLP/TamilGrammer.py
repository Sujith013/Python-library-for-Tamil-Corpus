import nltk
import re

class TamilGrammer:

    #tamil = Tamil()
    tokenized_words = []
    clitics_removed = []
    english_words = {}

    def __init__(self,tamil_text) -> None:

        #check type of tamil_text (pending implementation)
        self.tamil = tamil_text

        self.tokenized_words = nltk.word_tokenize(str(tamil_text))

        self.remove_clitics()
        self.to_english()

    
    def remove_clitics(self):
        words_new = []

        for x in self.tokenized_words:

            last = x[len(x)-1]
            z = ord(last)

            thirdL = x[len(x)-3]
            z1 = ord(thirdL)

            if z1==3006 and z==3006 and len(x)>4: #remove "aada" sounds from the end 
                y = x[0:len(x)-3] + chr(3021)
                words_new.append(y)

            elif (x.endswith("வது") or x.endswith("னது")) and ord(x[len(x)-4]) == 3006 and len(x)>6:
                words_new.append(x[0:len(x)-4] + chr(3021))
                y = "ஆ" + x[-3:]
                words_new.append(y)

            elif z==3006 or z==3015 or z==3019: # aa , ee and o sounds are removed
                y = x[0:len(x)-1] + chr(3021)
                words_new.append(y)
            
            else:
                words_new.append(x)
        
        self.clitics_removed = words_new
    

    def identify_gender(self):
        m=""

        for x in self.clitics_removed:
            y = re.search("தான்|னான்|பான்|றான்|டான்|வான்|ணான்|தேன்|னேன்|பேன்|றேன்|டேன்|வேன்$",x)
            z = re.search("தாள்|னாள்|பாள்|றாள்|டாள்|வாள்|ணாள்|தேள்|னேள்|பேள்|றேள்|டேள்|வேள்$",x)
            
            if len(x)>6:

                if (z!=None):
                    if m=="female" or m=="b":
                        continue
                    elif m=="male":
                        m="b"
                    else:
                        m="female"
                        
                    print(x)

                elif (y!=None):
                    if m=="male" or m=="b":
                        continue
                    elif m=="female":
                        m="b"
                    else:
                        m="male"

                    print(x)
            
            if m=="b":
                break

        if "அவள்" in self.clitics_removed and "அவன்" in self.clitics_removed:
            m="b"
            print("அவள்")
            print("அவன்")


        elif "அவள்" in self.clitics_removed:
            if m=="male":
                m="b"
                print("அவள்")
            else:
                m="female"

        elif "அவன்" in self.clitics_removed:
            if m=="female":
                m="b"
                print("அவன்")
            else:
                m="male"

        if m=="b":
            print("\nBoth the genders have been identified")

        elif m=="male":
            print("\nThe sentence is male specific")

        elif m=="female":
            print("\nThe sentence is female specific")

        else:
            print("\nIt's a gender neutral sentence")

    
    def identify_tense(self):
        m = []
        xy = []

        for x in self.clitics_removed:

            past = re.search("தான்|னான்|டான்|ணான்|தேன்|னேன்|டேன்$",x)
            present = re.search("றாள்|றான்|றேன்$",x)
            future = re.search("பான்|வான்|வாள்|பாள்|பேன்|வேன்$",x)

            if past!=None:
                m.append("p")
                xy.append(x)

            elif present!=None:
                m.append("pr")
                xy.append(x)
            
            elif future!=None:
                m.append("f")
                xy.append(x)

        print(xy)
        print(m)

        fT = max(m,key=m.count)

        if fT=="p":
            print("\nTense : Past")

        elif fT=="pr":
            print("\nTense : Present")

        elif fT=="f":
            print("\nTense : Future")

        else:
            print("\nNo tense can be identified in the sentence")


    def prepositions(self):

        prepositions = ["ல","இல்","உள்ள","உள்ளே","மேல","மேலே","மேல்","அடியில","அடியில்","கீழ","ககீழே","கீழ்"]
        prp_eng = ["in","in","inside","inside","on","on","on","under","under","under","under","under"]

        for x in self.clitics_removed:
            if x in prepositions:
                print(x+" - ",end="")

                z = prepositions.index(x)

                print(prp_eng[z])


    def pronouns(self):
        f = open("./TamilNLP/DataBase/pronouns.txt","r",encoding="utf-8")

        pronouns = f.readlines()

        pr_tamil = []
        pr_eng = []
        tmp = []

        for i in range(len(pronouns)):
            tmp = re.split(" ",pronouns[i])
            pr_tamil.append(tmp[0].rstrip())
            pr_eng.append(tmp[1].rstrip())

        f.close()

        print("The following pronouns have been identified in the sentence\n")

        for x in self.clitics_removed:
            if x in pr_tamil:
                z = pr_tamil.index(x)

                print(pronouns[z],end="")

    
    def to_english(self):

        eng1 = ["a","aa","i","ii","u","uu","e","ee","ai","o","oo","au","aK"]
        eng2 = ["k","nk","c","nc","t","Nn","th","n","p","m","y","r","l","v","z","L","R","N"] 


        for x in self.clitics_removed:
            eg=""

            for y in x:
                if y in self.tamil.uyir_list: 
                    ind = self.tamil.uyir_list.index(y)
                    eg+= eng1[ind]
                
                elif y in self.tamil.mei_list:
                    ind = self.tamil.mei_list.index(y)
                    eg+= eng2[ind]+"a"
                
                elif ord(y)==3021:
                    eg = eg[0:len(eg)-1]
                    continue

                elif ord(y) in self.tamil.asc:
                    ind = self.tamil.asc.index(ord(y))
                    eg = eg[0:len(eg)-1]
                    eg+= eng1[ind]

            self.english_words[x] = eg

    
    def root_word(self):

        f1=open("./TamilNLP/DataBase/Noun.txt","r")
        f2=open("./TamilNLP/DataBase/verb.txt","r")

        nounList = f1.readlines()
        verbList = f1.readlines()

        for i in range(len(nounList)):
            nounList[i] = nounList[i].rstrip()

        for i in range(len(verbList)):
            verbList[i] = verbList[i].rstrip()

        for x in list(self.english_words.values()):
            if x in nounList:
                print(x)
            elif x in verbList:
                print(x)

        f1.close()
        f2.close()
