from TamilNLP import Tamil
from TamilNLP import TamilGrammer

tamil_text = "ஏதென்சு மிகவும் பிரபலமான பண்டைய கிரேக்க சனநாயக நகர அரசு என்றாலும், இதுவே முதல் சனநாயக அரசு அல்ல; ஏதென்சுக்கு முன் பல நகர அரசுகள் இதேபோன்ற சனநாயக அரசியலமைப்பை ஏற்றுக்கொண்டிருந்தன. கிமு 4 ஆம் நூற்றாண்டின் பிற்பகுதியில்"

for i in tamil_text:
    print(i)

tamil_text = Tamil.Tamil(tamil_text)
print("-----------------")
for i in tamil_text:
    print(i)

