#Password Checker
#step 1: prompt user to enter their password
'''Check the following:
   2 - if the password contains the letter z(index of last char)
   1 - if the password ends with an !
   3 - if the password begins with any uppercase letter
   4 - if the password contains any special character
'''
RuleOne = False
RuleTwo = False
RuleThree = False
RuleFour = False
Special_Char = ['@', '#', '$', '%', 
                '^', '&', '*', '~', 
                '?', '}', '{', '_']
print('''Enter a password which...
      - Contains the letter z
      - Ends with an !
      - Begins with any uppercase letter
      - contains any special char''')
PW = input('Password: ')
#step 2: If yes to all 3 checks, Accept! // Any are no, Reject!
if PW[-1] == '!':
    RuleOne = True
    if 'z' in PW:
        RuleTwo = True
        if PW[0].isupper:
            RuleThree = True
            if PW:
                RuleFour = True
                print('Accept!')
else:
    print('Reject!')

#step 3: Implement more generic rules on the whiteboard
# Rule 4 and Rule 5