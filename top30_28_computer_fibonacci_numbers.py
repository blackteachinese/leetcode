# Q #28) Compute the first five Fibonacci numbers.

# Answer: 0 and 1 are the first two Fibonacci numbers and all the numbers after 0 and 1 are the addition of the two previous numbers.


from re import S


def computer():
    f,s=0,1
    step=2
    while step <= 5:
        f,s=s,f+s
        step += 1
        print(s)

computer()