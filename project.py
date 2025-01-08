#BMI Calculator

#1. I welcome the user with a print message and ask him to input his gender, weight and height which i capture as float
print("Welcome to my BMI calculator")
gender= (input("Are you Male or Female?",))
weight= float(input("Input your current weight in kg:",))
height= float(input("Input your current height in cm:",))

#2. I output gender, height and weight for the time being to check
print(f'You are {gender} who is {height} cm tall and weighing {weight} kg')

#3. I calculate his BMI with his height and weight and print the message according to his BMI taking th gender into account for different tips
def calculate_my_BMI(height, weight, gender):
    BMI = weight/height**2
    
    if BMI<18.5 and gender=="Male":
        print(f'You have a BMI of {round(BMI,2)} which is Underweight\nYou need to eat more Buddy!')
        print(calorie_tips["Men"])
    elif BMI >= 18.5 and BMI <=25 and gender=="Male":
        print(f'You have a BMI of {round(BMI,2)} which is Normal Weight\nKeep this weight Buddy!')
        print(calorie_tips["Men"])
    elif BMI >25 and gender == "Male":
        print(f'You have a BMI of {round(BMI,2)} which is Overweight\nStop eating this much Buddy!')
        print(calorie_tips["Men"])


    elif BMI<18.5 and gender=="Female":
        print(f'You have a BMI of {round(BMI,2)} which is Underweight\nYou need to eat more Lady!')
        print(calorie_tips["Women"])
    elif BMI >= 18.5 and BMI <=25 and gender=="Female":
        print(f'You have a BMI of {round(BMI,2)} which is Normal Weight\nKeep this weight Lady!')
        print(calorie_tips["Women"])
    elif BMI >25 and gender == "Female":
        print(f'You have a BMI of {round(BMI,2)} which is Overweight\nStop eating this much, Lady')
        print(calorie_tips["Women"])
    
    return BMI

# def optimal_BMI(BMI, height, weight):
#     weight=BMI*height**2
    



#4. I created a function to give different tips based on the users gender from which I call the value from within the function
calorie_tips = {
    "Men":"As a Man you should focus on strength training to build muscles",
    "Women":"As a woman, you may have more body fat compared to men at the same BMI, so be sure to check other health markers.",
}

#5. I call the function
calculate_my_BMI(height, weight, gender)


