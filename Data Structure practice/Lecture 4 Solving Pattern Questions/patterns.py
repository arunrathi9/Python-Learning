# pattern problems


def pattern1(n):
    '''
    Pattern1 (change with * for * pattern): 

    1 2 3 4
    1 2 3 4
    1 2 3 4
    1 2 3 4
    '''
    k = 0
    while(k<n):
        for i in range(n):
            print(i+1, end=" ")
        print()
        k += 1

def pattern2(n):
    '''
    Pattern2:
    4 3 2 1
    4 3 2 1
    4 3 2 1
    4 3 2 1
    '''
    k = 0
    while(k<n):
        i = n
        while(i>0):
            print(i, end=" ")
            i -= 1
        print()
        k += 1

def pattern3(n):
    '''
    Pattern 3:
    1 2 3
    4 5 6
    7 8 9
    '''
    count = 0
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            count += 1
            print(count, end=" ")
            j += 1
        print()
        i += 1

def pattern4(n):
    '''
    Pattern 4:
    *
    * *
    * * *
    * * * *
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<=i):
            print('*', end=" ")
            j += 1
        print()
        i += 1

def pattern5(n):
    '''
    Pattern 5:
    1
    2 2
    3 3 3
    4 4 4 4
    '''
    i = 1
    while(i <= n):
        j = 0
        while(j<i):
            print(i, end=" ")
            j += 1
        print()
        i += 1

def pattern6(n):
    '''
    Pattern 5:
    1
    2 3
    4 5 6
    7 8 9 10
    '''
    count = 1
    i = 1
    while(i <= n):
        j = 0
        while(j<i):
            print(count, end=" ")
            count += 1
            j += 1
        print()
        i += 1

def pattern7(n):
    '''
    Pattern 7:
    1
    2 3
    3 4 5
    4 5 6 7
    '''
    # i = 1
    # while(i <= n):
    #     j = 0
    #     count = i
    #     while(j<i):
    #         print(count, end=" ")
    #         count += 1
    #         j += 1
    #     print()
    #     i += 1

    # without using count
    i = 1
    while(i <= n):
        j = 0
        while(j<i):
            print(i+j, end=" ")
            j += 1
        print()
        i += 1

def pattern8(n):
    '''
    Pattern 8:
    1
    2 1
    3 2 1
    4 3 2 1
    '''
    i = 1
    while(i <= n):
        j = 0
        while(j<i):
            print(i-j, end=" ")
            j += 1
        print()
        i += 1

def pattern9(n):
    '''
    Pattern 9:
    A A A
    B B B
    C C C
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            print(chr(65+i), end=" ")
            j += 1
        print()
        i += 1

def pattern10(n):
    '''
    Pattern 10:
    A B C
    A B C
    A B C
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            print(chr(65+j), end=" ")
            j += 1
        print()
        i += 1

def pattern11(n):
    '''
    Pattern 10:
    A B C
    D E F
    G H I
    '''
    i = 0
    count = 0
    while(i < n):
        j = 0
        while(j<n):
            print(chr(65+count), end=" ")
            count += 1
            j += 1
        print()
        i += 1        

def pattern12(n):
    '''
    Pattern 12:
    A B C
    B C D
    C D E
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            print(chr(65+i+j), end=" ")
            j += 1
        print()
        i += 1

def pattern13(n):
    '''
    Pattern 13:
          *
        * *
      * * *
    * * * *
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            if j >= n-i-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            j += 1
        print()
        i += 1

def pattern14(n):
    '''
    Pattern 14:
    * * * *
    * * *
    * *
    *
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            if j >= n-i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
            j += 1
        print()
        i += 1

def pattern15(n):
    '''
    Pattern 15:
    * * * *
      * * *
        * *
          *
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n):
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
            j += 1
        print()
        i += 1

def pattern16(n):
    '''
    Pattern 16:
          1
        1 2 1   
      1 2 3 2 1
    1 2 3 4 3 2 1
    '''
    i = 0
    while(i < n):
        col = 0
        # first part
        j = 0
        while(j<n):
            if j >= n - i - 1:
                col += 1
                print(col, end=" ")
            else:
                print(" ", end=" ")  
            j += 1

        # second part
        k = 0
        while(k<i):
            col -= 1
            print(col, end=" ")
            k += 1

        print()
        i += 1

def pattern17(n):
    '''
    1 2 3 4 5 5 4 3 2 1
    1 2 3 4 * * 4 3 2 1
    1 2 3 * * * * 3 2 1
    1 2 * * * * * * 2 1
    1 * * * * * * * * 1
    '''
    i = 0
    while(i < n):
        j = 0
        while(j<n-i):
            print(j+1, end=" ")
            j += 1

        j = 0
        while(j<i*2):
            print("*", end=" ")
            j += 1
        
        j = 0
        while(j < n-i):
            print(n-j-i, end=" ")
            j += 1
        
        i += 1
        print()

pattern17(int(input()))