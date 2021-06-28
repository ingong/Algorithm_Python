set_list = set([])
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                cards = str(i) + str(j) + str(k) + str(l)
                min_card = int(min(cards, cards[1:] + cards[:1], cards[2:] + cards[:2], cards[3:] + cards[:3]))
                set_list.add(min_card)


numbers = "".join(list(map(str, input().split())))
min_numbers = int(min(numbers, numbers[1:] + numbers[:1], numbers[2:] + numbers[:2], numbers[3:] + numbers[:3]))
answer = [i + 1 for i, val in enumerate(sorted(set_list)) if val == min_numbers]
print(*answer)
