import sys
from pathlib import Path

VALUE = {'X': 1, 'Y': 2, 'Z': 3}  # Rock Y, Paper X, Scissors Z
VICTORY, DRAW, LOSS = 6, 3, 0 # points
match_data = []  # whole match_data

def read_file(filename='input'):
    filedata = []
    try:
        with open(filename) as file:
            for line in file:
                filedata.append(line.rstrip())
    except FileNotFoundError:
        print("Wrong file or file path")
    return filedata

def evalue_play_part_1(play):
    if play == 'A X':           # rock vs rock
        return DRAW + VALUE['X']
    elif play == 'A Y':         # rock vs paper
        return VICTORY + VALUE['Y']
    elif play == 'A Z':         # rock vs scissors
        return LOSS + VALUE['Z']
    elif play == 'B X':         # paper vs rock
        return LOSS + VALUE['X']
    elif play == 'B Y':         # paper vs paper
        return DRAW + VALUE['Y']
    elif play == 'B Z':         # paper vs scissors
        return VICTORY + VALUE['Z']
    elif play == 'C X':         # scissors vs rock
        return VICTORY + VALUE['X']
    elif play == 'C Y':         # scissors vs paper
        return LOSS + VALUE['Y']
    elif play == 'C Z':         # scissors vs scissors
        return DRAW + VALUE['Z']
    else:
        return 0

def evalue_play_part_2(play):
    if play == 'A X':           # loss to rock - scissors
        return LOSS + VALUE['Z']
    elif play == 'A Y':         # draw to rock - rock
        return DRAW + VALUE['X']
    elif play == 'A Z':         # win to rock - paper
        return VICTORY + VALUE['Y']
    elif play == 'B X':         # loss to paper - rock
        return LOSS + VALUE['X']
    elif play == 'B Y':         # draw to paper - paper
        return DRAW + VALUE['Y']
    elif play == 'B Z':         # win to paper - scissors
        return VICTORY + VALUE['Z']
    elif play == 'C X':         # loss to scissors - paper
        return LOSS + VALUE['Y']
    elif play == 'C Y':         # draw to scissors - scissors
        return DRAW + VALUE['Z']
    elif play == 'C Z':         # win to scisscors - rock
        return VICTORY + VALUE['X']
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        match_data = read_file(sys.argv[1])     # python3 2.py input     
    else:
        match_data = read_file('2/input.txt')   # opened folder AdventOfCode

    if match_data:
        score_part1, score_part2, games_played = 0, 0, 0
        for game in match_data:
            games_played = games_played + 1
            score_part1 = score_part1 + evalue_play_part_1(game)
            score_part2 = score_part2 + evalue_play_part_2(game)
        print(f'rounds:{games_played}, score 1:{score_part1} score 2:{score_part2}')
    else:
        print('You sucks!')
