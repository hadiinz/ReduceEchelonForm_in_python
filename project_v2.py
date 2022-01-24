import numpy as np


def reduceRowEchlonForm(A):
    m, n = A.shape
    k=0
    l =0
    while(0<= k < m and 0<= l < n):

        max = 0
        max_row = 0
        for i in range(k, m):
            if abs(A[i,l])>= max :
                max = abs(A[i,l])
                max_row = i

        ith_row = A[max_row].copy()
        A[max_row] = A[k]
        A[k] = ith_row

        if A[k][l] == 0:
            l+= 1;
        else:
            A[k] = A[k] / A[k,l]
            for i in range(0,m):
                if i == k : continue
                else:
                    A[i] = A[i] - ( A[i][l] / A[k][l] ) * A[k]

            k += 1;
            l += 1;

# def calculate_x(A):
#     m, n = A.shape
#     flag = False
#     if m< n-1 :
#         flag = True
#
#     X = []
#
#     if flag:
#         s2 = []
#         num =n-1-m
#         for i in range(num):
#             s2.append(m+i)
#         for i in range(m):
#             if A[i][i] == 1 :
#                 s1 = A[i][n-1]
#                 for j in range(len(s2)) :
#                     s1 -= 10*A[i][s2[j]]
#                 X.append(s1)
#         for i in range(num):
#             X.append(10)
#     else :
#         for i in range(n-1):
#             if A[i][i] == 1 :
#                 X.append(A[i][n-1])
#
#
#     for i in range(len(X)):
#         print("X" + str(i + 1) + " = " + str(X[i]), end="\n")

def calculate_x(A):
    m, n = A.shape

    if m<n-1 :
        for i in range(m , n-1):
            arr = [0] * n
            row = np.array(arr)
            A = np.vstack([A, row])
            m+=1

    flag_pivot_column = np.empty((n), dtype=bool)
    flag_pivot_column.fill(0)
    flag_zero_row = np.empty((m), dtype=bool)
    flag_zero_row.fill(1)

    for i in range(0, m):
        for j in range(0, n):
            if A[i][j] != 0 and j != n-1:
                flag_zero_row[i] = False
                flag_pivot_column[j] = True
                break

    for i in range(0, m):
        for j in range(0, n):
            if flag_zero_row[i] == True:
                if flag_pivot_column[j] == False:
                    if A[i][j] == 0 and j != n - 1:
                        A[i][j] = 1
                        A[i][n - 1] = 10
                        flag_pivot_column[j] = True
                        flag_zero_row[i] = False


    class_label = A[:, -1]
    dataset = A[:, :-1]
    y = np.linalg.solve(dataset,class_label)
    for i in range(m):
        print("X"+str(i+1)+" = "+str(y[i]), end="\n")

m,n = [int(x) for x in input().split()]
A = np.empty((m,n), float)
for i in range(m):
        A[i] = [float(x) for x in input().split()]

reduceRowEchlonForm(A)

for i in range(0,m):
    for j in range(0,n):
        print(A[i][j],end=" ")
    print()

calculate_x(A)
