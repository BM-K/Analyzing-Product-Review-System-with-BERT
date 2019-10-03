import csv

def convert_our_data(file, data_list):
    f = open("%s" % file , 'r', encoding="utf-8")
    rdr = csv.reader(f)
    for line in rdr:
        line = line[0].split('\t')
        data_list.append(line)
    f.close()
def csv2tsv(file, data_list):
    with open('%s'%file, 'w', encoding='utf-8') as f:
        wr = csv.writer(f, delimiter='\t')
        for i in range(len(data_list)):
            des = data_list[i][0]
            label = data_list[i][1]
            wr.writerow([des, label])

amz_data = []
imdb_data = []
yelp_data = []

if __name__ == '__main__':
    convert_our_data("amazon_cells_labelled.csv", amz_data)
    convert_our_data("imdb_labelled.csv", imdb_data)
    convert_our_data("yelp_labelled.csv", yelp_data)
    # ---
    csv2tsv("amazon_cells_labelled_c2t.tsv", amz_data)
    csv2tsv("imdb_labelled_c2t.tsv", imdb_data)
    csv2tsv("yelp_labelled_c2t.tsv", yelp_data)
