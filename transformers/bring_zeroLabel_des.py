import csv
output_label_list = []
zero_des = []
index = []

def bring_output_label():
    f = open("output_labels.txt", 'r', encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        line = line[0:1]
        output_label_list.append(line)
    f.close()

def bring_test_file(file, count):
    f = open("./GLUE_DIR/MRPC/%s" % file , 'r', encoding="utf-8")
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        if count == 0:
            count += 1
            continue
        else:
            if output_label_list[count-1] == '0':
                zero_des.append(line[0])
            count += 1
    f.close()

def print_bad_des(file):
    max = 0
    sum = 0
    num = 10
    f = open("./GLUE_DIR/MRPC/%s" % file, 'r', encoding="utf-8")
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        if line[0] in zero_des:
            sum += len(line[1])
            if max < len(line[1]):
                max = len(line[1])
            if len(line[1]) > 70:
                print("index : ", line[0], ", shot_des : ", line[1])
                index.append(line[0])
    f.close()