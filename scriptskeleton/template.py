from scriptskeleton import ScriptSkeleton

ss = ScriptSkeleton('page1 page50')

# 1
ss.feed("0")
# 2
ss.feed("0")
# 3
ss.feed("0")
# 4
ss.feed("0")
# 5
ss.feed("""4pan:
0
0
0
3b""")
# 6
ss.feed("""3pan:
3b
3b
b""")
# 7
ss.feed("""4pan:
0
2b
b
0""")
# 8
ss.feed("""4pan:
2b
3b
b
off""")
# 9
ss.feed("""3pan:
b off b
2b
0""")
# 10
ss.feed("""2pan:
2b
2b""")
# 11
ss.feed("""4pan:
0
0
off
b""")
# 12
ss.feed("""4pan:
0
0
0
2b""")
# 13
ss.feed("""3pan:
2b
2b
0""")
# 14
ss.feed("""4pan:
0
2b
b
b""")
# 15
ss.feed("""3pan:
0
off
2b""")
# 16
ss.feed("""5pan:
3b
off
2b down
b sfx b
2b""")
# 17
ss.feed("""4pan:
b
2b
blacksfx
b""")
# 18
ss.feed("0")
# 19
ss.feed("0")
# 20
ss.feed("""5pan:
0
0
0
b
b""")
# 21
ss.feed("""4pan:
offb
2offb
0
0""")
# 22
ss.feed("""3pan:
0
b
0""")
# 23
ss.feed("""2pan:
0
b""")
# 24
ss.feed("0")
# 25
ss.feed("0")
# 26
ss.feed("""5pan:
0
b
2b
0
0""")
# 27
ss.feed("""3pan:
2off
b
b""")
# 28
ss.feed("""3pan:
3offb
2b
3b""")
# 29
ss.feed("""4pan:
b
2b
2b
2b""")
# 30
ss.feed("""6pan:
2b
b
b
b
2offb
2offb""")
# 31
ss.feed("""4pan:
0
0
0
3b""")
# 32
ss.feed("""5pan:
2b
0
sfx
sfxs
0""")
# 33
ss.feed("""4pan:
b
3b
2b
2b""")
# 34
ss.feed("""3pan:
0
b
2b""")
# 35
ss.feed("""5pan:
2b
0
0
b
0""")
# 36
ss.feed("""5pan:
2b
0
0
3sq
b""")
# 37
ss.feed("""4pan:
offb 2smallb offb
3b
0
3b""")
# 38
ss.feed("""2pan:
2b
0""")
# 39
ss.feed("0")
# 40
ss.feed("pan(0) pan(0) pan(b)")
# 41
ss.feed("0")
# 42
ss.feed("0")
# 43
ss.feed("0")
# 44
ss.feed("""4pan:
2b
0
0
0""")
# 45
ss.feed("""5pan:
b
2b
0
b
0""")
# 46
ss.feed("0")
# 47
ss.feed("0")
# 48
ss.feed("0")
# 49
ss.feed("""6pan:
b
4b
2b
b
0
2b""")
# 50
ss.feed("""4pan:
2b
b
twojoined
3b""")

ss.to_file('capeta8-1.txt')
