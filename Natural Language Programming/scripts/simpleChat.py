# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 11:02:58 2024

@author: NFSU
"""
#%% Mial
import re

def valid():
    
    mail_id = []
    rgx2 = input("Enter name of the school: ")
    
    with open(r"D:\Hemang\Sem2\NLP\Chatbot\Text.txt", "r") as text:
        
        for line_number, line in enumerate(text, start = 1):
            print(line)
            if re.search(rgx2, line, flags = re.IGNORECASE):
                rgx1 = "(A-Z|a-z|.|_|%+|-|0-9)+@(A-Z|mka-z|.|_|%+|-)+"
                mail = re.search(rgx1, line, flags = re.IGNORECASE)
                mail_id.append(mail.group())
                
    return mail_id


if __name__ == "__main__":
    
    print("Hello! my name is Alex. How can i help you.")
    
    mail_id = valid()
    
    if len(mail_id) == 1:
        print("Email ID for contacting school", mail_id[0])   
        
    elif len(mail_id) > 1:
        string = ""
        print("Multiple mail ID has been found, you can contact any one of them. \n", string.join(mail_id))
    
    else:
        print("School not found.")
        
        
#%% phone number

regx = r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"