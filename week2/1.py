def convert(num):
    fraction = num - int(num)
    integer = int(num)
    BinInt = ''
    while integer > 0:
        BinInt = str(integer % 2) + BinInt
        integer = integer//2

    BinFra = ''
    while fraction*2 != 1 and fraction > 0:
        temp = fraction*2
        if temp > 1:
            temp -= 1
            BinFra += '1'
        else:
            BinFra += '0'

        fraction = temp
    BinFra += '1'
    if BinFra == '':
        return BinInt
    if BinInt == '':
        return BinFra
    else:
        return BinInt + '.' + BinFra
print(convert(float(input('enter number you want to convert: '))))
