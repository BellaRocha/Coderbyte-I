#Longest Word

#Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

#Examples:
#Input: "fun&!! time" 
#Output: time
#Input: "I love dogs" 
#Output: love

#Tags: 
#Searching
#String Manipulation

#Python:
import re
def LongestWord(sen):
  list_sen= re.sub("[^a-zA-Z0-9]+", " ",sen).split(' ')
  max = 0
  max_i = 0
  for i in range (len(list_sen)):
    if len(list_sen[i]) > max:
      max = len(list_sen[i])
      max_i = i

  return list_sen[max_i]

# keep this function call here 
print LongestWord(raw_input())
