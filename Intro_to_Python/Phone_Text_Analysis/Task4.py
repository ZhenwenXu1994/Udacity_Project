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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
#STEP 1: create a list which has all numbers that could never be telemarketers
target_list = []

#STEP 2: use for loop and if conditional statement to collect all target numbers 
for call in calls:
    if call[1] not in target_list:
       target_list.append(call[1])
for text in texts:
    if text[0] not in target_list:
       target_list.append(text[0])
    if text[1] not in target_list:
       target_list.append(text[1])

#STEP 3: create a list to store all possible numbers which could be telemarketers if this numbers are not in target_list
telemarketer_list = []
for call in calls:
    if call[0] not in target_list:
        if call[0] not in telemarketer_list:
            telemarketer_list.append(call[0])

#STEP 4: print outputs one per line in lexicographic order with no duplicates
print("These numbers could be telemarketers: ")
for number in sorted(telemarketer_list):
    print(number)
