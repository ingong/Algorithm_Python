while True:
    try:
        N = int(input())
    # An EOFError is raised when a built-in function like input()
    # or raw_input() do not read any data
    # before encountering the end of their input stream.
    except EOFError:
        break
    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= N
        if num == 0:
            print(i)
            break
        i += 1