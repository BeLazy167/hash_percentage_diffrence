import hashlib
strA = 'Engineering is fun'
strB = 'engineering is fun'

def diff(str1,str2):
    count = 0
    x = ''
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count+=1
    return((count/len(str1))*100)

str1,str2 = hashlib.md5(strA.encode()).hexdigest(),hashlib.md5(strB.encode()).hexdigest()
str3,str4 = hashlib.sha1(strA.encode()).hexdigest(),hashlib.sha1(strB.encode()).hexdigest()
print('HASHES MD5: \n' + str1,str2)
print("PERCENTAGE DIFFRENCE MD5:" ,diff(str1,str2))
print('HASHES SHA1: \n' + str3,str4)
print("PERCENTAGE DIFFRENCE SHA:" ,diff(str3,str4))
