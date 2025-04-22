def main():
    try:   
        age = int(input("How Old are you (in numbers):"))
    

        if age < 13 or age > 19:    
            print(f"You are NOT a teen")
        else:
            print(f"You are a teen")
    except ValueError:
     print("Error, you need to use number")
if __name__ == '__main__':
    main()