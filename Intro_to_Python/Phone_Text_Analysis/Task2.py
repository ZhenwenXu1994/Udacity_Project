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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
#STEP 1: create a dictionary as a target place to store all numbers as keys and total time of each nuumber as values  
total_time_of_different_num = {}

#STEP 2: use for loop and if conditional statement to store data from provided .csv file
for call in calls:
    if call[0] not in total_time_of_different_num:
        total_time_of_different_num[call[0]] = int(call[3])
    else:
        total_time_of_different_num[call[0]] += int(call[3])
    if call[1] not in total_time_of_different_num:
        total_time_of_different_num[call[1]] = int(call[3])
    else:
        total_time_of_different_num[call[1]] += int(call[3])

#STEP 3: determine the longest time by using for loop and if conditional statement
longestPhone,longestTime = max(total_time_of_different_num.items(),key=lambda x:x[1])

#STEP 4: create a message to print output of number and total longest time
message = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(message.format(longestPhone, longestTime))

        
