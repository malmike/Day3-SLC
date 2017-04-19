from client import ConsumingPublicApi

def main():
    client = ConsumingPublicApi()
    git_hub_user_name = input('Enter your git hub user name: ')
    value = client.get_api_data('%s'%git_hub_user_name)
    print (value)

if __name__ == "__main__":
    main()