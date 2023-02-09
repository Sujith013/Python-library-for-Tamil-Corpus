from TamilNLP import Tamil
from TamilNLP import TamilGrammer

tamil_text = "கடளே எனக்கு நல்ல குருவை அடையாளம் காட்டு பாரா தானோ என வேண்டினான் அவனையாடா அழைத்தாய் இதுவே அதாவது அவளாவது"

tamil_text = Tamil.Tamil(tamil_text)

tamil_text.remove_punctuators()
tamil_text.remove_digits()

tamil_grammar = TamilGrammer.TamilGrammer(tamil_text)

print(tamil_grammar.tokenized_words)
print("----------")
print(tamil_grammar.clitics_removed)
print("----------")    
tamil_grammar.identify_gender()
print("----------")    
tamil_grammar.identify_tense()
print("----------")    
tamil_grammar.prepositions()
print("----------")    
tamil_grammar.pronouns()
print("----------")    
tamil_grammar.root_word()
