'''
정수 3개를 입력받아 합과 평균을 출력해보자.

합과 평균을 줄을 바꿔 출력한다.
평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.
'''
x, y, z = map(int, input().split())
print( x+y+z )
print( round((x+y+z)/3, 1) )