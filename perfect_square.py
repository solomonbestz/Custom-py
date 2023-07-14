
def bestz_sqr_root(value: int):
    if value < 0:
        return "Can't Square"
    return int(value ** 0.5)

def bestz_perfect_square(value: int):
    """
    Returns True if value is a perfect square,
    Else Returns False if value is not a perfect square
    """
    number = bestz_sqr_root(value)
    if (number * number) != value:
        return False
    return True


if __name__=='__main__':
    number = int(input('Enter Number: '))

    print(bestz_perfect_square(number))

    

    