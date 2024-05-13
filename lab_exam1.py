def counter(num, target):
    count = 0
    for i in range(len(num)):
        if target == num[i] :
            count += 1
    return count

def main():
     num = []
     n = int(input("Enter the number of elements in the array: "))
     print("Enter the elements of the array:")
     for i in range(n):
        num.append(int(input()))

     target = int(input("Enter Target num: "))

     num_occured = counter(num, target)

     if num_occured > 0:
         print(f" {target} is found in the array {num_occured} times.")
        
     else:
        print(f"The number {target} is not found in the array.")


main()



    
