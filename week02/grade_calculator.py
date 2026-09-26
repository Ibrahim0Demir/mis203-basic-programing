counter=0
total_score=0
while True:
  std_name=input("Enter student name (or q to quit): ")
  if std_name== "q" :
    break
  stds_score=int(input("Enter score: "))
  if stds_score<0 or stds_score>100 :
    print("Invalid score. Please enter a number between 0 and 100.")
    continue
  counter+=1
  total_score=total_score+stds_score
  if stds_score>=90 and stds_score<= 100:
    print(f"{std_name}: {stds_score} -> A ")
  elif stds_score>=80 and stds_score<90:
    print(f"{std_name}: {stds_score} -> B ")
  elif stds_score>=70 and stds_score<80:
    print(f"{std_name}: {stds_score} -> C ")
  elif stds_score>=60 and stds_score<70:
    print(f"{std_name}: {stds_score} -> D ")
  else:
    print(f"{std_name}: {stds_score} -> F ")
if counter== 0:
  print("No students entered.")
else:
  print(f"Total students: {counter}")
  print(f"Average score: {total_score/counter}")
