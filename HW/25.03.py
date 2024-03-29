# Task 1 - Распределение почт
import re

text_emails = []
text_number_emails = []
text_all_emails = []

text = '''fhgfhgnbgfncnbvncv
gdfjlgfdjsbklvcbjklcbjtrlskhyjskleretgrse
grlkgrsdlgdfgjksfl bob@gmail.com jfdkgfdskjgslfgdfsjkgdfsjl

gfdjlkgfsjgkldfgdfsjglskjtrehiru4ywtriugeshviu34h54kj3

bob1@gmail.com,kgfdslgkdfsjgdflkgfxjblkcxbjdxfklggaslgakdsg;lasdkgf,vbfgfdgldfskgdf;lsgfdslgfds,bob_1@gmail.com bob2-wilson@ukr.net'''

emails = re.findall(r'[a-zA-Z0-9-_]+@+[a-z]+.[a-z]+', text)

for email in emails:
    end = email.find('@')
    if email[:end].isalpha():
        text_emails.append(email)
    elif email[:end].isalnum():
        text_number_emails.append(email)
    else:
        text_all_emails.append(email)

print(text_emails)
print(text_number_emails)
print(text_all_emails)