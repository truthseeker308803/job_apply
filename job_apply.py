name = input("What is your name?: ").capitalize().strip()
age = int(input("Please enter your age: "))
university = input("Are you a university graduate? (Yes or No:) ").lower().strip()
high_school = input("Are you a high school graduate? (Yes or No:) ").lower().strip()
Python = input("Do you know Python? (Yes or No:) ").lower().strip()
Java = input("Do you know Java? (Yes or No:) ").lower().strip()
C = input("Do you know C? (Yes or No:) ").lower().strip()
English = input("Do you know English? (Yes or No:) ").lower().strip()

a = "yes"
b = "no"

if (age <= 35) and (university == a or high_school == a) and (Python == a or Java == a or C == a) and (English == a):
  print(f"Congratulations {name} your application is received.")
else:
  print("Your application is not valid. Sorry!")

applicants = {name:
                {"personal_info": {"age": age, "university": university, "high-school": high_school},
                "technical_info": {"Python knows": Python, "Java knows": Java, "C knows": C, "English knows": English}}
}
print(applicants)