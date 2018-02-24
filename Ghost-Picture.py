
import sys

student_num_string = sys.argv[1]
student_num = int(sys.argv[1])

#Integer dividing student number by 100000 moves decimal at the end of the 9 digit student number 5 digits back, modulus dividing the result by 10 gives the last digit of the previous result (6th digit of 9 digit student number) 

sixth_digit = int((student_num / 100000) % 10)

print (sixth_digit) 

#rfind determines the index of the last instance of the number 0 in the student number

zero_index_string = student_num_string.rfind("0")

#The index of the last instance of the number zero is coverted to an integer

zero_index = int(zero_index_string)

print (zero_index)

#The sixth digit of the student number and the index of the last instance of zero from the student number are added together

sixth_digit_plus_zero_index = sixth_digit + zero_index

print (sixth_digit_plus_zero_index)

#The result from the last print statement has two added to it
sixth_digit_plus_zero_index_plus_two = sixth_digit_plus_zero_index + 2

print(sixth_digit_plus_zero_index_plus_two)

#The result from the last print statement is added with the integer that is directly below it in value

sixth_digit_plus_zero_index_plus_two = sixth_digit_plus_zero_index_plus_two + (sixth_digit_plus_zero_index_plus_two - 1)

print(sixth_digit_plus_zero_index_plus_two)

#The result of the last print statement has twenty subtracted from it

sixth_digit_plus_zero_index_plus_two = sixth_digit_plus_zero_index_plus_two - 20

print (sixth_digit_plus_zero_index_plus_two)

#The result of the last print statement is divided by two (converted to float)

sixth_digit_plus_zero_index_plus_two = float(sixth_digit_plus_zero_index_plus_two / 2)

print(sixth_digit_plus_zero_index_plus_two)

#The result of the last print statement has the value of the sixth digit of the student number and the index of the last instance of zero from the student number being added together subtracted from it

sixth_digit_plus_zero_index_plus_two = sixth_digit_plus_zero_index_plus_two - sixth_digit_plus_zero_index

print(sixth_digit_plus_zero_index_plus_two)

#The result of the last print statement has 105.5 added to it, which when converted to an integer will always have an exact value of 97

sixth_digit_plus_zero_index_plus_two = int(sixth_digit_plus_zero_index_plus_two + 105.5)

#The result of the last print statement is converted to an uppercase char character and will always be "A"

sixth_digit_plus_zero_index_plus_two = chr(sixth_digit_plus_zero_index_plus_two).upper()

print(sixth_digit_plus_zero_index_plus_two)
