import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import bring_zeroLabel_des as bzl
import sys
import re
import nltk
from nltk.corpus import stopwords

def data_text_cleaning(data):
    # 영문자 이외 문자는 공백으로 변환
    only_english = re.sub('[^a-zA-Z]', ' ', data)

    # 소문자 변환
    no_capitals = only_english.lower().split()

    # 불용어 제거
    stops = set(stopwords.words('english'))
    no_stops = [word for word in no_capitals if not word in stops]

    # 어간 추출
    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]

    # 공백으로 구분된 문자열로 결합하여 결과 반환
    return ' '.join(stemmer_words)


def get_TFIDF_Result(title_idx, cosine_sim, indices, data_Des):
    while True:
        try:
            idx = indices[title_idx]
            break
        except KeyError:
            print("------Error--No--Index----2--")
            print("\n")
            return
    idx = indices[title_idx]
    idx = int(idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    data_indices = [i[0] for i in sim_scores]
    num=1
    print("\n")
    f = open('bad_shot_des_after_bert.tsv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        if line[0] == title_idx:
            shot_des = line[1]
    f.close()
    f = open('bad_long_des_after_bert.tsv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        if line[0] == title_idx:
            long_des = line[2]
    f.close()

    print("Your input : ", title_idx, "\nshot_des : ", shot_des, "\nlong_des : ", long_des)
    print("\n")
    print("================Print Similar data================")
    f = open('bad_long_des_after_bert.tsv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        for i in data_indices:
            if(int(line[0])==int(i)):
                print(num,":",line[2])
                print('\n')
                num += 1
    print("=======================================================")


def main__run():
    data_num = []
    data_Name = []
    data_Des = []
    num = 0
    name = 0

    f = open('bad_long_des_after_bert.tsv', 'r', encoding='utf-8-sig') # 주석처럼 만들고 여기에는 bad_long_des 넣어주면 된다.
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        data_num.append(line[0])
        data_Name.append(line[1])
        if len(line[2]) < 100:
            data_Des.append('x') # 꼼수
        else:
            data_Des.append(data_text_cleaning(line[2]))
        num+=1
        name+=1

    f.close()

    pd_data_des = pd.Series(data_Des, index=data_num)

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(pd_data_des)

    from sklearn.metrics.pairwise import linear_kernel
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(data_num, index=data_num)
    print("\n")
    print("--Running--")
    while (1):
        print("------------------------------------------------------")
        idx = input("What do you want to see index(exit:-1) : ")
        num = int(idx)
        if idx in bzl.index:
            get_TFIDF_Result(idx, cosine_sim, indices, data_Des)
        else:
            if num == -1:
                sys.exit()
            else:
                print("-------Error--No--Index--------")
