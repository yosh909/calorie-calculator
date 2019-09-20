import sys
dot_line = "\t\t\t------"
answer_space = "\n\t\t\t"
print("Hello, This is a calorie calculator?")
num = 1
while num == 1:
    Ready = input("\t Are you ready to being?\n\t\t\t")
    if Ready == 'yes':
        print("\t Very well, let's begin.")
        num = 2
    elif Ready == "no":
        print("\t Vey well, have a great day.")
        num = 3
    else:
        print("\t Im sorry i didn't get that.")
if num == 3:
    sys.exit()
else:
    print(dot_line)
    print("Im first going to need some information\nbefore you can get your results back.")
print(dot_line)
Gender = input("What is your sex?: [Male or Female]" + answer_space)
print(dot_line)
if Gender == "male":
    Height = input("What is your height?: (in inches)[12in = 1ft]" + answer_space)
    height_int = (int(12.9) * int(Height))
    print(dot_line)
    Weight = input("What is your weight?: (in Pounds)[1lb  = 2.2kg]" + answer_space)
    weight_int = (int(6.3) * int(Weight))
    print(dot_line)
    Age = int(input(("What is your age?" + answer_space)))
    age_int = (int(6.8) * int(Age))
    Equation_male = (66 + weight_int + height_int - age_int)
    print("This is what your caloric intake should be for maintaining weight: " + str(Equation_male))



