import re

def email_sender(email_content):
    # Szuka tekstu po "From: " do końca linii
    match = re.search(r"^From:\s*(.*)", email_content, re.MULTILINE)
    return match.group(1).strip() if match else None

def email_recipient(email_content):
    # Szuka tekstu po "To: " do końca linii
    match = re.search(r"^To:\s*(.*)", email_content, re.MULTILINE)
    return match.group(1).strip() if match else None

def email_subject(email_content):
    # Szuka tekstu po "Subject: " do końca linii
    match = re.search(r"^Subject:\s*(.*)", email_content, re.MULTILINE)
    return match.group(1).strip() if match else None

def email_body(email_content):
    # Szuka treści po pierwszej pustej linii (\n\n) do końca tekstu
    match = re.search(r"\n\n(.*)", email_content, re.DOTALL)
    return match.group(1).strip() if match else None