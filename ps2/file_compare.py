'''
Tan Hao Qin 1000521
Tay Kang Sheng 1000591
Agrim Singh 1000748
'''

import sys

# Hash Values for words in New File
# HashCorruptedFile[i,j] = Hash value of lines i to j in Corrupted File
HashCorruptedFile = []

# Hash Values for words in Old File
# HashOriginalFile[i,j] = Hash value of lines i to j in Original File
HashOriginalFile = []

# Words in the Corrupted and Original File
wordsCorrupted = []
wordsOriginal = []

# n : number of lines in each file
n = 2 # default value


# variable to measure network transmission cost
cost=0






def compute_node_values():
    ''' in the first part of compute_hash_tree(), we computed HashOriginalFile[0][0], HashOriginalFile[1][1], HashOriginalFile[2][2].... etc
    
    Now, here in compute_node_values(), you have to calculate HashOriginalFile[i][j] where i < j
    So, HashOriginalFile[2][4] = hash_function(line 2-4 of corrupted file). It depends on your own has design. 
    
    For example, HashOriginalFile[2][4] can be = hash_function(hash_function(line 2)+2*hash_function(line 3)+3*hash_function(line 4)).... but it is good? Perhaps not. So, write your own hash function here! 
    '''

################ Part B Question 2: Complete the code here ###########


    base = 7
    def RecursiveOriginalHash(i,j):
        if i == j:
            HashOriginalFile[i][i] = base**i*HashOriginalFile[i][i]
        else:
            RecursiveOriginalHash(i,i+(j-i)/2)
            RecursiveOriginalHash(i+(j-i)/2+1,j)
            HashOriginalFile[i][j] = HashOriginalFile[i][i+(j-i)/2] + HashOriginalFile[i+(j-i)/2+1][j]
    def RecursiveCorruptedHash(i,j):
        if i == j:
            HashCorruptedFile[i][i] = base**i*HashCorruptedFile[i][i]
        else:
            RecursiveCorruptedHash(i,i+(j-i)/2)
            RecursiveCorruptedHash(i+(j-i)/2+1,j)
            HashCorruptedFile[i][j] = HashCorruptedFile[i][i+(j-i)/2] + HashCorruptedFile[i+(j-i)/2+1][j]
    RecursiveOriginalHash(0,n-1)
    RecursiveCorruptedHash(0,n-1)
    

def binary_check_hash(left,right):
    ''' performs binary search over the binary tree of hash values.
    search through the whole tree. 
    print "[binary_check_hash] found damaged content at line xx" for all damaged line found. 
    '''
    global cost

################# Part B Question 3: Complete the code here #########
    if left==right:
        if not compare(HashCorruptedFile[left][left],HashOriginalFile[left][left]):
            print "[naive_check_hash] found damaged content at line " + str(left)
    else:
        if not compare(HashCorruptedFile[left][right],HashOriginalFile[left][right]):
            binary_check_hash(left,left+(right-left)/2)
            binary_check_hash(left+(right-left)/2+1,right)
    
        
    












# read fileCorrupted and fileOriginal, save to wordsCorrupted and wordsOriginal
def read_files(fileCorrupted, fileOriginal):
    fCorrupted = open(fileCorrupted, 'r')
    fOriginal = open(fileOriginal, 'r')
    for line in fCorrupted:
        wordsCorrupted.append(line)
    for line in fOriginal:
        wordsOriginal.append(line)
    fCorrupted.close()
    fOriginal.close()




# Compute the hash values of the leaf nodes in the Hash Tree
def compute_hash_tree():
    for i in range(n):
        HashCorruptedFile.append([])
        HashOriginalFile.append([])
        for j in range(n):
            HashCorruptedFile[i].append(None)
            HashOriginalFile[i].append(None)

    for i in range(n):
        HashCorruptedFile[i][i] = hash_function(wordsCorrupted[i])
        HashOriginalFile[i][i] = hash_function(wordsOriginal[i])

    compute_node_values()



# compute the hash value of the string
def hash_function(s):
################# Part B Question 1: Complete the code here (just 1-2 line(s) should be enough!) #########
#naming variables required for the function    
    hashing_prime = 701    
    n = len(s)    
    hashvalue = 0    
# converting each character of a string into an integer and multiplying it by a base
    for i in range(n):
        hashvalue+=ord(s[i])*128**(n-1-i)                
    return hashvalue%hashing_prime


# compares the two hash values. total cost increase by 1
def compare(oldhash, newhash):
    global cost
    cost = cost + 1
    return oldhash == newhash



# naive hash check method, goes over all the lines and compares them.
def naive_check_hash(left,right):
    global cost
    for i in xrange(left,right+1):
        if not compare(HashCorruptedFile[i][i],HashOriginalFile[i][i]):
            print "[naive_check_hash] found damaged content at line " + str(i)



# performs the naive_check_hash algorithm and binary_check_hash algorithm.
# compares filename1 and filename2 with n lines each
# print out the cost

def file_compare(filename1, filename2, n1):
    global cost,n
    n=n1

    print "1. starting computation of hash tree..."
    read_files(filename1,filename2)
    compute_hash_tree()
    print "finished computation of hash tree\n"

    print "2. starting computation of naive_check_hash()..."
    cost = 0
    naive_check_hash(0,n-1)
    print "cost of navie_check_hash() =",cost,"\n"

    print "3. starting computation of binary_check_hash()..."
    cost = 0
    binary_check_hash(0,n-1)
    print "cost of binary_check_hash() =",cost,"\n"



if __name__ == "__main__":
    file_compare("file_corrupted1.txt","file_original1.txt", 1024)

