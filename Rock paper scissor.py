import random

comp = random.randint(1,3)
choice = int(input('1 for Rock✊\n2 for Paper✋ \n3 for Scissor ✌️ \nChoose: '))

if comp == 1 and choice == 1:
    print('You chose Rock✊\nCPU chose Rock✊\nIt\'s a tie!')

elif comp == 2 and choice == 2:
    print('You chose Paper✋\nCPU chose Paper✋\nIt\'s a tie!')

elif comp == 3 and choice == 3:
    print('You chose Scissor ✌️\nCPU chose Scissor ✌️\nIt\'s a tie!')

elif comp == 1 and choice == 2:
    print('You chose Paper✋\nCPU chose Rock✊\nYou win!') 

elif comp == 1 and choice == 3:
    print('You chose Rock✊\nCPU chose Scissor ✌️\nYou win!')

elif comp == 2 and choice == 1:
    print('You chose Rock✊\nCPU chose Paper✋\nCPU wins!')

elif comp == 2 and choice == 3:
    print('You chose Paper✋\nCPU chose Scissor ✌️\nCPU wins!')

elif comp == 3 and choice == 1:
    print('You chose Rock✊\nCPU chose Scissor ✌️\nYou win!')

elif comp == 3 and choice == 2:
    print('You chose Scissor ✌️\nCPU chose Paper✋\nCPU wins!')

else:
    print('Invalid Input!')
