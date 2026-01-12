def generator_hasel():
    yield "admin123"
    yield "user_password"
    yield "secret_key"

for haslo in generator_hasel():
    print(f"Sprawdzam hasło: {haslo}")