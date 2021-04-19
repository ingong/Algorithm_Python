A = ['abcd', 'xyz', 'spam']
B = sorted(A, key=lambda x: len(x))

C = [{'name': 'John','score':83},{'name':'Paul', 'score':92}]
C.sort(key=lambda x: x["score"], reverse=True)
print(C)

# 선형 탐색 : 리스트의 길이에 비례하는 시간 소요 Big-O(n)
# index 메서드를 활용하는 것과 동일
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1

# pseudo code
# def linear_search(L, x):
#     i 를 0 으로 초기화
#     while i가 L의 길이보다 작고 and L의 해당 index 값이 x 가 아닐때:
#         i 값을 1 증가
#     if i 가 L 의 길이보다 작을 때
#         return i
#     else
#         return -1


# 이진 탐색 : 한 번 비교가 일어날 때마다 리스트가 반씩 줄임 (divide & conquer)
