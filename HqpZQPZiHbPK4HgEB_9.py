"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

# this works fine and is really a good algorithm 
#num=6483074830
#from IPython.core.debugger import set_trace
def maxmin(num):
    def mini(num):
        min_lst=list(str(num))
        zeros_list=[]
        for i in range(len(min_lst)):
            if min_lst[i]=='0':
                zeros_list.append(i)
        while '0' in min_lst:
            min_lst.remove('0')
        #set_trace()
        k=0
        mylst=min_lst[:]
        for i in range(len(min_lst)):
            if mylst[0]==min(mylst) and k==0:
​
                for i in zeros_list:
                    min_lst.insert(i,'0')
                mylst=min_lst[1:]
                k=1
            elif mylst[0]==min(mylst):
                mylst=mylst[1:]
​
            else:
                if mylst.count(min(mylst))<2 :    # 
                    temp=min_lst[i]               # 4
                    idx_min=mylst.index(min(mylst))   #2 
                    min_lst[i]=min(mylst)     # min_lst[2]==0
                    min_lst[i+idx_min]=temp   # min_lst[4]=4
                    break
                if  mylst.count(min(mylst))>1:
                    #mylst[::-1].index(min(mylst))
                    temp=min_lst[i]
                    idx_min=len(mylst)-mylst[::-1].index(min(mylst))-1   # len(l)-l[::-1].index(min(l))-1
                    min_lst[i]=min(mylst)
                    min_lst[i+idx_min]=temp
                    break
        if k==0:
            for i in zeros_list:
                min_lst.insert(i,'0')
        return int(''.join(min_lst))
    def maxi(num):
        max_lst=list(str(num))
        max_lst
        mylst=max_lst[:]
        ind=0
        for i in range(len(max_lst)):
            if mylst[0]==max(mylst):
                mylst=mylst[1:]
            else:
                if mylst.count(max(mylst))<2 :    # 
                    temp=max_lst[i]               # 4
                    idx_max=mylst.index(max(mylst))   #2 
                    max_lst[i]=max(mylst)     # min_lst[2]==0
                    max_lst[i+idx_max]=temp   # min_lst[4]=4
                    break
                if  mylst.count(max(mylst))>1:
                    #mylst[::-1].index(min(mylst))
                    temp=max_lst[i]
                    idx_max=len(mylst)-mylst[::-1].index(max(mylst))-1   # len(l)-l[::-1].index(min(l))-1
                    max_lst[i]=max(mylst)
                    max_lst[i+idx_max]=temp
                    break
        return int(''.join(max_lst))
    return (maxi(num),mini(num))
#print(maxmin(190015878798001))

