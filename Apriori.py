import numpy as np
import ast
from itertools import combinations

def Apriori(support_input, confidence_input):
    tot_count = 0;
    data = np.loadtxt('associationruletestdata.txt', dtype = 'string', delimiter = '\t')
    total_Transactions = data.shape[0]
    for i in range(0, data.shape[1] - 1):
        for j in range(0, data.shape[0] ):
            data[i][j] = "G" + str(j+1) + "_" + data[i][j]
    Data_sets = list(map(set, data))


    c1, count = np.unique(data, return_counts = True)
    c1_frozen = c1
    c1_dict = dict(zip(c1_frozen, count))
    l1 = c1_dict

    #
    #The keepfrequentsets function keeps only the frequent itemsets and eliminates the itemsets
    #that do not satisfy the minimum support condition
    #
    def keepfrequentsets(Dc,minSup):
        eliminated_itemsets = []
        for key, value in Dc.items():
            if(float(value)/float(total_Transactions) < minSup):
                del Dc[key]
    #
    #The findcount function takes Ck as a parameter and returns the number of times each
    #itemset occurs in the given data
    #
    def findcount(Ck,k):
        if k == 2:
            Ck_sets = set(Ck)
        else:
            Ck_sets = Ck
        Ck_count = {}
        Ck_sets = sorted(Ck_sets)
        list1 = []
        list2 = []
        for c in Ck_sets:
            k = 0
            c1 = set(c)
            for row in Data_sets:
                if c1.issubset(set(row)):
                    k = k+1
            c = sorted(c)
            c = tuple(c)

            list1.append(k)
            list2.append(c)
        list2 = tuple(list2)
        list1 = tuple(list1)
        Ck_count = dict(zip(list2,list1))
        return Ck_count
    #
    #The createCk function takes Dc as a parameter which is a list of itemsets
    #It returns a list with all the possible combinations of itemsets from Dc
    #
    def createCk(Dc, k):
        list_frequent = []
        list_frequent1 = []
        list_frequent2 = []
        for key in Dc:
            list_frequent.append(key)
        if k == 2:
            Ck_result = []
            Ck_result = list(combinations(list_frequent,2))
        else:
            Ck_result = []
            for i in range (0, len(list_frequent)):
                for j in range(i + 1, len(list_frequent)):
                    list_frequent1 = list(list_frequent[i])
                    list_frequent2 = list(list_frequent[j])
                    list_frequent1.sort()
                    list_frequent2.sort()
                    if(list_frequent1[: k -2] == list_frequent2[: k - 2]):
                            list_frequent1 = set(list_frequent1)
                            list_frequent2 = set(list_frequent2)
                            union_result = (list_frequent1 | list_frequent2)
                            union_result = list(union_result)
                            Ck_result.append(union_result)
        return Ck_result

    #
    #Call keepfrequentsets and obtain L1
    #Populate dict_single_elements which is a list of single elements
    #and it's respective count
    #
    #
    keepfrequentsets(l1, support_input)
    no_of_frequent_itemsets = len(l1)
    print "Number of length 1 frequent itemsets generated : " + str(len(l1))

    allFreqItems = []
    L = l1
    list_single_elements = l1
    list_single_elements_tup = []
    list_single_elements_count = []
    for i in list_single_elements:
        list_single_elements_tup.append((i,))
        list_single_elements_count.append(list_single_elements.get(i))
    dict_single_elements = dict(zip(list_single_elements_tup,list_single_elements_count))

    tot_count = tot_count + len(l1)

    k = 2

    while (len(L) > 0):
        Ck = createCk(L, k)
        Lk = findcount(Ck,k)
        keepfrequentsets(Lk, support_input)   #Lk is a dictionary with frequent itemsets along with their count
        print "Number of length " + str(k) + " frequent itemsets generated : " + str(len(Lk))
        tot_count = tot_count + len(Lk)
        allFreqItems.append(Lk)
        L = Lk
        k += 1

    print "Total number of frequent itemsets generated : " + str(tot_count)
    #******************************************************

    response = raw_input("Enter template type:")

    if response == "1":
                response_1 = raw_input("Enter query:")
                part_1,condition_1,attributes_required = response_1.split ("/")
                print part_1
                print condition_1
                print attributes_required
                list1 =[]
                list1 = attributes_required.split(",")
                list1 = sorted(list1)
                list1 = tuple(list1)
                print list1

    if response == "2":
                response_2 = raw_input("Enter query :")
                part_1,condition_1,length_1 = response_2.split ("/")
                #print part_1
                length_1 = int(length_1)
                #condition_2 = string(condition_2)
                #print type(length_1)


    if response == "3":
                response_3 = raw_input("Type query type:")
                type_1,operation,type_2 = response_3.split("/")
                print operation
                if type_1 == "1" :
                          response_1 = raw_input("Enter query :")
                          part_1,condition_1,attributes_required = response_1.split ("/")
                          print part_1
                          print condition_1
                          print attributes_required
                          list1 =[]
                          list1 = attributes_required.split(",")
                          list1 = sorted(list1)
                          list1 = tuple(list1)
                          print list1

                if type_1 == "2":
                          response_2 = raw_input("Enter query :")
                          part_1,condition_1,length_1 = response_2.split ("/")
                          print part_1
                          length_1 = int(length_1)
                          print type(length_1)
                if type_2 == "1" :
                          response_3 = raw_input("Enter query :")
                          part_2,condition_2,attributes_required = response_3.split ("/")
                          print part_2
                          print condition_2
                          print attributes_required
                          list2 =[]
                          list2 = attributes_required.split(",")
                          list2 = sorted(list2)
                          list2 = tuple(list2)
                          print list2

                if type_2 == "2":
                        response_4 = raw_input("Enter query :")
                        part_2,condition_2,length_2 = response_4.split ("/")
                        print part_2
                        length_2 = int(length_2)
                        print type(length_2)

    def template_1(item,body,head,part,condition,locallist1):
        if part == "RULE":
            if condition == "NONE":

                item = list(item)

                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in item:
                            return False
                return True
            if condition == "ANY":
                item = list(item)

                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in item:
                            return True
                return False
            if condition == "1":
                item = list(item)

                attributes_required = list(locallist1)
                counter = 0
                for i in attributes_required:
                    if i in item:
                        counter = counter +1
                if counter == 1:
                    return True
                else:
                    return False


        if part == "BODY":
            if condition == "NONE":

                body = list(body)

                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in body:
                            return False
                return True
            if condition == "ANY":
                body = list(body)

                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in body:
                            return True
                return False
            if condition == "1":
                body = list(body)

                attributes_required = list(locallist1)
                counter = 0
                for i in attributes_required:
                    if i in body:
                        counter = counter +1
                if counter == 1:
                    return True
                else:
                    return False

        if part == "HEAD":
            if condition == "NONE":

                head = list(head)
                #print item
                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in head:
                            return False
                return True
            if condition == "ANY":
                head = list(head)

                attributes_required = list(locallist1)
                for i in attributes_required:
                    if i in head:
                            return True
                return False
            if condition == "1":
                head = list(head)

                attributes_required = list(locallist1)
                counter = 0
                for i in attributes_required:
                    if i in head:
                        counter = counter +1
                if counter == 1:
                    return True
                else:
                    return False

    def template_2(item,body,head,localpart,locallen,localcondition):
            if localcondition == "==":

                if localpart == "RULE":

                    if len(item) == locallen:

                        return True
                if localpart == "BODY":
                    if len(body) == locallen:
                        return True
                if localpart == "HEAD":
                    if len(head) == locallen:
                        return True
                return False
            if localcondition == ">=":
                if localpart == "RULE":

                    if len(item) >= locallen:
                        return True
                if localpart == "BODY":
                    if len(body) >= locallen:
                        return True
                if localpart == "HEAD":
                    if len(head) >= locallen:
                        return True
                return False
            if localcondition == "<=":
                if localpart == "RULE":

                    if len(item) <= locallen:
                        return True
                if localpart == "BODY":
                    if len(body) <= locallen:
                        return True
                if localpart == "HEAD":
                    if len(head) <= locallen:
                        return True
                return False

    def check_template(response,item,body,head):
        if response == "1":
            k = template_1(item,body,head,part_1,condition_1,list1)
            return k
        if response == "2":

            k = template_2(item,body,head,part_1,length_1,condition_1)

            return k
        if response == "3":
            if type_1 == "1":
                k1 = template_1(item,body,head,part_1,condition_1,list1)
            if type_1 == "2":
                k1 = template_2(item,body,head,part_1,length_1,condition_1)
            if type_2 == "1":
                k2 = template_1(item,body,head,part_2,condition_2,list2)
            if type_2 == "2":
                k2 = template_2(item,body,head,part_2,length_2,condition_2)
            if operation == "AND":
                if (k1) and (k2):
                    return True
                else:
                    return False
            if operation == "OR":
                if (k1) or (k2):
                    return True
                else:
                    return False

    #******************************************************

    def calConfidence(item, body):

        if(len(item) == 1):
            if item in dict_single_elements:
                item_count = dict_single_elements.get(item)
        if(len(body) == 1):
            if body in dict_single_elements:
                body_count = dict_single_elements.get(body)
        for i in range(len(allFreqItems)):

            if item in allFreqItems[i]:
                item_count = allFreqItems[i].get(item)
            if body in allFreqItems[i]:
                body_count = allFreqItems[i].get(body)
        confidence = float(item_count) / float(body_count)
        return confidence

    no_of_rules = 0
    for i in range(len(allFreqItems)):
        for item in allFreqItems[i]:
                k = len(item) - 1
                while(k > 0):
                    list_body = list(combinations(item, k))
                    k = k - 1
                    l_h = []
                    for index in range (len(list_body)):
                        list_head = tuple(set(item) - set(list_body[index]))
                        l_h.append(list_head)
                        item = sorted(item)
                        list_body[index] = sorted(list_body[index])
                        item = tuple(item)
                        list_body[index] = tuple(list_body[index])
                        error_counter =0
                        if(calConfidence(item, list_body[index]) >= confidence_input):

                            if check_template(response,item,list_body[index],list_head):

                                if len(list_body[index]) == 1:
                                    list_body[index] = list_body[index][0]
                                if len(list_head) == 1:
                                    list_head = list_head[0]
                                print str(list_body[index]) + "->" + str(list_head)
                                no_of_rules = no_of_rules + 1

    print "Total number of rules generated for query : " + str(no_of_rules)


support_value = float(raw_input("Enter support:"))
confidence_value = float(raw_input("Enter confidence:"))
Apriori(support_value, confidence_value)
