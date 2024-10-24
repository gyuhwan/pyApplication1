

for count in range(1, 21) :
    with open("{0} 차 회의록.txt".format(count), "w", encoding="utf-8") as proceedFile :
        proceedFile.write( "{0} 주차 보고서\n".format(count))
        proceedFile.write( "부    서 : \n")
        proceedFile.write( "이    름 : \n")
        proceedFile.write( "업무요약 : ")       