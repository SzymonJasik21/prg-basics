import emails

file_name = 'email.txt'

# Wczytanie surowej treści maila
with open(file_name, 'r', encoding='utf-8') as file:
    raw_email = file.read()

# Wykorzystanie funkcji z modułu emails
sender = emails.email_sender(raw_email)
recipient = emails.email_recipient(raw_email)
subject = emails.email_subject(raw_email)
body = emails.email_body(raw_email)

# Wyświetlenie wyników
print(f"From:    {sender}")
print(f"To:      {recipient}")
print(f"Subject: {subject}")
print("-" * 30)
print(f"Body:\n{body}")