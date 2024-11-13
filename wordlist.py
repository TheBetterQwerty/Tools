#!/usr/bin/env python3

import random
import argparse


words , numbers , info = [] , [] , {}
sp_chars = ["$", "@", "#", "%" "!", "&", "$$", "@@", "##", "!!", "%%", "&&" , "_"]

def leet_pass():
    leet_replacements = {
        'A': ['4', '@'],
        'E': '3',
        'L': '1',
        'O': '0',
        'S': ['5', '$'],
        'T': '7'
    }

    passwords1 = set()

    for word in words:
        for number in numbers:
            leet_word = ''
            for char in word.upper():
                if char in leet_replacements:
                    replacement = leet_replacements[char]
                    if isinstance(replacement, list):
                        replacement = random.choice(replacement)  # Choose a random replacement option
                    leet_word += replacement
                else:
                    leet_word += char

            passwords1.add(leet_word + number)
            passwords1.add(number + leet_word)

    return list(passwords1)[1000]


def passwords(use_leet=True):
    passwords = set()

    passwords.add(f"{info['name']}{info['surname']}")
    for sp in sp_chars:
        passwords.add(f"{info['name']}{sp}{info['surname']}")
        passwords.add(f"{info['name']}{info['surname']}{sp}{info['year']}")
        passwords.add(f"{info['surname']}{sp}{info['name']}")
        passwords.add(f"{info['name']}{sp}{info['year']}")
        passwords.add(f"{info['name']}{sp}{info['year'][::-1]}")
        passwords.add(f"{info['name'].capitalize()}{sp}{info['surname']}")
        passwords.add(f"{info['name'].capitalize()}{info['surname']}{sp}{info['year']}")
        passwords.add(f"{info['surname'].capitalize()}{sp}{info['name']}")
        passwords.add(f"{info['name'].capitalize()}{sp}{info['year']}")
        passwords.add(f"{info['name'].capitalize()}{sp}{info['year'][::-1]}")

        nickname = info.get("nickname" , "")
        if nickname:
            passwords.add(f"{nickname.capitalize()}{sp}{info['year']}")
            passwords.add(f"{nickname}{sp}{info['year'][::-1]}")
            passwords.add(f"{nickname}{sp}{info['year']}")

        if int(info['year']) < 2010 :
            passwords.add(f"{info['name']}{info['surname']}{sp}{info['year'][-1]}")
            passwords.add(f"{info['name']}{info['surname']}{sp}{info['date']}{info['month']}{info['year'][-1]}")
            passwords.add(f"{info['name']}{sp}{info['date']}{info['month']}{info['year'][-1]}")
            passwords.add(f"{info['name'].capitalize()}{info['surname']}{sp}{info['year'][-1]}")
            passwords.add(f"{info['name'].capitalize()}{info['surname']}{sp}{info['date']}{info['month']}{info['year'][-1]}")
            passwords.add(f"{info['name'].capitalize()}{sp}{info['date']}{info['month']}{info['year'][-1]}")
            
        if int(info['month']) < 10 :
            passwords.add(f"{info['name']}{sp}{info['date']}0{info['month']}")
            passwords.add(f"{info['name'].capitalize()}{sp}{info['date']}0{info['month']}")
        else:
            passwords.add(f"{info['name'].capitalize()}{sp}{info['date']}{info['month']}")
            passwords.add(f"{info['name']}{sp}{info['date']}{info['month']}")

    passwords.add(f"{(info['ph_no'])}")
    passwords.add(f"{(info['ph_no'])[:6]}")
    passwords.add(f"{(info['ph_no'])[6:]}")
    passwords.add(f"{info['date']}{info['date']}")
    passwords.add(f"{info['date']}{info['month']}")
    passwords.add(f"{info['date']}{info['year']}")
    passwords.add(f"{info['month']}{info['date']}")
    passwords.add(f"{info['month']}{info['month']}")
    passwords.add(f"{info['month']}{info['year']}")
    passwords.add(f"{info['year']}{info['date']}")
    passwords.add(f"{info['year']}{info['month']}")
    passwords.add(f"{info['year']}{info['year']}")

    generated_pass = len(passwords)

    for word in words:
        for number in numbers:
            passwords.add(word + number)
            passwords.add(number + word)
            passwords.add(number + number)
            passwords.add(word.capitalize() + number)
            passwords.add(number + word.capitalize())
            passwords.add(word.upper() + number)
            passwords.add(number + word.upper())
            passwords.add(word[0].upper() + word[1:] + number)
            passwords.add(number + word[0].upper() + word[1:])
            passwords.add(word[0].lower() + word[1:] + number)
            passwords.add(number + word[0].lower() + word[1:])
            passwords.add(word + '_' + number)
            passwords.add(number + '_' + word)
            passwords.add(word.capitalize() + '_' + number)
            passwords.add(number + '_' + word.capitalize())
            passwords.add(word.upper() + '_' + number)
            passwords.add(number + '_' + word.upper())
            passwords.add(word[0].upper() + word[1:] + '_' + number)
            passwords.add(number + '_' + word[0].upper() + word[1:])
            passwords.add(word[0].lower() + word[1:] + '_' + number)
            passwords.add(number + '_' + word[0].lower() + word[1:])
            passwords.add(word + '-' + number)
            passwords.add(number + '-' + word)
            passwords.add(word.capitalize() + '-' + number)
            passwords.add(number + '-' + word.capitalize())
            passwords.add(word.upper() + '-' + number)
            passwords.add(number + '-' + word.upper())
            passwords.add(word[0].upper() + word[1:] + '-' + number)
            passwords.add(number + '-' + word[0].upper() + word[1:])
            passwords.add(word[0].lower() + word[1:] + '-' + number)
            passwords.add(number + '-' + word[0].lower() + word[1:])
            passwords.add(word + '.' + number)
            passwords.add(number + '.' + word)
            passwords.add(word.capitalize() + '.' + number)
            passwords.add(number + '.' + word.capitalize())
            passwords.add(word.upper() + '.' + number)
            passwords.add(number + '.' + word.upper())
            passwords.add(word[0].upper() + word[1:] + '.' + number)
            passwords.add(number + '.' + word[0].upper() + word[1:])
            passwords.add(word[0].lower() + word[1:] + '.' + number)
            passwords.add(number + '.' + word[0].lower() + word[1:])
            passwords.add(word + '1234')
            passwords.add('1234' + word)
            passwords.add(word + '123')
            passwords.add('123' + word)
            passwords.add(word.capitalize() + '123')
            passwords.add('123' + word.capitalize())
            passwords.add(word.capitalize() + '1234')
            passwords.add('1234' + word.capitalize())
            for ch in sp_chars:
                passwords.add(word + ch)
                passwords.add(ch + word + number)
                passwords.add(word + number + ch)
                passwords.add(number + word + ch)
                passwords.add(word + ch + number)
                passwords.add(words[0]+words[1]+ch+number)
            passwords.add(word[::-1] + number)
            passwords.add(number + word[::-1])
            passwords.add(word.title() + number)
            passwords.add(number + word.title())

            if (use_leet):
                passwords.update(leet_pass())

            generated_pass += 1

        if generated_pass >= 100000:
            print("Number of passwords crossed 100000 so breaking ... ")
            break

    generated_passwords = list(passwords)

    return generated_passwords[:100000] # list


def get_info():
    global info
    global words
    global numbers

    name , surname = input("Enter victim name (separated by space) >> ").split()
    date , month , year = input("Enter DOB (separated by '-' ) >> ").split("-")
    phone_no = input("Enter victim phonenumber >> ")
    nickname = input("Enter victim nickname (optional) >> ")
    info["name"] = name
    info["surname"] = surname
    info["date"] = date
    info["month"] = month
    info["year"] = year
    info["ph_no"] = phone_no
    if nickname :
        info["nickname"] = nickname
    
    print("[*] Enter other keywords separated by space ")
    lines = input("-> ").split()

    words = [line for line in lines if not line.isdigit()]
    numbers = [line for line in lines if line.isdigit()]
    lines.clear()

def main(leet):
    get_info()
    file_name = f"{info['name']}{info['surname']}.txt"
    gen_passwords = passwords(use_leet=leet)
    with open(file_name , "w") as file:
        for password in gen_passwords:
            file.write(f"{password}\n")
    print(f"[+] Generated {len(gen_passwords)} Passwords And Stored at {file_name} ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script To Create A Worlist")
    parser.add_argument("-l" , "--l33t" , type=bool, required=False , default=True , help="Leet your passwords (default=True)")
    args = parser.parse_args()

    main(leet=args.l33t)
