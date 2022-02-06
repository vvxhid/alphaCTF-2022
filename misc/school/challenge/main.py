import time, random 

def create_expression():

    operations = ["*", "+", "-", "/"]

    op1 = operations[random.randint(0, 3)]
    op2 = operations[random.randint(0, 3)]

    expression = str(

        str(random.randint(0, 1000)) + 
        " " + 
        op1 + 
        " " +
        str(random.randint(0, 1000)) + 
        " " + 
        op2 + 
        " " + 
        str(random.randint(0, 1000))
    )

    result = int(eval(expression))
    
    return expression, result 


def main():


    print("Welcome to math class!")
    print("There are 3 expressions to solve")
    print("You have only 5 seconds for each one so be quick ^^")

    for i in range(3):

        expression, result = create_expression()
        print(f"Here is your expression: {expression}")
        
        start = time.time()
        user_answer = input("Your answer: ")
        taken_time = time.time() - start 

        if (taken_time < 5 and user_answer == str(result)):

            print("Good job")
            print("To the next one!")

        elif taken_time > 5:

            print("Too slow !")
            exit(0)

        else:

            print("Wrong answer")
            exit(0)

    print("Congrats nerd!! Here is your flag: alphaCTF{y0u_mus1_b3_a_r3al_math_n3rd!!}")

    
if __name__ == "__main__":

    main()