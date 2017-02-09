height = int(raw_input("Width?"))

def triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( i + 1 ) + '*' * ( t * 2 + 1 ))
        return triangle( i - 1, t + 1 )
