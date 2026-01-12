def check_login(user_input, correct_username):
    cleaned_input = user_input.strip()
    
    if cleaned_input.lower() == correct_username.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    db_user = "admin"
    
    test_input_1 = "  admin  "  #true bo usuwa biale znaki (usuwa spacje)
    test_input_2 = "admin\n"    #true bo usuwa biale znaki (nową linie(\n))
    test_input_3 = "  user123" #false bo mimo usuniecia bialych znakow jest zle

    print("Test 1 (spacje):", check_login(test_input_1, db_user))
    print("Test 2 (znak nowej linii):", check_login(test_input_2, db_user))
    print("Test 3 (zły użytkownik):", check_login(test_input_3, db_user))

    # .lstrip   ---->     usuwa znaki tylko z lewej strony (left)
    # .rstrip   ---->     usuwa znaki tylko z prawej strony (right)
    # .strip    ---->     usuwa znaki z obu stron jednoczesnie

    