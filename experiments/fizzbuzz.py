__author__ = 'johnfulgoni'

def fizzbuzz_recursive(begin, end, result):
    if begin == end:
        return result

    if fizzbuzz(begin):
        result.append('(' + str(begin) + ') fizzbuzz')
    elif buzz(begin):
        result.append('(' + str(begin) + ') buzz')
    elif fizz(begin):
        result.append('(' + str(begin) + ') fizz')

    return fizzbuzz_recursive(begin + 1, end, result)

def fizzbuzz(number):
    return number % 3 == 0 and number % 5 == 0

def buzz(number):
    return number % 5 == 0

def fizz(number):
    c = number % 3 == 0
    return c

if __name__ == '__main__':
    begin = 1
    end = 100
    print 'Beginning Fizz Buzz from ' + str(begin) + ' to ' + str(end) + '!'
    print fizzbuzz_recursive(begin, end, []);
    print 'Done'