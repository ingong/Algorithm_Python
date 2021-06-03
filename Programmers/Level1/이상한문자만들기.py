s = "try hello world"


word = " ".join(map(lambda x: "".join([val.upper() if idx % 2 == 0 else val.lower() for idx, val in enumerate(x)]), s.split(" ")))
print(word)

