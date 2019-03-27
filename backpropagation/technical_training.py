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

# def d_signoid(x):
#     return signoid(x) * (1 - signoid(x))

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


        # # hidden node 6
        # self.inputweight =   [[0.19208054089180404, 0.2027317921080124, 0.15015097971602503, 0.18263475515842692, 0.3711770758280898,
        #   0.14040396162318433],
        #  [0.16943235197588113, 0.33063219449714465, 0.32913444863365837, 0.11677731446082082, 0.3244448379079039,
        #   0.3232682824710681],
        #  [0.18548602421527882, 0.24267179473156605, 0.12614987585631116, 0.1666589588359519, 0.14902205490594228,
        #   0.13591294123002542],
        #  [0.22838810444093116, 0.10903800586269359, 0.32449211905442077, 0.18372524041873312, 0.19071683711880777,
        #   0.18370283411996868],
        #  [0.2425788515890456, 0.3921961683167774, 0.2207528595664466, 0.15760771271248908, 0.1502936865255997,
        #   0.24378981485404055]]

        # self.hiddenweight = [[0.2470334794602744], [0.2996208564675664], [0.2154854099905709], [0.16768417958002663], [0.2704761852836417],
        #  [0.253139198651516]]
        #
        # self.bias_hiddenweight = [[0.1533869724892909]]
        #




        #hidden node 10
        # Input
        # weight
        # [[0.24113345172961445, 0.22412507685287808, 0.2605017434389806, 0.27983202270233465, 0.3375449228928644,
        #   0.159390111516925, 0.33057352018519803, 0.16171943844107795, 0.235741725948484, 0.14244555781399576],
        #  [0.2992636791387883, 0.23619022654522454, 0.20305636881877515, 0.3421042775610793, 0.3288879695572272,
        #   0.39225651208085743, 0.10730287196370439, 0.3881313255632324, 0.157577530309176, 0.3683816931040963],
        #  [0.1478837566439102, 0.2165211095739314, 0.10886055106619594, 0.25780862835224205, 0.3849028943340024,
        #   0.19782833320826398, 0.2542291710207444, 0.24593226777597404, 0.2851989329399919, 0.2315541582977414],
        #  [0.3899445960977387, 0.2667213403582484, 0.33373525871145443, 0.38595135010958803, 0.31157611952792796,
        #   0.3648704361022097, 0.1480756836507201, 0.3294968366215537, 0.286844381033471, 0.21969429959366438],
        #  [0.29989113686171853, 0.19920048184731465, 0.14411586572963622, 0.1996910645325043, 0.3350395602101593,
        #   0.2682933291380748, 0.14654485709336695, 0.2938230381641952, 0.2896439838482676, 0.2791718797032302]]
        # hidden
        # weight
        # [[0.17112063178048686], [0.34961874361030587], [0.1589535389666073], [0.1901770228308412],
        #  [0.17136688199840996], [0.26690591691171706], [0.36569147634710575], [0.3817468798513416],
        #  [0.14616874360828447], [0.28269029732356116]]
        # bias
        # weight,, . [[0.2822832238348835]]

        # hidden node 6
        # Input
        # weight
        # [[0.19208054089180404, 0.2027317921080124, 0.15015097971602503, 0.18263475515842692, 0.3711770758280898,
        #   0.14040396162318433],
        #  [0.16943235197588113, 0.33063219449714465, 0.32913444863365837, 0.11677731446082082, 0.3244448379079039,
        #   0.3232682824710681],
        #  [0.18548602421527882, 0.24267179473156605, 0.12614987585631116, 0.1666589588359519, 0.14902205490594228,
        #   0.13591294123002542],
        #  [0.22838810444093116, 0.10903800586269359, 0.32449211905442077, 0.18372524041873312, 0.19071683711880777,
        #   0.18370283411996868],
        #  [0.2425788515890456, 0.3921961683167774, 0.2207528595664466, 0.15760771271248908, 0.1502936865255997,
        #   0.24378981485404055]]
        # hidden
        # weight
        # [[0.2470334794602744], [0.2996208564675664], [0.2154854099905709], [0.16768417958002663], [0.2704761852836417],
        #  [0.253139198651516]]
        # bias
        # weight,, .
        # [[0.1533869724892909]]

        #hidden node 4
        # self.inputweight =        [[0.3080070394168448, 0.3863543827420006, 0.13904373055161276, 0.17416439956750118],
        #  [0.1661785561615567, 0.20989159618985473, 0.11667389682393814, 0.3926054971327322],
        #  [0.3075729867104649, 0.12760279069735245, 0.21164117122132742, 0.36782283923411385],
        #  [0.1092433896987114, 0.3441365556500089, 0.11431631761411128, 0.39626656206157584],
        #  [0.1514830980464342, 0.2987124334098422, 0.22699085216723325, 0.3784744039883058]]
        # # hidden
        # # weight
        # self.hiddenweight = [[0.1899937134744334], [0.18214897505737843], [0.3429989159449267], [0.25307567211569776]]
        # self.bias_hiddenweight=  [[0.3128501048715797]]

        # Total
        # Iteration..................
        # .25921

        # hidden node 8
        self.inputweight =[[0.3171579045473818, 0.2752772355671475, 0.35290161088279826, 0.16828342803080942, 0.17600361128349057,
          0.10217502234846108, 0.36788661963491054, 0.39805951495369307],
         [0.32051651883692345, 0.12081690688380883, 0.281649731184927, 0.238700084908729, 0.3917099742837141,
          0.2506347884107924, 0.2765585695618722, 0.1945322733078481],
         [0.23031531160166224, 0.2615046820013361, 0.29731932630385743, 0.36773842355370956, 0.3158394111239722,
          0.304896589527408, 0.39297198333637007, 0.3936267809703363],
         [0.19002074573619687, 0.37137023669560754, 0.20743360697751967, 0.3204732970484689, 0.3722301978677144,
          0.2764385182374439, 0.3834266033156757, 0.25311006399019187],
         [0.15391872678609853, 0.24162767657689596, 0.26356100951324296, 0.12946588063963088, 0.352060832425647,
          0.12006568571041418, 0.3082612621418556, 0.3797527283773363]]



        self.hiddenweight =[[0.3845960301727155], [0.11879180341867662], [0.16386481509015127], [0.3856898140213345], [0.2503881102119231],
         [0.16034620280882927], [0.3674043053052227], [0.3002543271222755]]
        self.bias_hiddenweight =[[0.24931988925141724]]


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


