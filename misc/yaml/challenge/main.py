import warnings
from yaml import *
import sys 

def check_data(user_input):

    data = load(user_input)

    if not isinstance(data, dict):

        raise Exception("Data must be a dictionnary")
        exit(0)

    
    if (len(data.keys()) > 3):

        print("Only 3 keys needed")
        exit(0)

    if (not 'team_7even' in data.keys() or not 'categories' in data.keys() or not 'visible' in data.keys()):

        print("Wrong yaml file")
        exit(0)
    
    if (not 'authors' in data['team_7even'][0]):

        print("Please provide the authors of the challenge")
        exit(0)

    else:

        with open("authors.yaml", "w") as f:

            dump(data['team_7even'][0]['authors'], f)
            f.close()
        

def main():

    warnings.filterwarnings("ignore")
    print("Give me a yaml file as input: ")
    sys.stdout.flush()
    
    try:

        raw_data = sys.stdin.read()
        check_data(raw_data)
        
    except Exception as e:
        
        print("Error: ", e)
        exit(1)


if __name__ == "__main__":

    main()