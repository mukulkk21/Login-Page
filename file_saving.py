class Save:
    def __init__(self, Name, Mail, username, password, security):
        self.Name = str(Name)
        self.Mail = str(Mail)
        self.username = str(username)
        self.password = str(password)
        self.security = str(security)
        self.save()

    def save(self):
        with open("data.txt", 'a') as file:
            file.write(f"Name: {self.Name}, Mail: {self.Mail}, Username: {self.username}, Password: {self.password}, Security: {self.security}\n")
        print("File saved successfully")


class Verify:
    def __init__(self, username, password):
        self.username = str(username)
        self.password = str(password)

    def ver(self):
        with open("data.txt", 'r') as file:
            for line in file:
                if self.username in file and self.password in file:
                    return True
        return False

    #
    # def print_file_contents(self):
    #     with open("data.txt", 'r') as file:
    #         print(file.read())