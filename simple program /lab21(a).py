list_A = [10, 20, 30, 40, 50]
list_B = [60, 70, 80, 90, 20]

print("Original lists:")
print("List A:", list_A)
print("List B:", list_B)

temp = list_A[2]
list_A[2] = list_B[1]
list_B[1] = temp

print("\nLists after swapping a single element:")
print("List A' (swapped):", list_A)
print("List B' (swapped):", list_B)
