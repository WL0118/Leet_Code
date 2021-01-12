class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        Alen = len(A)
        arr = [0] * Alen
        count =  0 
        flag = 0
        for ind, ele in enumerate(A):
            #print(ind)
            flag = arr[ind]^flag
            
            if(ele^flag==0):
                if ind+K > Alen:
                    return -1
                #print("count")
                count+=1
                flag = flag^1
                if(ind+K<Alen):
                    arr[ind+K]=1

                
        return count

#         count=0
#         LengthA=len(A)
        
#         for ind in range(0,LengthA+1-K):
#             #print(ind,'ind')
            
#             if A[ind]==0:

#                 A[ind:ind+K]=map(lambda x:(x+1)%2,A[ind:ind+K])

#                 #A[ind:ind+K]^=A[ind:ind+K]             
                
#                 #print(A[ind:ind+K])
#                 count+=1

#         if sum(A[LengthA-K:])==K:
#             return count
#         else:
#             return -1
