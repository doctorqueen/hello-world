sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try: 
    fr = float(sr)
    fh = float(sh)
#xp = float(xh) * float(xr)
#print(fh,fr)
#xp = fh * fr
#print("pay:", xp)
except: 
    print("Error, please enter numeric input functions") #이론: try에서 제대로 된 입력값이 입력되지 않으면 except에 지정된 구문이 출력된다.  
    quit()   #이 quit의 역할은 쓰면은  콘솔에서 잡다한 오류 문장들의 나열들을 보는 것을 줄여줘서 시각적으로 편하다.  
if fh > 40 :
    #print("overtime") 사실 출력문을 쓸 때는 프로그래머들이 주석처리를 한다. 마치 html과 css에서 특유의 방식으로 주석 처리하면서 확인하는 부분이 있듯이
    # 파이썬 작업할 때도 반드시 이렇게 한다. 
    reg = fr * fh
    overtimepay = (fh - 40.0) * (fr * 1.5)
    print(reg, overtimepay)
    final = reg + overtimepay 
else:
    #print("Recular")
    final = fh * fr
print("Pay: ", final)


#1. 프로그래머는 이상한 파일 이름들을 잘 다루어야 한다. 가벼운 파일도 다루어야 하고 명령문을 사용해서 마우스를 쉽게 클릭하는 것 이외에도 할 수 있어야 한다. 
#2. 맞는 파일에서 작업중인지 여러 번확인을 해야 한다. 이상한 웹을 프로그래밍 짜고 있을 수 있으니까 
#경험: 이건 내가 이미 겪었던 일이다. html파일 작업할 때 다른 파일을 작업해서 웹이 실행 안된 경우가 있으니까. 




#깨달은 점: 이론을 이해했어도 이론하고 매칭이 안되면 실기에서 의미가 없다는 사실을 몸소 깨달았다. 그래서 이론은 일단 읽어두고 매칭이 잘 안된다면 억지로 하지 않고 자연스럽게 두고 실기 경험에 집중한다.


#ex_03_02.py already succede!!!!