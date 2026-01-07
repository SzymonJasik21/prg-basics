initials = lambda name, surname: name[0].upper() + surname[0].upper()

print(initials("John", "Brown"))
print(initials("anna", "may"))

u_name = input("Enter name: ")
u_surname = input("Enter surname: ")
print(f"Initials: {initials(u_name, u_surname)}")