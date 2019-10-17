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
    count = 0
    max = 0
    sum = 0
    num = 10
    f = open("./GLUE_DIR/MRPC/%s" % file, 'r', encoding="utf-8") # 여기를 애초에 만든 bad des 를 넣어줘야함.
    rdr = csv.reader(f, delimiter='\t')
    for line in rdr:
        if count == 9 :
            break
        if line[0] in zero_des:
            sum += len(line[1])
            if max < len(line[1]):
                max = len(line[1])
            if len(line[1]) > 90:
                print("index : ", line[0], "\nshot_des : ", line[1])
                f2 = open('./GLUE_DIR/MRPC/ld1_allp.tsv','r',encoding=
                          'utf-8-sig')
                rdr2 = csv.reader(f2, delimiter='\t')
                for line2 in rdr2:
                    if line[0] == line2[0]:
                        print("\nlong_des : ",line2[2],"\n")
                        print("------------------------------------------"
                              "---------------------------------------")
                        break
                count += 1
                index.append(line[0])
    f.close()