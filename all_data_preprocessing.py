import csv
f = open('all_data_shuffle___wait.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)
data_list = []
for i in range(len(r)):
    data_list.append(r[i])

f.close()

with open('all_data_shuffle_train.tsv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, delimiter='\t')
    for i in range(0,2100):
        des = data_list[i][0]
        label = data_list[i][1]
        wr.writerow([i, des, label])
n=0
with open('all_data_shuffle_test.tsv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f, delimiter='\t')
    for i in range(2100,3000):
        des = data_list[i][0]
        label = data_list[i][1]
        wr.writerow([n, des, label])
        n +=1