"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

#STEP 1: first of all, create a list to store all different numbers
target_list = []

#STEP 2: determine whether the input number is appeared in the target list using for loop to create a judgement action of all numbers on the texts list and calls list
for text in texts:
    if text[0] not in target_list:
       target_list.append(text[0]) 
    if text[1] not in target_list:
       target_list.append(text[1])
for call in calls:
    if call[0] not in target_list:
       target_list.append(call[0]) 
    if call[1] not in target_list:
       target_list.append(call[1])
    
#STEP 3: create a form of message to output by counting the length of target list
message = "There are {} different telephone numbers in the records."
print(message.format(len(target_list)))