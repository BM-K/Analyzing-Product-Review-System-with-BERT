import csv
output_label_list = []
zero_des = []

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

def bring_output_label():
    f = open("output_labels.txt", 'r', encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        line = line[0:1]
        output_label_list.append(line)
    f.close()
    
def test():
    f = open("afsdf.txt",'w')
    f.write("asdf")
    f.close()
