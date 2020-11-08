sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fr = float(sr)
fh = float(sh)
#xp = float(xh) * float(xr)
#print(fh,fr)
#xp = fh * fr
#print("pay:", xp)
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
 

#python 으로 시급 계산이 가능하다. 이때 시간이 40시간을 넘느냐에 따라서 
#overtime으로 출력되냐 regular가 되는지가 갈린다. mulitya dimension도 이와 비슷하게 프로그래밍을 작성할 수 있다. 
#피드백: 종종 변수선언을 할 때 변수를 알맞게 입력하지 않아서 틀렸다, input의 인자값에 제대로 문자열을 서술해주지 않았다. 

#ex_03_01.py succede!!!!
