def main():
    vowels = "aeiouy"
    letter = input("Enter a letter:")
    
    if letter.isalpha() and len(letter)== 1:
        if letter.lower() in vowels:    
            print(f"the letter is a vowel")
        else:
            print(f"the letter is NOT a vowel")
    else:
        print(f"Enter a singel lettergg")
if __name__ == '__main__':
    main()

  