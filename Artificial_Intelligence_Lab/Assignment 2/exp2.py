print("Enter Any Two Subject You Like From The Following - ")
print("Maths, Programming, Biology, Physics, AI Concepts, Chemistry, Statistics")
sub1 = input("1st subject - ").lower()
sub2 = input("2nd Subject - ").lower()

if sub1 == "maths" and sub2 == "physics" or sub2 == "maths" and sub1 == "physics":
	print("Mechanical Engineering")
elif sub1 == "chemistry" and sub2 == "biology" or sub2 == "chemistry" and sub1 == "biology":
	print("Biotechnology")
elif sub1 == "maths" and sub2 == "programming" or sub2 == "maths" and sub1 == "programming":
	print("Computer Engineering")
elif sub1 == "ai concepts" and sub2 == "programming" or sub2 == "ai concepts" and sub1 == "programming":
	print("Artificial Intelligence and Machine Learning Engineering")
elif sub1 == "statistics" and sub2 == "programming" or sub2 == "statistics" and sub1 == "programming":
	print("Artificial Intelligence and Data Science")
else:
	print("Oops!!...Somthing Went Wrong :( ")
