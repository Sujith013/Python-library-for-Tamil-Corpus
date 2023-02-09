from TamilNLP import Tamil
from TamilNLP import TamilGrammer

tamil_text = "ஏதென்சு, () ஆகயால் [மிகவும் ]பிரபலமான பண்டைய கிரேக்க சனநாயக நகர அரசு என்றாலும், இதுவே முதல் சனநாயக அரசு அல்ல; ஏதென்சுக்கு முன் பல நகர அரசுகள் இதேபோன்ற சனநாயக அரசியலமைப்பை ஏற்றுக்கொண்டிருந்தன. கிமு 4 ஆம் நூற்றாண்டின் பிற்பகுதியில்"

tamil_text = Tamil.Tamil(tamil_text)

print(tamil_text.uyir)
print("---")
print(tamil_text.mellinam)
print("---")
print(tamil_text.vallinam)
print("---")
print(tamil_text.idayinam)
print("---")
print(tamil_text.sanskrit)
print("---")
print(tamil_text.total_characters)
    

