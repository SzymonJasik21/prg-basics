required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# Sprawdzenie, czy wymagane uprawnienia są podzbiorem uprawnień użytkownika
# (Czy użytkownik posiada WSZYSTKIE wymagane elementy?)
has_permissions = required_permissions <= user_permissions

print(has_permissions)