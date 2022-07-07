def addStudentRecord(file):
 data = open("data.txt", 'a')  # open the file with all the students id


 f = file + ".txt"  # make it a string
 try:
  m = open(f, "x")  # create it and check if its there or not
 except OSError:
  print("id", file, "already exists please try again")
 else:
  print("student record has been made.")
  data.write("\n" + file)
  m.close()
 data.close()





