import random
import math

def list_weight(x, y):
    list1 = []
    for i in range(x):
        m = []
        for j in range(y):
            m.append(random.uniform(0.1, 0.4))
        list1.append(m)
    return list1

def signoid(x):
    return 1 / (1 + math.exp(-x))

def d_signoid(x):
    return signoid(x) * (1 - signoid(x))

class neuralnet:
    def __init__(self, inputnode, hiddennode, outputnode):
        # initialize number of node
        self.inputnode = inputnode + 1  #for bias node
        self.hiddennode = hiddennode
        self.outputnode = outputnode

        # #make array for weight
        # self.inputweight = list_weight(self.inputnode,self.hiddennode)
        # self.hiddenweight = list_weight(self.hiddennode,self.outputnode)
        # self.bias_hiddenweight = list_weight(self.outputnode,1)

        # self.inputweight = [[0.21,-0.4],[0.15,0.1],[0.2,0.22],[0.25,0.11],[-0.3,0.25]]
        # self.hiddenweight =  [[-0.2], [0.3]]
        # self.bias_hiddenweight = [[-0.4]]

        #hidden node 8
        self.inputweight = [[0.10822803735314036, 0.25697118745839986, 0.27847715572560394, 0.29469781543386087, 0.37146413953467283, 0.27833247901316627, 0.10993889968991166, 0.12748258446053196], [0.22460910927082672, 0.15657557324189986, 0.14562365189509185, 0.2329520905637502, 0.3721800491724323, 0.3558450502704801, 0.1278061288536565, 0.17648226855355226], [0.18111940000368504, 0.14858255238235615, 0.2946372722123345, 0.17563384097446805, 0.31101553100085433, 0.1552409468142978, 0.29686408126750685, 0.34359717325947814], [0.3506127619205063, 0.3765412109031062, 0.2167301601221788, 0.18558152738824035, 0.12979909030439513, 0.23786629945006021, 0.1516315851716671, 0.2259948512179227], [0.16448111254160305, 0.19748412695115006, 0.2264473466279008, 0.2549451886495146, 0.16997711527776319, 0.24055530309943618, 0.2855372202939363, 0.36277114365338525]]
        self.hiddenweight =  [[0.31010654067936777], [0.32078728176744586], [0.11814876193961832], [0.2368336297243779], [0.27891353313921], [0.35834459266758023], [0.1375127735333306], [0.198556683543744]]

        self.bias_hiddenweight =    [[0.3376963474675446]]

        #hidden node 10
        # input
        # weight..
        # [[0.2883928297147189, 0.15960282017051908, 0.3169067445678515, 0.3415236509720604, 0.3838660546612602,
        #   0.33278247760765406, 0.12147268338858688, 0.3625693562162464, 0.1653387348995592, 0.13919781875531617],
        #  [0.14618452404542548, 0.12133767572703277, 0.35964873699788513, 0.2417940448952814, 0.3687657798073608,
        #   0.22577749171968797, 0.228742267444084, 0.13905088692726983, 0.35344814743394437, 0.27064737160582486],
        #  [0.25965889552350563, 0.34588379805253805, 0.12794844095530378, 0.1534726575412353, 0.22508268649039237,
        #   0.37468825458458266, 0.11823151976349361, 0.34577516038917566, 0.27578388159885864, 0.17062748571701292],
        #  [0.20632166652611508, 0.3387374759242777, 0.3533586781497946, 0.2040274314053262, 0.31272824134835925,
        #   0.30510730297197763, 0.28843265905931104, 0.31515278389208423, 0.25719462857535746, 0.21823121472386214],
        #  [0.20816492276274828, 0.15966175077803155, 0.15037808134183414, 0.15531666165694116, 0.23575645127139014,
        #   0.1493649062601548, 0.2942612605676035, 0.3263220758155855, 0.3848006697346352, 0.17765903878458605]]
        # Hidden
        # weight..
        # [[0.2083184174919976], [0.2820146855266952], [0.1667457260638238], [0.17137080460812476], [0.2930949408409219],
        #  [0.22459270252154695], [0.16145525337033517], [0.11230548734420544], [0.3495172504961429],
        #  [0.35277437372243314]]
        # bias
        # hidden
        # [[0.3530413092406818]]















        self.bias = [[1.0]]


        # make array of node
        self.input_array = [1.0] * self.inputnode
        self.hidden_array = [1.0] * self.hiddennode
        self.output_array = [1.0] * self.outputnode

    def feedforward(self, datas,target,abc):
        a = [[1.0, 1.0]]
        # set value to input node
        for i in range(self.inputnode-1): #already set 1.0 to bias node
            self.input_array[i] = datas[i]

        # calculate the value in hidden layer
        for i in range(self.hiddennode):
            sum = 0.0
            for j in range(self.inputnode):
                sum = sum + self.inputweight[j][i] * self.input_array[j]
                # print self.input_array[j] * self.bias
                # sum = 2
            self.hidden_array[i] = signoid(sum)
        #
        # print "hidden node value"
        # print self.hidden_array



        # calculate value in output layer
        for i in range(self.outputnode):
            sum = 0.0
            bias_hiddenweight = self.bias_hiddenweight[i][0] * self.bias[0][0]
            sum = bias_hiddenweight
            for j in range(self.hiddennode):
                sum = sum + self.hiddenweight[j][i] * self.hidden_array[j]
            self.output_array[i] = signoid(sum)
        # print "Output is: "
        # print self.output_array

        #calculate error
        error = 0
        for k in range(self.outputnode):
            # partial_error = 0.5 * (target[abc] - self.output_array[k]) ** 2
            partial_error = (target[abc] - self.output_array[k])

            error = error + partial_error
        #
        # print "Error is...... " + str(error) + "...target is........" + str(target[abc]) + "..calculated output is.." + str(self.output_array[k])
        return error


    def backpropagate(self, target, abc):
        # find output delta
        temp = 1.0
        output_delta = [1.0] * self.outputnode
        # print "target is..........."
        # print target[abc]

        for i in range(self.outputnode):
            temp = target[abc] - self.output_array[i]
            output_delta[i] = temp * self.output_array[i] * (1 - self.output_array[i])

        # print "Output delta is: "
        # print output_delta

        # find hidden delta
        hidden_delta = [1.0] * self.hiddennode
        for i in range(self.hiddennode):
            del_in = 0.0
            for j in range(self.outputnode):
                del_in = del_in + output_delta[j] * self.hiddenweight[i][j]
            hidden_delta[i] = self.hidden_array[i] * (1 - self.hidden_array[i]) * del_in
        # print "Hidden delta"
        # print hidden_delta




        # update hidden weight
        for i in range(self.outputnode):
            learning_rate = 0.5
            for j in range(self.hiddennode):
                weight_inc = learning_rate * output_delta[i] * self.hidden_array[j]
                self.hiddenweight[j][i] = self.hiddenweight[j][i] + weight_inc
        # print "Updated hidden weight"
        # print self.hiddenweight

        # update bias weight
        for i in range(self.outputnode):
            weight_inc = learning_rate * output_delta[i]
            self.bias_hiddenweight[i][0] = self.bias_hiddenweight[i][0] * self.bias[0][0] +weight_inc

        # print "updated bias"
        # print self.bias_hiddenweight

        # # #update input weight
        for i in range(self.hiddennode):
            for j in range(self.inputnode):
                weight_inc = learning_rate * hidden_delta[i] * self.input_array[j]
                # print "Updated weight"
                # print weight_inc
                self.inputweight[j][i] = self.inputweight[j][i] + weight_inc

        # print "Updated input weight"
        # print self.inputweight
        #




    def final11(self, datas):
        # print "Final input weight........: "
        # print self.inputweight
        # print "Final hidden weight........."
        # print self.hiddenweight

        a = [[1.0, 1.0]]
        # set value to input node
        for i in range(self.inputnode - 1):  # already set 1.0 to bias node
            self.input_array[i] = datas[i]

        # calculate the value in hidden layer
        for i in range(self.hiddennode):
            sum = 0.0
            for j in range(self.inputnode):
                sum = sum + self.inputweight[j][i] * self.input_array[j]
            self.hidden_array[i] = signoid(sum)

        # calculate value in output layer
        for i in range(self.outputnode):
            sum = 0.0
            bias_hiddenweight = self.bias_hiddenweight[i][0] * self.bias[0][0]
            sum = bias_hiddenweight
            for j in range(self.hiddennode):
                sum = sum + self.hiddenweight[j][i] * self.hidden_array[j]
            self.output_array[i] = signoid(sum)
        # print "Output is: "
        # print self.output_array

        return self.output_array



    def accuracy(self,tar,out):
        acc = abs((tar - out))/tar

        return acc


# print list_weight(2,3)
# c = neuralnet(2, 2, 1)
# datas = [0,0]
#
# qw=1
# while qw<2:
#     qw = qw+1
#     print "Serial number: " + str(qw)
#     c.feedforward(datas)
#     c.backpropagate([0])
#

#
# print "output" + str(c.feedforward(datas))
# c.backpropagate([0])

# c.backpropagate([0])
# c.backpropagate([0])
# c.backpropagate([0])

#
# qw=1
# while qw<50001:
#     qw = qw+1
#     print "Serial number: " + str(qw)
#     c.feedforward(datas)
#     c.backpropagate([0])
# #
#
# datas = [1, 1]
# print "output 123123" + str(c.feedforward(datas))
#
# qw = 1
# while qw < 501:
#     qw = qw + 1
#     print "Serial number: " + str(qw)
#     c.feedforward(datas)
#     c.backpropagate([0])
#
# import matplotlib
# from matplotlib import pyplot as p
# p.plot([12,23],[2,4)]
# p.show()


