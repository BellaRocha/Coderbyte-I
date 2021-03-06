#Letter Count I

#Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces.

#Examples:
#Input: "Hello apple pie" 
#Output: Hello
#Input: "No words" 
#Output: -1

#Tags:
#Hash Table
#Searching
#String Manipulation

#Python:
def LetterCountI(strParam):
  list_str = strParam.split(' ')
  count = []
  total_count = []
  for i in range (len(list_str)):
    for j in range (len(list_str[i])):
      count.append(list_str[i].count(list_str[i][j]))
    total_count.append(max(count))
    count = []
  
  largest = max(total_count)

  if largest == 1:
    return -1

  for k in range (len(total_count)):
    if total_count[k] == largest:
      return list_str[k]

# keep this function call here 
print LetterCountI(raw_input())
