# encoding=utf-8

age_mommy = 38
age_daddy = 43
age_max = 14

height_mommy = 170
height_daddy = 178
height_max = 130

def sum_of(a, b, c):
    return (a+b+c)

def avg_of(a, b, c):
    return sum_of(a, b, c) / 3

print("Total age of my family is ", sum_of(age_mommy, age_daddy, age_max))
print("Avg age of my family is", avg_of(age_mommy, age_daddy, age_max))

print("Total height of my family is ", sum_of(height_mommy, height_daddy, height_max))
print("Avg height of my family is", avg_of(height_mommy, height_daddy, height_max))