id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

report = list(set(report))
report2D = [[0] * 2 for _ in range(len(report))]
reportee = list()
tarReportee = list()
tarReporter = list()
answer = list()

for i in range(len(report)):
    report2D[i] = report[i].split(" ")
    reportee.append(report2D[i][1])
reporteeSet = set(reportee)

for r in reporteeSet:
    if reportee.count(r) >= k:
        tarReportee.append(r)

for r in report2D:
    if r[1] in tarReportee:
        tarReporter.append(r[0])

for i in id_list:
    answer.append(tarReporter.count(i))
print(answer)