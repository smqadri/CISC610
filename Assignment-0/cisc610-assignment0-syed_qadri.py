'''
Assignment 0: Programming Assessment

Write a program that:

- include a class that accepts a list of numbers on instantiation.

- in the class, write a method that recursively returns the upper bound (maximum), and

- write another method that iteratively find the lower bound (minimum)_.  

- next create a main function area that reads in the contents from a .CSV file to create an array or list data structure. 
    That data structure should be passed to the class you just developed.
'''


class findRecursive:                # Class that accepts a list of numbers on instantiation.
    def __init__(self, list):       # The constructor of a class which takes the attribute values as 
                                    # input parameters and them initializes them
        self.list = list            # initialize the list attribute
        self.n = len(list)          # initialize the lists length attribute

    def maxRec(self):               # Method that returns the upper bound (maximum)
        return self.findMaxRec(self.list, self.n)

    def findMaxRec(self, list, n):  # Method that recursively finds the upper bound (maximum)
        if n == 1:
            return list[0]          # if the list has only one element, return that element
        else:
            return max(list[n - 1], self.findMaxRec(list, n - 1))   # if the list has more than one element, 
                                                                    # return the maximum of the last element 
                                                                    # and the recursive call of the method with 
                                                                    # the list and the n-1
         
    def minRec(self):               # method that returns the lower bound (minimum)
        return self.findMinRec(self.list, self.n)   

    def findMinRec(self, list, n):  # method that iteratively (for loop) finds the lower bound (minimum)
        minValue = list[0]          # initialize the minimum value to the first element of the list
        for i in list:              # for loop to find the minimum value
            if i < minValue:        # if the current element is less than the minimum value, update the minimum value
                minValue = i        # update the minimum value
        return minValue             # return the minimum value

myList = [1,2,3,4,5,66,7]                    # Initializing a list of numbers
    
myFindRec = findRecursive(myList)   # Instantiating the class and passing the list
  
print("Finding the upper bound (maximum) recursively and the lower bound (minimum) recursively from the list: \n", myList, "\n")

print("The maximum number in the list is: ", myFindRec.maxRec())    # Printing the maximum number in the list
print("The minimum number in the list is: ", myFindRec.minRec())    # Printing the minimum number in the list

def main():   # Main function area that reads in the contents from random_numbers.csv file to create an array or list data structure. 
              # That data structure should be passed to the class you just developed.
    import csv
    
    print("\n\nReading the CSV and finding the upper bound (maximum) recursively and the lower bound (minimum) recursively from the imported list.\n")
    
    myFile = open("random_numbers.csv", "r", encoding="utf-8-sig")      # Reading the csv file. It appears to be created using Windows encoding,
                                                                        # so using UTF-8 with signature (utf-8-sig) to resolve this BOM error.
                                                                        # https://docs.python.org/3.7/library/codecs.html#encodings-and-unicode
    
    
    dataList = csv.reader(myFile)               # Read csv file into list 
    csvList = []                                # Initialize an empty list
    
    for inner_list in dataList:                 # Converting the strings into integers Python
        for string in inner_list:
            csvList.append(int(string))

    myFindRec = findRecursive(csvList)          # Instantiating the class and passing the list imported from the CSV file

    print("The maximum number in the CSV list is: ", myFindRec.maxRec())
    print("The minimum number in the CSV list is: ", myFindRec.minRec())


if __name__ == '__main__':                      # Calling the main function
    main()
