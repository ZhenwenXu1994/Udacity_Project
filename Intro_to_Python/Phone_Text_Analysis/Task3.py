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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
# SECTION 1:
#STEP 1: create a list to store all codes
telecodes = []

#STEP 2: determine type of each number by using if conditional statement, and store the data to above list
for call in calls:
    num_from = call[0]
    num_to = call[1]
    # determine whether dialed number is called by people is in Bangalore
    if num_from[:5] == "(080)":
        # determine whether answer number's type is in fixed lines
        if num_to[:1] == "(":
            # get the index of end bracket of area code because the area codes vary in length, and then get the string of area code
            telecode = num_to[1:call[1].index(")")]
        # if answer's type is mobile phone, the area code will be first four digits
        else:
            telecode = num_to[:4]
        # store disappeared area codes into list of area codes
        if telecode not in telecodes:
            telecodes.append(telecode)

#STEP 3: print outputs one per line in lexicographic order with no duplicates
print("The numbers called by people in Bangalore have codes:")
for code in sorted(telecodes):
    print(code)

#SECTION 2:
#STEP 1: create a for loop with if conditional statement to count the number of local calls and outgoing calls
local_calls = 0
outgoing_calls = 0

for call in calls:
    num_from = call[0]
    num_to = call[1]
    # This condition is for local calls
    if num_from[:5] == "(080)" == num_to[:5]:
        local_calls += 1
    # This condition is for outgoing calls
    if num_from[:5] == "(080)":
        outgoing_calls += 1

#STEP 2: use values of local_calls and outgoing_calls to calculate percentage, and then print output
rate = local_calls/outgoing_calls
message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(message.format('%.2f%%' % (rate*100)))         
"""
   ********* This task was refered to https://github.com/ChrisMaslow/investigate-texts-and-calls/blob/master/Task3.py **********
"""        
