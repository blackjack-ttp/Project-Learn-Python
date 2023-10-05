# Xây dựng chương trình giúp người và máy tính nói chuyện với nhau về: 
# Máy tính lần lượt hỏi thông tin của về tên, tuổi, giới tính, số điện thoại, email, địa chỉ, nghề nghiệp, sở thích, sở trường, 
# người dùng sẽ nhập vào thông tin của mình. Sau đó hiển thị kết quả của cuộc nói chuyện là thông tin của người dùng.

name=str(input("What is your name? =>"))
age=int(input("How old are you? =>"))
gender=str(input("Please tell me your gender =>"))
phone=int(input("What is your phone number? =>"))
email=str(input("What is your email? =>"))
address=str(input("What is your address? =>"))
job=str(input("What is your job? =>"))
hobby=str(input("What is your hobby? =>"))
forte=str(input("What is your forte? =>"))
print("Your information!!")
print("Name: ", name)
print("Age: ", age)
print("Gender: ", gender)
print("Phone: ", phone)
print("Email: ", email)
print("Address: ", address)
print("Job: ", job)
print("Hobby: ", hobby)
print("Forte: ", forte)
print("Thank you for providing us with this information")
