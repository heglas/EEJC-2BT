import re

padrao = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
texto = 'Entre em contato pelo e-mail: usuario@example.com'
emails = re.findall(padrao, texto, re.IGNORECASE)
print(emails)
