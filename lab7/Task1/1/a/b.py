a = int(input())
next = a + 1
previous = a - 1

next_txt = "The next number for the number {} is {}."
previous_txt = "The previous number for the number {} is {}."
print(next_txt.format(a, next))
print(previous_txt.format(a, previous))