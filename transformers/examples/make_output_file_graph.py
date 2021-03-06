import matplotlib.pyplot as plt
import csv
fig = plt.figure()

class make_output_file_graph():
    def __init__(self, preds):
        self.preds = preds
        self.bad_label_index = []

    def make_output_labels(self):
        one = 0
        zero = 0
        preds_label_data = []

        with open("output_labels.txt", 'w') as writer:
            for i in range(len(self.preds)):
                writer.write(str(self.preds[i]))
                writer.write('\n')
            for j in range(len(self.preds)):
                preds_label_data.append(str(self.preds[j]))
        with open("output_labels.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if int(line) == 1:
                    one += 1
                else:
                    zero += 1
        return one, zero

    def make_bert_pred_bad_des(self):
        count = 1
        with open("output_labels.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if int(line) == 0:
                    self.bad_label_index.append(count)
                    count += 1
                else:
                    count += 1

    def make_bad_long_des_file(self):
        long_des = []
        count = 0
        idx_count = 0
        f = open('./GLUE_DIR/MRPC/ld1_allp.tsv', 'r', encoding='utf-8-sig')
        rdr = csv.reader(f, delimiter='\t')
        for line in rdr:
            temp = []
            if int(self.bad_label_index[count]) == int(line[0]):
                temp.append(idx_count)
                temp.append(line[2])
                long_des.append(temp)
                idx_count += 1
                count += 1
        f.close()

        with open("bad_long_des_after_bert.tsv", 'w', encoding='utf-8') as f:
            wr = csv.writer(f, delimiter='\t')
            for i in range(len(long_des)):
                index = long_des[i][0]
                ld = long_des[i][1]
                index = str(index)
                ld = str(ld)
                wr.writerow([index, index, ld])

    def make_bad_shot_des_file(self):
        shot_des = []
        count = 0
        idx_count = 0
        f = open('./GLUE_DIR/MRPC/sd1_allp.tsv', 'r', encoding='utf-8-sig')
        rdr = csv.reader(f, delimiter='\t')
        for line in rdr:
            temp = []
            if int(self.bad_label_index[count]) == int(line[0]):
                temp.append(idx_count)
                temp.append(line[1])
                shot_des.append(temp)
                idx_count += 1
                count += 1
        f.close()

        with open("bad_shot_des_after_bert.tsv", 'w', encoding='utf-8') as f:
            wr = csv.writer(f, delimiter='\t')
            for i in range(len(shot_des)):
                index = shot_des[i][0]
                sd = shot_des[i][1]
                index = str(index)
                sd = str(sd)
                wr.writerow([index, sd])

    def make_output_labels_num(self, one, zero):
        with open("output_labels_num.txt", 'w') as writer:
            writer.write("one :")
            writer.write(str(one))
            writer.write('\n')
            writer.write("zero : ")
            writer.write(str(zero))
            writer.write('\n')

    def make_graph(self, one, zero):
        labels = ['good', 'bad']
        ratio = [one, zero]
        plt.pie(ratio, labels=labels, shadow=True, startangle=90, autopct='%1.2f%%')
        fig.savefig('./graph_go_consol' + '.png')

    # def make_graph2(self, epoch, loss):
    #     plt.plot(epoch, loss)
    #     plt.ylabel('Loss')
    #     plt.xlabel('Epoch')
    #     fig.savefig('./graph_loss_go_consol' + '.png')