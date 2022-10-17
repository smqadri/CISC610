'''
Assignment 0: Programming Assessment

Write a program that:

- include a class that accepts a list of numbers on instantiation.

- in the class, write a method that recursively returns the upper bound (maximum), and

- write another method that iteratively find the lower bound (minimum)_.  

- next create a main function area that reads in the contents from a .CSV file to create an array or list data structure. That data structure should be passed to the class you just developed.
'''


class findRecursive:        # Class that accepts a list of numbers on instantiation.
    def __init__(self, list, n):
        self.list = list
        self.n = n

    def maxRec(self):   # a method that returns the upper bound (maximum)
        return self.findMaxRec(self.list, self.n)

    def findMaxRec(self, list, n):   # a method that recursively finds the upper bound (maximum)
        if (n == 1):
            return list[0]
        return max(list[n - 1], self.findMaxRec(list, n - 1))

    def minRec(self):  # method that returns the lower bound (minimum)
        return self.findMinRec(self.list, self.n)

    def findMinRec(self, list, n):  # method that iteratively finds the lower bound (minimum)
        if (n == 1):
            return list[0]
        return min(list[n - 1], self.findMinRec(list, n - 1))
       
list1 = [1,2,3,4,5,66,7]  
    
myFindRec = findRecursive(list1, len(list1))        # Instantiating the class and passing the list
  
print("Finding the upper bound (maximum) recursively and the lower bound (minimum) recursively from the list: \n", list1, "\n")

print("The maximum number in the list is: ", myFindRec.maxRec())
print("The minimum number in the list is: ", myFindRec.minRec())

def main():   # main function area that reads in the contents from a .CSV file to create an array or list data structure. That data structure should be passed to the class you just developed.
    import csv
    
    print("\n\nReading the CSV and finding the upper bound (maximum) recursively and the lower bound (minimum) recursively from the imported list.\n")
    
    myFile = open("random_numbers.csv", "r", encoding="utf-8-sig")   # Read csv file. It has UTF-8 with signature encoded BOM https://docs.python.org/3.7/library/codecs.html#encodings-and-unicode
    
    
    dataList = csv.reader(myFile)       # Read csv file into list 
    list2 = []
    for inner_list in dataList:     # Converting the strings into integers Python
        for string in inner_list:
            list2.append(int(string))

    myFindRec = findRecursive(list2, len(list2))        # Instantiating the class and passing the list imported from the CSV file

    print("The maximum number in the CSV list is: ", myFindRec.maxRec())
    print("The minimum number in the CSV list is: ", myFindRec.minRec())


if __name__ == '__main__':
    main()
