# encoding=utf-8

age_all_members = [38, 43, 14, 70, 68, 74, 66, 1]
height_all_members = [170, 178, 130, 164, 174, 180, 169, 15]

def sum_of(all_data):
    result_data = 0
    for data in all_data:
        result_data = result_data + data
    return result_data

def avg_of(all_data):
    return sum_of(all_data) / len(all_data)

print("Total age of my family is ", sum_of(age_all_members))
print("Avg age of my family is", avg_of(age_all_members))

print("Total height of my family is ", sum_of(height_all_members))
print("Avg height of my family is", avg_of(height_all_members))