def main(i,j):
    i += j
    j = i[0:len(i) - len(j)]
    i = i[len(j):]
    print(i,j)

main('abkkkdd','iiddkds')