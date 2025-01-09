#BMI Calculator

#1. I welcome the user with a print message and ask him to input his gender, weight and height which i capture as float
print("Welcome to my BMI calculator")
gender= (input("\nAre you Male or Female?\n",))
weight= float(input("\nInput your current weight in kg:\n",))
height= float(input("\nInput your current height in m:\n",))

#2. I calculate the optimal weight range using the height of the person and output the otpimal range weight 
def optimal_BMI(height):
    
    target_weight_low=18.5 * height**2
    target_weight_high=24.9 * height**2
    print (f'A healthy weight for you is between {round(target_weight_low, 2)} kg and {round(target_weight_high,2)} kg')



#3. I calculate his BMI with his height and weight and print the message according to his BMI taking th gender into account for different tips
def calculate_my_BMI(height, weight, gender):
    BMI = weight/height**2
    if BMI<=18.5 and gender=="Male":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Underweight')
        optimal_BMI(height)
        print(calorie_tips["Men"])
        
    elif BMI > 18.5 and BMI <25 and gender=="Male":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Normal Weight\nKeep this weight Buddy!')
        optimal_BMI(height)
        print(calorie_tips["Men"])
    elif BMI >=25 and gender == "Male":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Overweight\nStop eating this much Buddy!')
        optimal_BMI(height)
        print(calorie_tips["Men"])


    elif BMI<=18.5 and gender=="Female":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Underweight\nYou need to eat more Lady!')
        optimal_BMI(height)
        print(calorie_tips["Women"])
    elif BMI > 18.5 and BMI <25 and gender=="Female":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Normal Weight\nKeep this weight Lady!')
        optimal_BMI(height)
        print(calorie_tips["Women"])
    elif BMI >=25 and gender == "Female":
        print(f'\nYou are {gender} who is {height} m tall and weighing {weight} kg')
        print(f'You have a BMI of {round(BMI,2)} which is Overweight\nStop eating this much Lady')
        optimal_BMI(height)
        print(calorie_tips["Women"])
    
    

#4. I created a function to give different tips based on the users gender from which I call the value from within the function
calorie_tips = {
    "Men":"As a Man you should focus on strength training to build muscles",
    "Women":"As a woman, you may have more body fat compared to men at the same BMI, so be sure to check other health markers.",
}

#5. I call the function
calculate_my_BMI(height, weight, gender)
