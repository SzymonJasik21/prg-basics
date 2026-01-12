class Haslo:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __str__(self):
        if len(self.password) >= 8:
            status = "OK"
        else:
            status = "ERR"
            
        return self.user + "_" + status

if __name__ == "__main__":
    print(Haslo("admin", "12345"))
    print(Haslo("moderator", "tajnehaslo123"))