#Find Intersection

#Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false. 

#Examples:
#Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] 
#Output: 1,4,13
#Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"] 
#Output: 1,9,10

#Tags:
#Array

#Python:
def FindIntersection(strArr):
  first_list = strArr[0].split(", ")
  second_list = strArr[1].split(", ")
  intersect = ""

  for i in range (0, len(first_list)):
    for j in range (0, len(second_list)):
      if first_list[i] == second_list[j]:
        intersect = intersect + first_list[i] + ","
        break
    
  if intersect == "":
    return "false"
  else:
    return intersect[0:-1]

# keep this function call here 
print FindIntersection(raw_input())
