import heapq
#Since heapq is to do min Heap
#I did max heap by store the opposite number and sort using the min heap property
FirstCommand = input().split()                   
#The first line consists of two integer numbers m,k.
m, k = int(FirstCommand[0]),int(FirstCommand[1])

Arr = list(map(int,input().strip().split()))[:2*k]
#The second line consists of the 2k values in the initial set.

Arr.sort() #The array is sorted from small to large initally

#Two Heap connected with Arr with 2*k element
MinHeap = []
MaxHeap = []

#The following m lines each consists of the command of an operation.
for i in range(0,m):
    Operation = input().split() #Get the operation
    A = int(Operation[0])       #Fisrt is to find the type of the operation
    
    if (A==1):                  #Insert a value
        B = int(Operation[1])   #Get the insert value
        #Below is three cases
        #Case 1: Inserted value is smaller than the smallest number in Arr
        #Case 2: Inserted value is larger than the largest number in Arr
        #Case 3: Inserted value is between the value scope of the Arr
        if (B < Arr[0]):  #Case1
            #In Case1, we should divide the problem in to two cases
            #Sub Case1:len(MinHeap)==len(MaxHeap)
            #Sub Case2:len(MinHeap)<len(MaxHeap)
            #len(MaxHeap) always larger or equal to len(MinHeap) based on my design
            if (len(MinHeap)==len(MaxHeap)):
                heapq.heappush(MaxHeap,-B)
                #Then we just need to push the value in Maxheap and maintaining the Maxheap invariant
            elif (len(MinHeap)<len(MaxHeap)):
                #In order to make the balance, We need to fine-tune the array
                heapq.heappush(MinHeap,Arr[2*k-1])
                #Push the value in Minheap and maintaining the Maxheap invariant
                Arr.remove(Arr[2*k-1])
                #Remove the value pushed into the Minheap in Arr
                temp = -heapq.heappop(MaxHeap)
                #Small cases we need to take care. 
                #I didn't think of it at first and resulted in the error
                
                if (B>temp): #The inserted B smaller than the Arr[0] may larger than the max number in Maxheap
                    Arr.append(B)                  #Then we just need to append the B in Arr
                    heapq.heappush(MaxHeap,-temp)  #Push the temp back
                else:
                    Arr.append(temp)               #Otherwise, append the max number in maxheap
                    heapq.heappush(MaxHeap,-B)     #Insert the B in maxheap
                Arr.sort()                         #Sort the Arr again
                
        elif (B>Arr[2*k-1]):  #Case2
            #In Case2, we also should divide the problem in to two cases
            #Sub Case1:len(MinHeap)==len(MaxHeap)
            #Sub Case2:len(MinHeap)<len(MaxHeap)
            if (len(MinHeap)==len(MaxHeap)):
                #Small cases we need to take care. 
                #I didn't think of it at first and resulted in the error
                if (len(MinHeap)==0):              #When len(MinHeap)==len(MaxHeap)==0
                    heapq.heappush(MaxHeap,-Arr[0])#We need special handling
                    Arr.remove(Arr[0])             #We just need to remove the Arr[0]
                    Arr.append(B)                  #And insert the B directly into the Arr
                    Arr.sort()                     #Sort the Arr again
                else:
                    heapq.heappush(MaxHeap,-Arr[0])
                    Arr.remove(Arr[0])
                    
                    Number = heapq.heappop(MinHeap)
                    #Small cases we need to take care. 
                    #I didn't think of it at first and resulted in the error
                    if (B<Number): #The inserted B larger than the Arr[2*k-1] may smaller than the min number in Minheap
                        Arr.append(B)                  #Then we just need to append the B in Arr
                        heapq.heappush(MinHeap,Number) #Push the Number back
                    else:
                        Arr.append(Number)
                        heapq.heappush(MinHeap,B)
                    Arr.sort()
                    
            elif (len(MinHeap)<len(MaxHeap)):          #To make the balance
                heapq.heappush(MinHeap,B)              #We just need to push the B in the Min heap
        #Case3, we also should divide the problem in to two cases
        #Sub Case1:len(MinHeap)==len(MaxHeap)
        #Sub Case2:len(MinHeap)<len(MaxHeap)
        elif (len(MinHeap)==len(MaxHeap)):
            heapq.heappush(MaxHeap,-Arr[0])
            Arr.remove(Arr[0])
            Arr.append(B)
            Arr.sort()

        elif (len(MinHeap)<len(MaxHeap)):
            heapq.heappush(MinHeap,Arr[2*k-1])
            Arr.remove(Arr[2*k-1])
            Arr.append(B)
            Arr.sort()
        
    elif (A==2):    #Output all the median 2k values
        print(' '.join(map(str, Arr)))
        
    elif (A==3):    #Delete the p-th value among median 2k values
        B = int(Operation[1]) #Get the Pth value
        #Delete,Append and resort to maintain the 2k Arr
        #Also divided into two cases
        if (len(MinHeap)<len(MaxHeap)):
            Arr.remove(Arr[B-1])
            Arr.append(-heapq.heappop(MaxHeap))
            Arr.sort()
        elif (len(MinHeap)==len(MaxHeap)):
            Arr.remove(Arr[B-1])
            Arr.append(heapq.heappop(MinHeap))
            Arr.sort()
        
        
    
        


        
