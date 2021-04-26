from itertools import combinations
L, C = map(int, input().split())
alphabets = sorted(input().split())
result = []

for s in combinations(alphabets, L):
    v_flag = False
    c_flag = 0
    word = ''.join(s)

    for i in word:
        if i in "aeiou":
            v_flag = True
        else:
            c_flag += 1
    if v_flag == True and c_flag >= 2:
        result.append(word)


# 리스트의 형태로 결과를 반환
print(result)

# 한 줄씩 띄워서 결과 값을 출력하게 해준다
print("\n".join(result))

# 문제 설계 복습하기
# combinations 를 사용하기 위해 import 시킨다
# L 과 C 를 입력받는다
# 알파벳을 입력받는 동시에, 정렬 시킨다 sorted(input().split())
# 결과 값을 입력받을 리스트 생성
#
# combinations 라이브러리를 통해 조합을 만들고, 해당 값이 조건을 만족시키는지 확인
# 모음이 한 개 이상 => boolean 활용
# 자음의 개수가 2개 이상 => 0 으로 확인
# 중요중요! word = ''.join(s) => 튜플의 형태이므로 순회하기 위해서는 이렇게 합쳐줘야한다
#
# 모음에 있는지 확인한다
# 아니면 자음이니깐 +1 을 해준다
#
# 조건에 만족한다면 result 에 더해준다

# print('\n'.join(result))


