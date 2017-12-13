
from numpy import *
import csv

import time

import FPTreeBuilder
import FPTreeMiner
from apyori import apriori

def associationAnalysis():
    transactions = [[]]
    formedTransactions = [[]]

    with open('Consumer_Complaints.csv', 'rb') as csvfile:
        rowreader = csv.reader(csvfile)
        for row in rowreader:
            transactions.append(row[1:])
        transactions.remove([])
        headerList = transactions[0]

        print headerList

    for transaction in transactions:
        trans = []
        for i in range(len(transaction)):
            item = transaction[i]
            attributeName = headerList[i]
            trans.append(attributeName + ':' + item)

        formedTransactions.append(trans)

    formedTransactions = formedTransactions[2:]

    # targetItem1 = 'Consumer disputed?:No'
    # targetItem2 = 'Consumer disputed?:Yes'
    #
    # min_sup = 100000
    # headerTable = {}
    # counts = []
    # 
    # print('Using FP-Growth algorithm to find the frequent pattern in given census:(min_sup is 150 by default)')
    # start_timeFP = time.time()
    # fpTreeBuilder = FPTreeBuilder.FPTreeBuilder(formedTransactions, min_sup, counts, headerTable)
    # FPTreeMiner.FPTreeMiner(targetItem1, targetItem2, fpTreeBuilder.tree, min_sup, headerTable)
    # print("---FP-Growth using %s seconds ---" % (time.time() - start_timeFP))

    
    print('Using Apriori library to find the frequent pattern in given transactions:')
    start_timeA = time.time()
    aprioriResults = list(apriori(formedTransactions,min_support=0.6,min_confidence = 0.9))
    print aprioriResults
    outputFile = open('06-09.text', "w")
    for i in aprioriResults:
        outputFile.write(str(i) + '\n')
    outputFile.close()
    print("---Apriori using %s seconds ---" % (time.time() - start_timeA))


if __name__ == '__main__':

    associationAnalysis()


