import pandas as pd
##############################################################
#Read encoded files and tracked nucleotides in encode section
##############################################################
data = pd.read_csv('encoded.csv')
tags = pd.read_csv('tags.csv')
rows, cols = tags.shape
#mapper = {1:'A', 2:'C', 3:'G', 4:'T', 5:'.', 6:'GGG', 7:'AAC'}
#string = [1,2,3,4,5,6,7]
######################################
#declare map and necessary variables
######################################
mapper = {}
string = []

####################################
#map number codes with nucleotides
####################################
for i in range(0,rows):
    
    k,val = eval(tags['Tags'][i])
    mapper[val] = k
    string.append(val)
###################################
#replace codes with nucleotides
###################################
for i in string:
    data['refvar'].replace(i, mapper[i], inplace=True)
    data['qvar'].replace(i, mapper[i], inplace=True)
##########################
#Save the decoded files
##########################
data.to_csv('decoded.csv',index=False)
