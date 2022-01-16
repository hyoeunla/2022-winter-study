# 18.6 실습 문제 ▶ 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며 
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 
# 3으로 끝나지 않는 숫자가 출력되게 만드세요. 

# 입력 : 1 20
# 결과 : 1 2 4 5 6 7 8 9 10 11 12 14 15 16 17 18 19 20

# start, stop = map(int, input().split())
 
# i = start
 
# while True:
# _____________________
#     print(i, end=' ')
#     i += 1

# 정답 
start, stop = map(int, input().split())
i = start
while True: 
    if i % 10 == 3: 
        i += 1
        continue                              
    if i > stop: 
        break     
    print(i, end=' ')
    i += 1