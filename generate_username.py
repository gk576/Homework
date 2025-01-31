# we start by generating the usernames
def generate_usernames(students):
    usernames = []
    username_count = {}

    # creating the base of the username 
    def generate_username(student):
        first_name, last_name = student.split(' ')
        username = first_name[0].lower() + last_name.lower()
        
        if username in username_count:
            username_count[username] += 1
            username = username + str(username_count[username])
        else:
            username_count[username] = 0
        
        return username
    
    for student in students:
        usernames.append(generate_username(student))
    
    return usernames

# testing the program 
students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas', 'Mike Smith', 'Alex Green']
result = generate_usernames(students)
print(result)