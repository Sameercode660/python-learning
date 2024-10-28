# Write a Python function that takes a list and removes duplicate items, returning a list with only unique items in the original order.

def removeDuplicates(l1):
      unique_items = []

      for item in l1:
        if item not in unique_items: 
            unique_items.append(item)
      return unique_items

print(removeDuplicates([1,2,3,4,4,4,4,5,5,5]))


l2 = [1,2,3,0,2]

l2 = list(set(l2))

print(l2)
    