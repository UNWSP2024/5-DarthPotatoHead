#Program Written By: Ainsley Bellamy
#Date Written: 02/17/2025
#Program Title: Kilometer_Converter


# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

#Function to convert kilometers to miles.
def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214
#Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
#Get User Input
    inputted_kilometers = float(input("Enter distance in kilometers: "))
#Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    converted_input = kilometer_conversion(inputted_kilometers)
#Display the miles
    print(f"{inputted_kilometers:.4f} kilometers is equal to {converted_input:.4f} miles.")