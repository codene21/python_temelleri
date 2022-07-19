fruits = {'orange', 'apple', 'banana'}
# print(fruits[0]) => indekslenemez

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])

fruits.remove('mango')
fruits.discard('apple')

print(fruits)

fruits.pop()

print(fruits)

myList = [1,2,3,3,3,4,4,4,5]
print(myList)
print(set(myList))