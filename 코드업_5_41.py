'''
영문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.
'''
order = ord(input())
print(chr(order+1)) #아스키 코드로 변환된 숫자에 1을 더한 뒤 아스키 문자로 재변환