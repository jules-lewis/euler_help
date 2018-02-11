
def number_to_words(num):
    '''My implementation of a fairly common helper function, that
       converts a number up to 1,000,000 into English words
    '''

    d = {  0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four',
           5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine',
          10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',
          14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen',
          17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen',
          20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty',
          60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    if 0 <= num < 1000000:

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0:
                return d[num]
            else:
                return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < 1000):
            if num % 100 == 0:
                return d[num // 100] + ' hundred'
            else:
                return d[num // 100] + ' hundred and ' + number_to_words(num % 100)

        if num % 1000 == 0:
            return number_to_words(num // 1000) + ' thousand'
        else:
            return number_to_words(num // 1000) + ' thousand, ' + number_to_words(num % 1000)

