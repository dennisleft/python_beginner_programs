'''
Create a program whwere the user inputs
1. email address
2. password
3. name

and the program finds the email prefix, domain and password
eg. for abc@def.com, pass:idcoisn
print
    abc    def  idcoisn
'''
def user_input():
    print('Hi there! What is your name?\n')
    name=input()
    print('\n{}, enter your email address:\n'.format(name))
    email=input()
    print('\nEnter your password:\n')
    password=input()

    #prefix
    prefix_index=email.index('@')
    prefix=email[:prefix_index]
    

    #domain
    email_without_prefix=email[prefix_index+1:]
    domain_index=email_without_prefix.index('.')
    domain=email_without_prefix[:domain_index]
    

    #password
    pass_length=str(len(password))

    #
    print('\n {}\t{}\tPassword has {} characters'.format(prefix, domain,pass_length))

user_input()
