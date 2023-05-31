print(True)
print(False)
sav1 = True
sav2 = False
sav3 = 0

name = '1분'
_name = 'tt'

print(_name)
# 변수 이름은 숫자로 시작할 수 없거나 특정 특수문자는 사용할 수 없다

#형 변환

sav = '22'
sav4 = '11'
sav5 = 'two'
kaka = '3.14'
int(sav4)
float(sav)
str(sav5)
#문자형태의 실수를 정수로 변환할려면 우선 실수로 변환한 뒤 정수로 변환해야됨
int(float(kaka))
# 정수로 변환
int()
# 실수로 변환 (ex:1.0)
float()
# 문자로 변환
str()

#연산자

# %는 나머지 예시 print(5%2) 5를 2로 나눴을 때 나머지 값이 나옴 실행결과 1
print(5%2)

# //는 몫, 예시 print(5//2) 5를 2로 나눴을 때의 몫, 실행결과 2
print(5//2)

# **는 거듭 제곱(제곱), 예시 print(5**2) 실행결과 25
print(5**2) 

# 비교 연산자는 >, <, >=, <=가 있다. 결과는 불리안 형태로 True, False로 나옴
# ==는 같다, !=는 같지 않다를 의미함

#논리 연산자

#and는 둘다 참이면이라는 뜻으로 
print(5 > 7 and 5 > 2)
#7이 5보다 크기 때문에 둘 다 참이 아니여서 실행 시 False가 결과로 나옴

#or는 하나라도 참이면 이라는 뜻으로
print(5 > 7 or 5 > 2)
#5가 2보다 크기 때문에 두 명제 중 하나가 참이여서 True로 실행됨

#not은 반전을 의미하며 어떤 값을 반전시킴
print(not 3 < 5)
#5가 3보다 크지만 not을 했기 때문에 반전되어 False 값이 나옴

#멤버 연산자(멤버인지 아닌지를 확인할 수 있는 연산자)

#in은 어떤 값 안에 멤버가 포함됐는지 확인 하는 것
print('c' in 'cat')
#cat 안에 c가 들어 있기 때문에 True 값이 나옴

# not in은 미포함을 의미하며 어떤 값 안에 멤버가 없는지를 확인하는 것
print('c' not in 'cat')
#cat 안에 c가 들어 있기 때문에 False 값이 나옴

#불리안
#bool() 코드로 불리안 형태로 변경할 수 있음
#이때 값이 있으면 True로 없으면 False로 판단함
#문자 자료형의 경우

a = 'hello' # 값이 있음
b = '     ' # 따옴표 안에 공백이 있기 때문에 값이 있음
c = '' # 따옴표 안에 아무것도 없기 때문에 값이 없음
bool(a)
a

#숫자의 경우 0이 아닌 모든 수는 True, 0은 False가 됨

a1 = 1 #값이 있음
b1 = -1 #값이 있음
c1 = 0 #값이 없음

bool(c1)

#파이썬에서 None은 값이 없음을 의미하는데 이 역시 불리안 형 변환을 할 경우 False로 나옴
bool(None)

print('신랑 신부 입장')
# 한줄 주석은 샵을 사용
print('큰 박수 부탁드립니다.')

#여러 줄의 주석은 ''','''를 이용한다
print('신랑 신부 입장')
'''걷기 시작하고
잠시 후에'''
print('큰 박수')

#인덱스 값의 특정 부분을 불러옴 파이썬의 문자열은 0부터 시작
langss = 'PYTHON'
print(langss[0]) # PYTHON의 첫번째 값인 P를 부름
#마지막을 부를 때는 -1를 넣으면 됨 -1에서 -2, -3으로 하면 문장의 역순으로 불러옴

#슬라이싱은 특점 범위를 정해서 불러오는 것을 의미함
print(langss[0:5]) #첫 번째부터 5전 직전까지 가져옴
print(langss[1:6])
print(langss[1:])#맨 앞을 비우면 첫번째 부터 맨 뒤를 비우면 앞에 설정한 값 이후로 끝까지 불러옴
print(langss[:])#처음부터 끝까지 가지고 오려면 인덱스 없이 작성하면 됨

#문자열 처리

snack = "꿀꽈배기"
two = '2개'

juseyo = snack + two
juseyo
# 여기다 꿀꽈배기2개 주세요라는 말을 만들기 위해서 해당 방법을 써도 되지만
juseyo = juseyo + '주세요'
juseyo
# juseyo 변수가 2번 쓰여서 코드가 예쁘지 않음 이때 +=를 써서 표현할 수 있음
# juseyo 변수에다가 '주세요'라는 글자를 더한 값을 juseyo 변수에 넣겠다는 뜻
juseyo += '주세요'
juseyo

#문자만이 아닌 다른 자료형에서도 가능
num = 3
num += 2
num

#더하기만이 아닌 다른 연산자도 가능
num = 4
num -= 2
num

#문자열의 길이를 구하는 방법

snack = '꿀꽈배기'

# 길이를 의미하는 len()을 사용하면 알 수 있음
print(len(snack))

#여러줄 문자를 변수선언 할때
snack = '''꿀꽈배기는
너무
맛있어요'''
snack

#메소드란 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음을 의미
#문자열 메소드의 형태는 문자열.메소드()

letter = 'how are YOU?'
#해당 문자열 전체를 소문자로 바꾸려고 한다면
print(letter.lower())

#문자열 전체를 대문자로 바꾸려고 한다면
print(letter.upper())

#첫글자만 대문자로 바꾸고 싶다면
print(letter.capitalize())

#각 단어들의 첫 글자만 대문자로
print(letter.title())

#문자열의 대소문자를 뒤바꾸려면
print(letter.swapcase())

#문자열을 나누려면 split을 사용, 결과로는 띄어쓰기 기준으로 리스트 형태로 반환함
print(letter.split())

# 문자열 내에서 어떤 글자가 몇 번 쓰였는지 확인하려면 count 메소드 사용
print(letter.count('how'))

s = '나도고등학교'

# 문자열의 시작이 '나도'인지 확인하려면
print(s.startswith('나도'))
# 실행 시 맞으면 True 값이 나옴

# 문자열이 어떤 값으로 끝나는지 확인하려면
print(s.endswith('초등학교'))
# s의 문자열 마지막은 고등학교여서 False 형태로 나옴

s = '...나도고등학교...'

# 문자열 앞뒤로 불필요한 부분이 있을 경우
print(s.strip('.'))
#strip('') 괄호 안 따옴표에 제거할 문자를 넣으면 제거됨, 괄호 안에 아무것도 없을 경우 문자열 앞뒤로 불필요한 공백 제거

# 문자열 일부를 변경하려면
print(s.replace('고등학교','고교'))
'''replace 괄호안에 ('변경을 원하는 문장','바꾸려는 문장) 형식으로 작성''' 

s = '나도고등학교'

# 특정 글자가 어디 있는지 확인하려면
print(s.find('학교'))
# 인덱스 기준으로 어느 위치에 있는지 알려줌

# 다른 문자들 사이에 가운데로 넣고 싶다면
print(s.center(10,'-'))
# center("인덱스 기준으로 늘어날 숫자",'넣고 싶은 문자') 형태로 작성

# 문자열 포맷

python = '파이썬'

java = '자바'

#어떤 변수를 동시에 출력하여 문자열을 만들 때 

print('개발 언어에는 {}, {}가 있어요'.format(python, java))
''' 문자열 중 추가할 부분에 중괄호 삽입하고 .format(변수명1,변수명2) 형식으로
작성하면 순서대로 삽입됨'''

# 중괄호 안에 숫자를 넣어서 순서를 정할 수 있음
print('개발 언어에는 {1}, {0}가 있어요'.format(python, java))

# f-string python 3.6 이상 부터 가능하며
print(f'개발 언어에는 {python}과 {java}가 있어요')
# 문자열 앞에 f 작성 후 중괄호 안에 변수 삽입

# 15. 탈출 문자(역슬래시\와 특정 문자나 숫자의 조합으로 표현할 수 없는 기능이나 문자를 표시)
print("나는 속으로 '엄청 어려운데'라고 생각 했다.")
# 큰 따옴표는 \" 작은 따옴표는 \'
print ('나는 속으로 \'엄청 어려운데\'라는 생각에 \"엄청 쉽지\"라고 했다')
'''문자열 안에 큰따옴표와 작은 따옴표 모두 사용되는 경우 해당 방법을 이용'''

'''폴더 주소 사용 시 \가 에러날 경우 \\를 사용한다'''

# 문자열의 줄을 바꿀 때는 \n을 사용

snack = '꿀꽈\n배기는\n엄청처언처너처'
print(snack)

# 16. 리스트
'''파이썬에서는 여러 개의 데이터를 한꺼번에 관리하기 위한
내장 자료형을 제공함 그 중 하나가 리스트
변수가 하나의 값만 저장한다면 리스트는 여러 개의 값을 저장할 수 있음
대괄호 안에 값을 넣으며 ,(콤마)로 구분함'''

my_list = ['오예스', '몽쉘', '초코파이','초코파이','초코파이'] #리스트에는 중복 허용
# 리스트에는 문자, 정수, 실수, 불리안 같은 아무 값이나 섞어 넣을 수 있음
# 빈 리스트 생성하고 싶은 경우 대괄호를 비우면 됨

# 리스트의 인덱스에 해당하는 값을 보고 싶을 경우, 리스트의 값은 순서가 보장됨
print(my_list[0])

# 때문에 리스트의 슬라이싱도 가능함
print(my_list[0:2])

# 리스트의 어떤 값이 포함됐는지 볼려면
print('몽쉘' in my_list)
print('가나' not in my_list)

# 리스트 값의 갯수를 보고 싶으면
print(len(my_list))


# 리스트의 값을 수정하고 싶으면
my_list[1] = '몽쉘카카오'
print(my_list)

# 리스트의 맨 뒤에 값을 추가하고 싶으면
my_list.append('빅파이')
print(my_list)

# 리스트의 값을 삭제하려면?
my_list.remove('오예스')
print(my_list)

# 다른 리스트와 합치려면?
my_list = ['오예스', '몽쉘', '초코파이']
your_list = ['빅파이', '오뜨']
'''extend() 메소드를 사용하면 리스트가 확장됨'''
my_list.append(your_list)
print(my_list)

'''
리스트 메소드
insert() 원하는 위치에 값 추가 사용법 (변수.insert(x,y)) x는 위치 y는 추가하고 싶은 값
pop() 원하는 위치(또는 마지막)의 값 삭제
clear() 모든 값 삭제
sort() 값 순서대로 정렬
reverse() 순서 뒤집기
copy() 리스트 복사
count() 어떤 값이 몇 개 있는지
index() 어떤 값이 어디에 있는지

값을 추가하는 append, extend, insert의 차이
append는 무조건 값을 마지막 순서에 추가하며
extend는 리스트 전체가 마지막에 추가되며
insert는 원하는 위치에 값을 삽입할 수 있음

값을 삭제하는 remove, pop의 차이는
remove는 특정 색인이 아닌 첫번째 일치 값을 제거
pop은 특정 인덱스에서 항목을 제거하고 반환
'''

my_list.insert(1,'치킨')
print(my_list)

my_list.pop(1)
my_list

my_list.index('몽쉘')

# 18. 튜플

'''튜플은 도다른 내장 자료형이며 리스트는 대괄호에 콤마로 구분한다면
튜플은 소괄호로 구분한다
리스트와의 가장 큰 차이점은 리스트는 값을 수정할 수 있지만 튜플은 불가
값은 리스트와 동일하게 중복 가능하며, 형태 상관없이 삽입 가능'''

my_tuple = ('오예스', '몽쉘', '초코파이')

# 튜플의 추가와 삭제가 불가하지만 다른 것은 리스트와 동일하게 사용 가능

my_tuple.count('몽쉘')

my_tuple.index('오예스')

print('치킨' not in my_tuple)

print(my_tuple[0:2])

print(my_tuple[-1])

'''소괄호 안에 값을 넣어 튜플 선언하는 행위를 패킹이라 함
반대의 행위를 언패킹이라고 함'''

(pie1, pie2, pie3) = my_tuple # 튜플 안에 있는 값을 각각의 변수에 삽입 순서대로
pie1

numbers = (1,2,3,4,5,6,7,8,9,10)

'''numbers라는 튜플을 언패킹하려고
(one,two,others) = numbers라고 코드 작성 시 튜플 안에 값과 변수의 갯수가 맞지 않아
오류 발생 이때는 *을 사용해 one에 첫번째 값, two에 두번째 값 *others에 나머지
모든 값을 넣으면 됨 이 경우 others는 튜플이 아닌 리스트의 형태로 저장됨'''

(one, two, *others) = numbers
others

'''
(*others, nine, ten) = numbers 같이 반대의 경우에는 others에 1부터 8까지
nine에는 9, ten에는 10이 저장됨
(one, *others, ten) = numbers 는 one에 1 others에 2부터 9까지 ten에 10이 저장됨'''

# 19. 세트

''' 
세트는 리스트, 튜플과 같이 내장 자료형 값의 순서가 보장되지 않고 중복도 안됨
세트는 중괄호{} 안에 콤마로 구분됨'''

A = {'돈까스', '보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}

#.intersection이라는 메소드 사용시 세트 간 교집합인 값을 가져옴

print(A.intersection(B))

# .union 메소드는 합집합을 통해서 세트의 모든 값을 합칠 수 있음
# 이때 순서는 보장되지 않으며 중복을 허용하지 않기 때문에 중복 값은 하나만 나옴
print(A.union(B))

# 한 세트 안에서만 값을 추리려면(차집합)
print(A.difference(B))
# 이 경우 A에 있는 값만 나오며 B와 중복된 값은 안나옴

'''튜플은 순서가 보장되지 않아 인덱스를 통해 접근이 불가능함
그렇다고 값을 추가할 수 없는 건 아님'''

A.add('닭갈비')
print(A)
#add 메서드를 통해 세트에 값 추가 가능

#세트에서 값을 제거할 때는 remove 메서드 사용
A.remove('닭갈비')
print(A)

# clear 메서드로 세트 안에 값 다 날릴 수 있음
A.clear()
print(A)

'''
세트 메소드
copy() 세트복사
discard() 값 삭제(해당 값이 없어도 에러 발생x)
isdisjoint() 두 세트에 겹치는 값이 없는지 여부
issubset() 다른 세트의 부분집합인지 여부
issuperset() 다른 세트의 상위집합인지 여부
update() 다른 세트의 값들을 더함
'''

'''
원래 튜플에는 값을 수정할 수 없지만 리스트 형태로 변환한 뒤 값을 추가하고
다시 튜플 형태로 바꿔 값을 수정할 수 있다.
'''

my_t = (1,2,3,4)
my_l = list(my_t)
my_l.append(5)
print(my_l)
my_t = tuple(my_l)
print(my_t)

# 20. 딕셔너리

'''
사전을 의미하며 예시로 단어를 의미하는 key와 뜻을 의미하는 value가 값으로 이루어짐
key는 중복을 허용하지 않고 
형태는 딕셔너리 = {key1:value1,key2:value2}
'''

person = {
    '이름':'나귀욤',
    '나이':7, 
    '키':160, 
    '몸무게':50
    }
print(person)

print(person['나이'])

# 정의된 딕셔너리 데이터에 접근하려면 대괄호안에 키값을 넣으면 됨

''' 
없는 키값을 호출하면 에러가 발생하는데 get 메소드를 사용하면 오류가 생기지 않고 
없는 key에 접근하면 None이 출력'''

print(person.get('유유'))

# 새로운 데이터를 추가하려면 변수이름[추가할 key] = '추가할 value'

person['최종학력'] = '고등학교'

# 특정 키의 밸류를 바꾸려면 위 방식을 응용하면 됨

person['나이'] = 55
person

'''
하나가 아닌 여러 key의 value를 바꾸려면
update 메소드를 사용
형태는 변수이름.update({'변경을 원하는 key1':'변경 원하는 value1,'변경을 원하는 key2':'변경 원하는 value2,})
''' 

person.update({'키':180,'몸무게':70})
person

# 특정 key:value를 삭제하려면 pop 메소드를 사용한다.
person.pop('최종학력')
print(person)
# 모든 데이터를 삭제하려면 clear 메소드를 사용

# 딕셔너리 안에 어떤 key가 있는지 확인하려면 keys 메소드 사용
print(person.keys())        
# 반대로 딕셔너리 안에 어떤 value가 있는지 확인하려면 values 메소드 사용
print(person.values())
# key와 value 모두 출력하는 items 메소드 존재
print(person.items())

'''
딕셔너리 메소드
fromkeys() 제공된 keys를 통해 새로운 딕셔너리 생성 및 반환
popitem() 마지막에 추가된 데이터 삭제
setdefault() key에 해당하는 value 반환 key가 없다면 새로 만들고
defalut value 설정 및 반환
'''

'''
리스트의 값 중 순서가 중요하고 중복값이 없어야 할 경우
딕셔너리로 변경해서 중복값을 없애고 순서를 유지한 채 다시 리스트로 변경할 수 있음

'''
my_lili = [1,2,3,4,4,4]

my_dic = dict.fromkeys(my_lili)
print(my_dic)

my_li2 = list(my_dic)
my_li2

# 21. 조건문

# 변수가 참일 경우 특정 문장 실행 
# if는 만약 ~ 다면, else는 그렇지 않다면을 의미

today = '화요일'
if today == '일요일':
    print('놀아라')
print('공부해라')

today = '화요일'
if today == '일요일':
    print('공부 그만하고 놀아도 돼')
else:
    print("핸드폰 그만하고 앉아")
print('준비해라')

# 예제
total = 2
if total <= 4:
    print('추가 금액 없습니다')
else:
    print('1인당 1만원 추가입니다')
print('감사합니다')
''' 
예제설명
토탈 인원이 4명을 초과하는 경우 1만원의 추가 금액이 있지만
total 변수의 값은 2명이라 추가 금액 조건에 맞지 않아 추가금액이
없다는 문구가 출력됨'''

''' if 조건문 중에서는 elif라는 것도 있음 이것은
앞의 조건의 참이 아닐 때 다른 조건을 다시 한 번 확인하기
위한 용도로 사용됨
elif는 갯수 상관없이 사용할 수 있음'''
''' elif 예시
if 조건1:
    1 문장
elif 조건2:
    2 문장
else 조건3:
    3문장
    '''

today = '일요일'
if today == '토요일':
    print('아주 좋아 죽어')
elif today == '일요일':
    print('나쁘지 않아')
else: 
    print('지옥이야`~~~')

# if 중첩(if 문 내에서 또 다른 if문을 사용하는 경우)

yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else :
        print('다행이다')
''' if문에서 foul을 받을 경우 yellow_card가 하나씩 증가하며 yellow_card
가 2개가 될 경우 경고 누적 퇴장을 출력하는 if문 작동'''

yellow_card = 0
foul = False
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else :
        print('다행이다')
else: 
    print('주의')
    ''' 반대로 foul이 False 라면 아래 if문이 전부 해당되지 않기때문에
    맨 마지막 주의 문구만 출력됨'''

# 예제
min = 35 #게임시간
if min > 20:
    print("게임 많이 했네")
    if min > 40:
        print("당장 안꺼")
else:
    print('아직 많이 안했네')

# 22. for 반복문
''' 컴퓨터에게 특정 코드를 여러번 작성하지 않고 몇번 실행할 지 
안내하는 반복문'''
'''for 변수 in 반복 범위 또는 대상:
    반복 수행문장'''

for x in range(10): #range(10)은 10번을 반복하라는 의미, x는 변수를 의미
    print('팔 벌려 뛰기 해')

for x in range(10): # x는 range(10)으로 인해 반복할 때마다 숫자가 증가됨
    print(f'팔 벌려 높이 뛰기 {x}회')
#range(10)은 어떤 범위내에 숫자들을 만들어주는 기능을 함 0 이상 10 미만

#예제
for num in range(10):
    print(f'음료 쿠폰(입장 번호{num+1})')
''' num에 range(10)으로 인해 숫자가 들어가고 print 부분에 1씩 추가로
더해지기 때문에 1부터 10번까지 출력됨'''

''' range(10)의 경우 숫자가 10가 되면 멈춤을 의미
range의 시작과 끝을 정하고 싶다면
range(start,stop) start 이상 stop 미만
형태로 사용하면 된다.'''

for i in range(1,11):
    print(f'아주 빨리빨리 오셔야 {i}번째에 들어올 수 있어요')

''' 또 다른 형태로 range(start, stop, step)도 존재함
start 이상 stop 미만 step 만큼 증가로 step 값을 정하면
start stop 사이에서 step 값으로 정한만큼 올라감
단 step 값을 정해도 stop 값을 초과하지 않음'''

for e in range(1, 100, 5):
    print(f'아 그저 {e}위가')

for n in range(1, 31, 10):
    print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')

'''
for 반복문은 range같은 범위 뿐만 아닌 반복 대상(ex:리스트, 튜플,딕셔너리)
같은 것도 for문으로 활용할 수 있음'''

my_list = [1,2,3]

for x in my_list:
    print(x) # 이 경우 리스트 안에 있는 1,2,3을 각각 x에 대입하면서 
'''
1
2
3
이라는 값이 출력하게 됨
튜플의 경우에도 같음'''

my_tuple = (1,2,3)

for x in my_tuple:
    print(x)

# 단 딕셔너리는 조금 다름

person = {'이름':'나귀욤','나이':27,'키':120,'몸무게':23}

''' 딕셔너리는 key와 value로 이루어져있기 때문에'''

for x in person.keys():
    print(x)

for x in person.values():
    print(x)

''' keys나 values와 같은 메소드를 사용해야 됨'''
''' 혹은 둘 다 출력하고 싶은 경우'''

person = {'이름':'나귀욤','나이':27,'키':120,'몸무게':23}
for k, v in person.items():
    print(k, v)
# for 문에 변수를 두 개 넣고(ex : k, v) items 메소드를 사용하면 된다.

# 뿐 만 아니라 일반 문자열도 for 반복문을 사용할 수 있다.

fruit = 'apple'

for a in fruit:
    print(a)
''' 이때는 문자열 내 한 글자 씩 변수에 삽입되기 때문에
a
p
p
l
e
라고 출력됨'''

''' for 반복문은 리스트, 튜플과 같은 자료형은 컴마로 구분된 값을,
문자열을 한 글자 씩 출력하며 123같은 정수는 반복대상으로 사용할 수 없음'''

# 23. while 반복문

''' for 반복문과는 차이점이 있는데 for는 정해진 범위나 데이터를 반복하는
것이라면 while은 조건이 참인 동안 계속해서 반복하는 것
'''

max = 25 # 최대 허용 무게
weight = 0 # 현재 무게
item = 3 # 각 짐의 무게

while weight + item <= max: # weight와 item을 더한 값이 max 값 보다 작거나 같을 때 까지
    weight += item #weight(현재 무게)에 3을 더한다
    print(f'짐이 추가됐습니다')
print(f'총 무게는 {weight}입니다')


# 24. break

''' 반복문에서 사용하는 것으로 반복문 내에서 반복 수행 중인 동작을 즉시 멈추고
 반복문을 탈출하는 역할'''

drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']

for x in drama: # x에 drama 리스트의 값이 들어감
    if x == '시즌3': # x에 시즌 3일 경우
        print('탈출해야돼') # 해당 문구를 프린트 하고
        break # 반복문을 멈춤
    print(f'{x} 시청') # x가 시즌3가 들어가기 전까진 해당 문구 반복

# 25. continue

''' 반복문에서 어떤 경우에 동작을 건너뛰고 싶을 때 사용'''

drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']

for x in drama: # x에 drama 리스트의 값이 들어감
    if x == '시즌3': # x에 시즌 3일 경우
        print('이건 건너뛰어') # 해당 문구를 출력
        continue # 이후 즉시 다음 반복으로 넘어가게 됨
    print(f'{x} 시청 중') # x가 시즌 3일 때는 출력되지 않고 그 이후 부터 출력됨

for x in range(10):
    if x % 2 == 1: # 0 이상 10 미만의 숫자 중 2로 나눴을 때 나머지가 1인 홀수인 경우에는 다음 반복으로 그렇지 않은 경우에는 출력하므로 0,2,4,6,8이 출력됨
        continue
    print(x)

# 26. 리스트 컴프리헨션

''' 리스트 안에 표현식(계산식)과 for문, if문을 한줄에 넣어 새로운 리스트를 만들어 내는 것'''

products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [] # recall 대상 제품

for p in products:
    if p.startswith('SIRO'): # 제품명이 SIRO로 시작되는가?
        recall.append(p)# recall 리스트에 if문에 맞는 값을 넣는다

print(recall)

# 리스트 컴프리헨션 형태
# new_list = [변수 활용 for 변수 in 반복대상 if 조건]

my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x > 3] # my_list에서 값을 순회하면서 3보다 큰 값을 구함
''' for x in 앞에 x가 붙는 이유는 앞에 x가 없을 경우 변수의 리스트 그대로 값이 들어가지만
x+1, x*3, str(x)+'번째'(x를 문자열로 바꿈) 같이 조건을 적을 경우 리스트의 값이 변경되어 들어감'''

print(new_list)

# 위의 products 예시를 컴프리헨션으로 사용한다면

products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [x for x in products if x.startswith('SIRO')]
print(recall)

# 모든 모델 명에 se를 붙여줘
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [x+'SE' for x in products]
print(recall)

# 모든 모델명을 소문자로 바꿔줘
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [x.lower() for x in products]
print(recall)

# 22년 제품만 뽑는데 뒤에 (최신형)이라는 글자를 붙여줘
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [x+'(최신형)' for x in products if x.endswith('22')]
print(recall)

# 22년 미만 제품만 뽑는데 앞에 (구형)이라는 글자를 붙여줘
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = ['(구형)'+ x for x in products if '2022' not in x]
''' ('구형')+ x으로 x 값 앞에 구형을 붙이고 '2022' not in x를 통해
값 not in 변수 형식으로 2022가 들어가지 않는 값만 리스트에 삽입'''
print(recall)

# 26. 함수

''' 함수란 어떤 동작을 수행하는 코드들의 묶음,
여러 곳에서 사용되는 코드는 하나의 함수로
함수의 형태
def 함수명():
    수행할 문장
함수는 형태를 정의만 하면 아무 역할을 하지 않음
함수의 역할을 시키기 위해서는 호출이라는 것이 필요
함수명() 형태로 호출시킴
      '''

def show_price(): #함수정의
     print('커트 가격은 10000원 입니다.')
show_price() # 함수 호출

customer1 = '나장발'
print(f'{customer1} 고객님')
show_price()

customer2 = '나수염'
print(f'{customer2} 고객님')
show_price()

''' 함수명() 괄호 안에는 비워놓을 수 있지만 전달값(parameter)를 넣을 수 있음
전달값은 콤마로 구분하여 여러 개 사용할 수 있고
함수 내에서만 사용'''

def show_price(customer): #함수정의 # customer 전달값은 show_price 함수를 호출하는 곳에 보내주는 전달값이며 함수 내에서 customer라는 변수를 사용가능
     print(f'사랑하는 {customer} 고객님')
     print('커트 가격은 10000원 입니다.')


customer1 = '나장발'
show_price(customer1)#호출 시 값 전달을 위해 변수 이름 작성

customer2 = '나수염'
show_price(customer2)#호출 시 값 전달을 위해 변수 이름 작성

def now_nn(ss,dd):
    print(f'{ss}나우나우{dd}')

dd1 = '쉣'
dd2 = '누가'
now_nn(dd2,dd1)

# 27. 반환값

''' 함수 내에서 어떤 동작이나 연산을 수행하고 나서 그 함수를 호출한
쪽으로 결과를 반환
def 함수명(전달값):
    수행할 문장
    return 반환값
    형태로 return 키워드를 사용한다
    '''

def get_price(): # 함수 정의
    return 15000

price = get_price() #함수 호출
print(f'미용실 금액은 {price}원 입니다')

# 단골 손님의 경우 5천원 할인 하려 함
def get_price(is_vip): # True : 단골손님, False : 일반손님
    if is_vip == True:
        return 10000 # 단골손님
    else :
        return 15000 # 일반손님
    
price = get_price(True)# 함수를 호출 할때 True값으로 호출했기 때문에 단골손님으로 10000원이 결제
print(f'커트 가격은 {price}원 입니다')

''' 반환값은 튜플 형태로도 여러 개의 값들을 반환할 수 있음 return 키워드로
값을 반환하게 되면 반환 즉시 함수에서 탈출'''

# 28. 기본값

''' 기본값이란 전달값에 기본으로 사용되는 값 
형태로는 
def 함수명(전달값=기본값):
    수행할 문장
    '''

def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else : 
        return 15000
    
price = get_price()
print(f'커트 가격은 {price}원 입니다')
# 기본 값으로 False 설정됐기 때문에 단골인 경우에만 함수호출 괄호 안에 True만 넣으면 됨

# 29. 키워드값

''' 전달값이 여러개 있는 경우 전달값의 대상을 정해주는 것'''

def get_price(is_vip=False,
              is_birthday=False,
              is_membership=False,
              card=False,
              review=False,
              first_time=False):
    if is_vip == True:
        return 10000
    elif is_birthday == True:
        return 12000
    elif is_membership == True:
        return 13000
    elif card == True:
        return 14000
    elif review == True:
        return 11000
    elif first_time == True:
        return 10000
    else :
        return 15000
    
price = get_price(review=True) # 키워드 값의 순서는 상관 없음
print(f'손님께서 결제할 금액은 {price}원 입니다')

# 30. 가변인자
''' 개수가 바뀔 수 있는 인자를 의미 이 함수를 호출할 때 전달값이 몇 개가 될지 모르는 경우
개수를 신경쓰지 않고 함수를 사용할 수 있게 해줌 사용방법은
*전달값 형식으로 전달값 앞에 *을 붙여주면 됨
이때 값은 튜플 형태로 값들을 받게 됨
주의할 점은 가변인자는 마지막에 위치한 전달값 하나에만 사용해야 한다 '''
    
def visit(today, *customers): #today는 오늘의 날짜를 전달받음
    print(today) #날짜 출력
    for customer in customers:
        print(customer) # customer 변수에 custmoers 전달값이 들어가서 반복문으로 모든 고객의 이름을 출력

visit('2022년 05월 25일', '나장발') # 한 명일때
visit('2022년 05월 25일', '나장발', '나숙숙') # 두 명일때
visit('2022년 05월 25일', '나장발', '나숙숙', '나두두') # 세명 명일때

# 31.지역변수

''' 함수 내에서 정의된 변수를 의미 지역 변수는 그 함수 내에서만 사용 가능'''

def secret():
    message = '이건 나의 비밀' # secret 함수 내에서 정의된 message는 해당 함수에서만 사용가능(다른 함수 및 함수 밖에서 사용 x)
    print(message) # 값 출력
    message= '함수 내에서는 자유롭게 수정이 가능해요'


# 31. 전역변수

''' 함수 안이나 밖이나 상관없이 어디서든 사용가능 '''

message = '나는 전역 변수'

print(message)

def no_secret():
    global message # 전역 변수 사용, 없으면 여기서 만듬
    message = '이러면 또 지역변수'
    print(message) # 이 경우 지역변수로 출력됨

no_secret()

message = '나는 전역 변수'

print(message)

message = '나는 전역 변수'

print(message)

def no_secret():
    global message # 전역 변수 사용, 없으면 여기서 만듬
    message = '오 진짜 전역변수'
    print(message) # 이 경우 지역변수로 출력됨

no_secret()
print(message)

x = 3
def add():
    x = 6
    x += 3
add()
print(x)
''' add() 함수 내에서 x = 6과 같이 global 선언 없이 값을 설정하면
x라는 지역 변수가 새로 생기게 됨, 그래서 전역 변수인 x는 변함 없이 3'''

# 32. 사용자 입력

''' 입력값은 항상 문자열 형태 4라는 숫자열을 써도 문자열 '4'의 문자열 형태로 바뀜
이럴때는 형변환을 이용하면 됨(int로 input을 감싸면 숫자열의 형태로 값을 받음)'''

name = input('예약자분 성함이 어떻게 되나요?')
print(name)

num = int(input('총 몇 분이세요?'))

if num > 4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다')

dream = input('당신의 꿈은 무엇인가요?')
print(f'나의 꿈은 {dream}입니다')

# 33. 파일입출력
''' open() 코드를 통해 파일에 텍스트를 쓰거나 파일로부터 읽어올 수 있음'''

# 예시
open(파일명, 열기 모드, encoding='인코딩')

'''열기모드
r : read(읽기)
a : append(이어서 쓰기)
w : write(쓰기)'''

# 파일 쓰기
f = open('list.txt', 'w', encoding='utf8') #쓰기 모드로 파일열기
f.write('김xx\n') #문장 입력하기
f.write('정xx\n') #문장 입력하기
f.write('허xx\n') #문장 입력하기
f.close() # 파일 

''' 파일을 열었으면 반드시 .close()로 닫아줘야 함'''

#파일 읽기
f = open('list.txt','r',encoding='utf8') #읽기 모드로 파일열기
contents = f.read() # 파일 내용 다 읽어오기
print(contents)
f.close()

#파일을 한 줄 씩 읽고 싶은 경우
f = open('list.txt','r',encoding='utf8')
for line in f:
    print(line, end='')
f.close

# 34. with
''' 블럭을 벗어나면 자동으로 파일 닫음(close) 때문에 
따로 close함수를 사용하지 않아도 됨'''

'''f = open('list.txt', 'w', encoding='utf8')'''
#해당 코드가 with을 사용하면

with open('list1.txt','w', encoding='utf8') as f: # 콜론 다음부터 들여쓰기 해서 코드를 작성하면 됨
    f.write('김xx\n')
    f.write('정xx\n')
    f.write('허xx\n')  

with open('list1.txt','r',encoding='utf8') as f:
    contents = f.read()
    print(contents)

# 35. 클래스

'''여러 변수들을 묶어서 한 번에 관리할 수도 있고 클래스 안에 어떤 기능을 하는
함수와 같은 걸 만들어서 동작할 수 있음'''

''' A 클래스로부터 만들어진 객체(object) B가 있다고 할 때,
B는 A의 인스턴스(instance)라고 표현한다'''

# 클래스의 형태

class 클래스명:
    클래스를 정의

class BlackBox:
    pass #pass는 구현해야 하는 부분을 잠시 미뤄두기 위해서 사용
b1 = BlackBox() # 변수를 선언하듯 객체 b1을 작성하고 = 뒤에 클래스명 작성
b1.name = '까망이' #변수 선언 b1이라는 객체에 name이라는 변수를 선언함
print(b1.name)
#b1 객체가 BlackBox의 인스턴스가 맞는지 확인하려면
print(isinstance(b1, BlackBox))#값이 True이면 인스턴스가 맞음

class BlackBox:
    pass

b1 = BlackBox()
b1.name = '까망이'

b2 = BlackBox()
print(b2.name)

''' __init__은 반드시 첫 번째 인수로 self를 지정해야됨'''
class BlackBox():
    def __init__(self,name,price): ## 각각 객체를 만들때 넣어주는 초기화 역할을 하는게__init__
        self.name = name # self.name을 멤버 변수라함
        self.price = price # self.price를 멤버 변수라함

b1 = BlackBox('까망이',200000)
print(b1.name,b1.price)
b2 = BlackBox('하양이',100000)
print(b2.name,b2.price)

''' 멤버 변수는 클래스 객체마다 서로 다른 값을 가질 수 있음 멤버 변수는 모든 객체가 아닌
특정 객체에만 추가할 수 있음'''


# 클래스에 특정한 기능을 넣으려고 하는 경우 
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def set_travel_model(self): # 전달 받는 값이 없다면 self 하나만 적어도 됨
        print('여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b1.set_travel_model() # 실행 결과 : 여행 모드 ON

#메소드에 전달값이 필요한 경우

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def set_travel_model(self, min):# 여행 모드 시간(분)
        print(str(min) + '분 동안 여행모드 ON')

b1 = BlackBox('까망이', 2000000)
b1.set_travel_model(20)#괄호 안에 들어가는 숫자는 min에 들어가는 값임

class Student:
    def intorduce(self, name, age):
        print(f'제 이름은 {name}이고 {age} 살입니다')

student = Student()
student.intorduce('나도코딩',29)

'''클래스 내에서 메소드를 정의할 때 self를 사용
이때 self는 객체 자기자신을 의미함'''

class BlackBox:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def set_travel_mode(self,min): # self에는 b1이나 b2같은 객체 자기 자신이 들어가게 됨
        print(f'{self.name} {min}분 동안 여행모드 ON')
    
b1 = BlackBox('까망이','200000')
b2 = BlackBox('하양이','100000')

b1.set_travel_mode(20)
b2.set_travel_mode(10)

'''self
1. 메소드를 정의할 때 처음 전달값은 반드시 sefl
2. 메소드 내에서는 self.name과 같은 형태로 멤버변수를 사용
객체를 통해 메소드를 호출할 때 self 부분에 해당하는 전달값은 따로 명시하지 않아도 됨'''

# 36. 상속
'''상속이란 A 클래스에서 사용하는 모든 코드들을 그대로 물려 받아서 B 클래스에 사용하거나
추가로 필요한 내용들을 코드로 확장하는 개념
이때 상속 해준 클래스를 부모 클래스라고 하며 상속 받은 클래스는 자식클래스라 한다''' 


#기본 블랙박스
class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price


#여행 모드 지원 블랙박스
class TravelBlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 ON')

''' 특정 클래스를 상속받으려면'''

class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox): #상속 받을 클래스의 괄호안에 상속해줄 클래스를 작성하면 된다
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 ON')
    # __init__ 메소드를 기본 블랙박스 클래스에서 상속받았기 때문에 작성하지 않아도 됨
b1 = TravelBlackBox('하양이',100000)#하양이와 가격이 부모 클래스에 존재하는 init메소드의 name과 price라는 멤버변수로 설정됨
print(b1.name,b1.price)
b1.set_travel_mode(20)

#. 37. super

''' 상속 받은 클래스에서 새로운 멤버 변수를 만들려고 하는 경우 부모클래스.메소드(self)보다
간편하게 super().메소드()를 이용해
상속 받은 채 새로운 변수를 추가할 수 있다'''

class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox): #상속 받을 클래스의 괄호안에 상속해줄 클래스를 작성하면 된다
    def __init__(self,name,price,sd):
     super().__init(name,price)
     self.sd = sd
    
     def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 ON')