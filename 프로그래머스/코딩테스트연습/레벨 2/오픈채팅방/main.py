def solution(record):
    answer = []
    textline = []
    id_nickDict = dict()

    for rec in record:
        output = ''
        recInfo = rec.split(' ')
        if recInfo[0] == "Enter":
            output += recInfo[1] + "님이 들어왔습니다."
            textline.append(output)
            id_nickDict[recInfo[1]] = recInfo[2]
        elif recInfo[0] == "Leave":
            output += recInfo[1] + "님이 나갔습니다."
            textline.append(output)
        else:
            id_nickDict[recInfo[1]] = recInfo[2]

    for line in textline:
        uid = line[:line.index('님')]
        line = line.replace(uid,id_nickDict[uid])
        answer.append(line)

    return answer