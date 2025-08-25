list_A = [10, 20, 30, 40, 50]
list_B = [60, 70, 80, 90, 20]

print("Original lists:")
print("List A:", list_A)
print("List B:", list_B)

list_A[0], list_B[4] = list_B[4], list_A[0]

list_A[1], list_B[0] = list_B[0], list_A[1]

print("\nLists after swapping elements as per part III of the image:")
print("List A' (swapped):", list_A)
print("List B' (swapped):", list_B)
