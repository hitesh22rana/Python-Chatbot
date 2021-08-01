def bmi():
    print('              W-E-L-C-O-M-E'          )
    print(" ")
    print('Lets!! Calculate your Body Mass Index (BMI)')
    print(" ")

    height = float(input("Enter Your height in metre : "))
    weight = float(input("Enter Your Weight in Kg : "))
    BMI = round(weight/((height)*(height)),2)
    if(BMI>=30.0):
        print(f"Your BMI is {BMI} and you are obprint.")
    elif(BMI>=25.0 and BMI<30.0):
        print(f"Your BMI is {BMI} and you are overweight.")
    elif(BMI<25.0 and BMI>=18.5):
        print(f"Your BMI is {BMI} and you have ideal BMI. Congratulations!!")
    else:
        print(f"Your BMI is {BMI} and you are Underweight.")

if __name__ == "__main__":
    bmi()