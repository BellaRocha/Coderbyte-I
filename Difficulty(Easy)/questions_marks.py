#Questions Marks

#Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

#For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

#Examples:
#Input: "aa6?9" 
#Output: false
#Input: "acc?7??sss?3rr1??????5" 
#Output: true

#Tags:
#Hash Table
#Searching 
#String Manipulation

#Python:
import re 
def QuestionsMarks(strParam):
  strEdit = re.sub('[abcdefghijklmnopqrstuvwxyz]', '', strParam) 
  first_num = 0
  second_num = 0
  i = 0
  pair_found = 0 
  while i < len(strEdit) - 1:
    q_value = 0
    if strEdit[i].isdigit() and strEdit[i + 1] == '?':
      first_num = float(strEdit[i])
      i += 1
      while strEdit[i] == '?':
        q_value += 1
        if (i == len(strEdit) - 1):
          return "false"
        i += 1
      if q_value == 3:
        second_num = float(strEdit[i])
        if first_num + second_num == 10.0:
          pair_found += 1
      elif q_value < 3 or q_value > 3:
        second_num = float(strEdit[i])
        if first_num + second_num == 10.0:
          return "false"
    else:
      i += 1
  if pair_found > 0:
    return "true"
  return "false"

# keep this function call here 
print QuestionsMarks(raw_input())
