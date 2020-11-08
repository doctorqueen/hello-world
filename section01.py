#section01
#오늘은 기본 출력을 해보자  예약어 함수 살펴보기 
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')



# Seperator 옵션 사용 

print('T','E','S','T',sep='')
print('2019','02','29',sep='-')
print('victoria0707','naver.com',sep='@')


# end 옵션 사용
print("Welcome To",end=' ')
print('the black parade',end=' ')
print('piano parade')

#format 사용(매우 중요하다)[],{},()
print('{} and{}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me')#mapping(숫자 별로 할당을 한다는 의미이다. 자연스럽게 이해 될 것이다. format형식으로도 많이 사용한다. )
print("{a} are {b}". format(a='You', b='Me')
#좀더 정확하게 사용 가능
#그러나 format이라는 함수를 안쓰고 사용하고 싶으면 안쓰고 하는 방법이 있는데 상관은 없다. 
#%s: 문자, #d: 정수, %f: 실수
#문자열의 데이터를 정확하게 알려주기 때문에 코딩할 때 매우 정확하다고 할 수 있다. 코딩 따라하면서 이 세가지 정도로 알고 사용, 8진수, 16진수를 사용하게 될 때 필요하다. 
print("%s is favorite number is %d"('mingyoung',7)) #이때 퍼센트를 붙이고 s에는 문자가 오고 %d에는 숫자가 온다. 
#가장 정확한 코딩표현 방법이다/ 이 때 퍼센트를 %f와 %s 에 대해섲 조금더 깊게 코딩을 해보자. 


