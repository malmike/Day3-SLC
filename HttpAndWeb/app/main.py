from client import ConsumingPublicApi

def main():
    client = ConsumingPublicApi()
    git_hub_user_name = input('Enter your git hub user name: ')
    dict_value = client.get_api_data('%s'%git_hub_user_name)
    for i in dict_value:
        print (str(i) +'\t-\t'+ str(dict_value[i]))

if __name__ == "__main__":
    main()