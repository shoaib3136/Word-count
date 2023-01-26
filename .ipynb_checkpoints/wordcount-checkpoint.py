'''
Developed by: Shaik Shoaib Nawaz.
Reference Number:- 22005600.
'''
count =0
with open('myfile.txt','r') as test:
    for i in test:
        word = i.split()
        count+=len(word)
print('The number of words in the file myfile.txt are :',count)