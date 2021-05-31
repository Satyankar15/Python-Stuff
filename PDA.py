from sys import exit
print("PDA TO TEST CONDITION a^ib^(i+j)c^j ")
pda = input("Input String: ")
count = []
count.append('$')
count.append('$')
flag = 0
ans = ''
#print("q0",end='')
ans = ans + 'q0'
for i in pda:
    if i == 'a' and flag == 0:
        count.append(i)
        #print("Stack :" + str(count))
        ans = ans + '-->q0'
    elif i =='b':
        if count.pop() != '$' and flag !=2:
            flag = 1
           # print("Stack :" + str(count))
        else:
            flag = 2
            count.append(i)
            #print("Stack :" +str(count))
        ans = ans + '-->q1'
    elif i=='c' and flag == 2:
        if count.pop() != '$' :
            #print("Stack :" + str(count))
            ans = ans + '-->q2'
        else:
            print("Rejected")
            exit()
    else:
        print("Rejected")
        exit()
if count.pop() == '$':
    ans = ans + '-->qf'
    print("Accepted")
else:
    print("Rejected as number of a is greater")
print(ans)