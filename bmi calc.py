def bmi_calc():
    while True: 
        
        print("IMPORTAT! \nAlways use a period to separate the decimal! Thanks:)")
        
        name = input('Write you name (to stop, write "Stop"): ')
        
        if name == "Stop":
            print("Stopping")
            break
        
        if name != "Stop":
            height = float(input("What is your height in meters? "))
            weight = float(input("What is your weight in kg? "))
            bmi = weight / (height**2)
            print(name+"'s", "Bmi is: ", bmi)
            if 18.5>bmi:
                print(bmi, "is underweight")
            elif 18.5<bmi<24.9:
                print(bmi, "is normal weight")
            elif 25<=bmi<30:
                print(bmi, "is overweight")
            elif bmi>=30:
                print(bmi, "is Obesity")
bmi_calc()
    