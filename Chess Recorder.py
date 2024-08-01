"""This is a simple program I wrote as a university fresher to take chess moves as input and output them to a text file in order to convert them to a pgn 
later on. This program is by no mean polished and is far from perfect, but I hope it can be of some use to anyone going through it. Feel free to use
this code as you please in your own work granted that I get acknowledgement. Enjoy!"""

def recorder_without_score_input():
    print("Enter '.' to end the game")

    #Loop to to continuously take moves and terminate once the end of the game is reached
    count = 1
    while True:    
        if (count-1)%10==0:
            fout.write('\n')
        else:
            fout.write('  ')
        move_W = input(f'Enter move {count} for white: ')
        if move_W=='.':
            fout.write('\n')
            break
        move_B = input(f'Enter move {count} for black: ')
        if move_B=='.':
            output_line = f'{count}. {move_W}\n'
            fout.write(output_line)
            break
        output_line = f'{count}. {move_W} {move_B}'
        fout.write(output_line)
        count+=1

def recorder_with_score_input():
    recorder_without_score_input()
    #Not a required part of the program as it just takes the winner, the score and the means of win (or draw).
    acceptable_scores = ['1-0','0-1','0.5-0.5']
    ending_methods = ['by Checkmate', 'by Resignation', 'Stalemate', 'Insufficient material', 'on Time']
    while True:
        winner = input('Enter the colour of the winning side or enter the word "draw": ')
        if winner == 'draw':
            score = '0.5-0.5'
        elif winner.lower() == 'white':
            score = '1-0'
        else:
            score = '0-1' 
        end = input(f'Enter match ending process (choose from {ending_methods}): ')
        if end  in ending_methods :
            break
        else:
            print('Invalid score or ending method.')
    if winner=='draw':
        end_text = f'The match is drawn due to {end}'
    else:
        end_text = f'{winner} wins {end}'
    end_text+=f'\nThe score is {score}'
    fout.write(end_text)

#driver code
player1 = input('Name of Player One: ')
player2 = input('Name of Player Two: ')
current_date = input('Enter unique indentifier for game (such as date and time): ')
name = player1+' vs '+player2+' '+current_date+'.txt'
fout = open(name,'w')
heading = f'[White "{player1}"]\n[Black "{player2}"]\n'
fout.write(heading)

choice = input('Input "a" for recorder with score input and "b" for recorder without score input: ')
while True:
    if choice.lower()=='a':
        recorder_with_score_input()
        break
    elif choice.lower()=='b':
        recorder_without_score_input()
        break
    else:
        print("Invalid input")

fout.close()
