def mergesort(num):
    if len(num) > 1:
        middle = len(num)//2
        left = num[:middle]
        right = num[middle:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                num[k] = left[i]
                i+=1
            else:
                num[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            num[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            num[k] = right[j]
            j+=1
            k+=1
    