import pandas as pd
###########################
#Read sample data
###########################
data = pd.read_csv('sample.csv')
rows, cols = data.shape
#mapper = {'A':1, 'C':2, 'G':3, 'T':4, '.':5, 'GGG':6, 'AAC':7}
#string = ['A','C','G','T','.','GGG','AAC']
######################################
#declare map and necessary variables
######################################
mapper = {}
string = []
count = 0
####################################
#map nucleotides with number codes
####################################
for i in range(0,rows):
    if data['refvar'][i] not in mapper.keys():
        count += 1
        mapper[data['refvar'][i]] = count
        string.append((data['refvar'][i],count))
        
    if data['qvar'][i] not in mapper.keys():
        count += 1
        mapper[data['qvar'][i]] = count
        string.append((data['qvar'][i],count))
###################################
#replace nucleotides with codes
###################################
for i,j in string:
    data['refvar'].replace(i, mapper[i], inplace=True)
    data['qvar'].replace(i, mapper[i], inplace=True)
##########################
#Save the files
##########################
data.to_csv('encoded.csv',index=False)
dict = {'Tags': string}          
df = pd.DataFrame(dict)  
df.to_csv('tags.csv',index=False) #keep track of replaced nucleotides to get back them