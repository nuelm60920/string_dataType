def student_info(**name):
    if not name or len(name) < 2:
        print("Student must have a name longer 2 letters!")
        

    else:

        print(f"student's name: {name}" )
        #no_subject  = 5
        #count = 0 

        student_subject_details = {}
        total_score = 0

        #while count < no_subject:
        while True:
            subject = input('enter subject name:').strip().capitalize()

            if subject.lower() == "quit" or subject.lower() == "q":
                print("you have come to the end!")
                break

            mark = int(input("enter the subject's mark:").strip())

            #store student's subject and mark

            student_subject_details[subject] = mark
            #total score
            
            #count += 1
        
        for subj in student_subject_details.items():
            print(subj)

        total_score = sum(student_subject_details.values())
        print(f"Total score of {name} is: {total_score}")


       
           

        

x= input('enter student name:').capitalize()
y = input('enter student id')
student_info(name=x,y=y, email="nuel@yahoo.com")


name ={1:10, 2:20, 3:30, 4:40}

name['Name'] ="Nuel"

print(name)

for x,y in name.items():
    print(x,y)


