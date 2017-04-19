from client import ConsumingPublicApi

def main():
    #Initial an object of the ConsumingPublicApi class
    client = ConsumingPublicApi()
    #Get the user name of the git hub account of the user
    git_hub_user_name = input('Enter your git hub user name: ')
    #Pass the user name as an argument to the function get_api_data
    dict_value = client.get_api_data('%s'%git_hub_user_name)
    #Loop through the values returned while printing them
    for i in dict_value:
        print (str(i) +'\t-\t'+ str(dict_value[i]))

if __name__ == "__main__":
    main()