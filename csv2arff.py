import sys
import csv
import collections

# Main function
def main():
    if len(sys.argv) < 2:
        print('Give the csv filename')
    else:
        csv2arff(sys.argv[1])

# Function to convert csv to arff
def csv2arff(csvfilename):
    with open(csvfilename, 'r') as csvfile:
        filename = sys.argv[1][0:len(sys.argv) - 6]
        with open(filename+".arff", 'w') as arfffile:
            reader = csv.DictReader(csvfile)
            headers = collections.OrderedDict()
            for header in reader.fieldnames:
                headers[header] = set()
            # Get the distinct values for each column
            for row in reader:
                for index in headers.keys():
                    if row[index] != '' and not(row[index].isdigit()):
                        headers[index].add(row[index])
            arfffile.write('@relation {}\n'.format(filename))
            print('@relation {}\n'.format(filename))
            # set attributes to the distinct values
            for index in headers.keys():
                headerstring = '@attribute ' + index
                if len(headers[index]) > 0:
                    headerAttrib = '{'
                    for ele in sorted(headers[index]):
                        headerAttrib += ele + ','
                    headerAttrib = '{}{}'.format(headerAttrib[0:len(headerAttrib)-1], '}')
                else:
                    headerAttrib = '{0, 1}'
                headerstring += ' {}\n'.format(headerAttrib)
                arfffile.write(headerstring)
                print(headerstring)
            arfffile.write('@data\n')
            print('@data\n')
            csvfile.seek(0, 0)
            csvfile.readline()
            csvrow = csv.reader(csvfile)
            # copy each row except the header to arff file
            for row in csvrow:
                rowstring = '{'
                for i,item in enumerate(row):
                    if i != 0 and item == '1':
                        rowstring += str(i-1)+' 1,'
                    # if item != '':
                    #     rowstring += '{},'.format(item)
                    # else:
                    #     rowstring += '?,'
                arfffile.write(rowstring[0:len(rowstring)-1]+'}\n')
                print(rowstring[0:len(rowstring)-1]+'}\n')


if __name__ == '__main__':
    main()
