

scoreFile = open('score.txt', 'w', encoding='utf8')

print("국어 : 100", file = scoreFile )
print("영어 : 90", file = scoreFile )

scoreFile.close()

scoreFile = open('score.txt', 'a', encoding='utf8')
scoreFile.write("수학 : 85\n")
scoreFile.write("사회 : 95\n")

scoreFile.close() 

scoreFile = open('score.txt', 'r', encoding='utf8')
print(scoreFile.read())
scoreFile.close()

scoreFile = open('score.txt', 'r', encoding='utf8')
print(scoreFile.readline(), end="")
print(scoreFile.readline(), end="")
print(scoreFile.readline(), end="")
print(scoreFile.readline(), end="")

scoreFile.close()

scoreFile = open('score.txt', 'r', encoding='utf8')
while True :
    line = scoreFile.readline()
    if not line :
        break
    print(line, end="")
scoreFile.close()

scoreFile = open('score.txt', 'r', encoding='utf8')
lines = scoreFile.readlines()

for line in lines :
    print(line, end="")

scoreFile.close()