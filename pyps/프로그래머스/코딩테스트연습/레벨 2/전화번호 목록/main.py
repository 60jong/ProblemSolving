def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)
    headDict = {}

    for number in phone_book:

        for idx in range(len(number)):
            if number[:idx] in headDict.keys():
                answer = False
                break
        headDict[number] = ''

    return answer