last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

#adding new subjects and grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

print(gradebook)

#change on the visual arts grade
gradebook[-1][1] = 98

print(gradebook)

#remove the grade score of "poetry"
gradebook[2].remove(85)

print(gradebook)

#Add "Pass" to "poetry"
gradebook[2].append("Pass")

print(gradebook)

#Add last semester and gradebook together
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)