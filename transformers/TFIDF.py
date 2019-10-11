import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import bring_zeroLabel_des as bzl

def get_TFIDF_Result(title, cosine_sim):
    while True:
        try:
            idx = indices[title]
            break
        except KeyError:
            print("------No page name. Maybe I don't update recent page------")
            print("\n")
            return
    idx = indices[title]
    idx = int(idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    data_indices = [i[0] for i in sim_scores]
    num=1
    for i in data_indices:
        print(num,":",data_Des[i])
        num += 1
    print("------------------------------------------------------")

data_num = []
data_Name = []
data_Des = []
k = 0

f = open('ld1_allp.tsv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f, delimiter='\t')
for line in rdr:
    if int(bzl.zero_des[k]) == int(line[0]):
        data_num.append(line[0])
        data_Name.append(line[1])
        data_Des.append(line[2])
    k += 1
f.close()

pd_data_des = pd.Series(data_Des, index=data_num)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(pd_data_des)

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data_num, index=data_Name)

print("--Running--")
while(1):
    print("------------------------------------------------------")
    print("What do you want to use functions?")
    print("1 : search similar page (compare each description)")
    print("0 : exit")
    a = int(input("input number: "))
    if a == 1:
        data_input = input("data input :")
        get_TFIDF_Result(data_input, cosine_sim)
    elif a == 0:
        exit()
    else:
        print("Error No function try again")
