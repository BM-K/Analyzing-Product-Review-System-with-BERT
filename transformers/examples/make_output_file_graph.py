import matplotlib.pyplot as plt
fig = plt.figure()

class make_output_file_graph():
    def __init__(self, preds):
        self.preds = preds

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
                # print(int(line))
                if int(line) == 1:
                    one += 1
                else:
                    zero += 1
        return one, zero

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
