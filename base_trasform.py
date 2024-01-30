def convert_to_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        print(f"result({result}) += number({number}) % 10 * multiplier({multiplier})")
        print(f"number({number}) % 10 = {number % 10}")
        result += number % 10 * multiplier
        print(f"result => {number % 10 * multiplier}")
        print(f"multiplier({multiplier}) *= base({base})")
        multiplier *= base
        print(f"multiplier = {multiplier * base} ")
        print(f"number{number} = number // 10")
        number = number // 10
        print(f"number = {number}")
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    print("테스트 통과")

def convert_from_decimal(number, base):
    multiplier, result = 1, 0
    while number > 0:
        print(f"result({result}) += number({number}) % base({base}) * multiplier({multiplier})")
        print(f"number({number}) % base({base}) = {number % base}")
        result += number % base * multiplier
        print(f"result => {result}")
        print()
        print(f"multiplier({multiplier}) *= 10")
        multiplier *= 10 
        print(f"multiplier = {multiplier} ")
        print()
        print(f"number({number}) = number({number}) // base({base})")
        number = number // base 
        print(f"number = {number}")
        print('===============')
    return result

def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    print("테스트 통과")

def convert_from_decimal_larger_base(number, base):
    strings ="0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit  = number % base
        result = strings[digit] + result
        number = number // base
    return result

def test_convert_from_decimal_larger_base():
    number, base = 31, 16
    assert(convert_from_decimal_larger_base(number, base) == '1F')
    print("테스트 통과")

if __name__ == "__main__":
   #test_convert_to_decimal()
   #test_convert_from_decimal()
   test_convert_from_decimal_larger_base()
