from typing import TextIO, Dict, List


def get_game_dict(game_data: TextIO) -> Dict[str, List[int]]:
    """Return a dictionary containing the team name and a list of points
    earned in each game for each team in the open file game_data.

    >>> input_file = open('sample_games.txt')
    >>> get_game_dict(input_file)
    {'Toronto Maple Leafs': [2, 2, 1, 0, 0, 2], 'Grande Prairie Storm': [], \
'Montreal Canadiens': [1, 2, 1, 0, 2]}
    >>> input_file.close()
    """

    team_to_points = {}
    
    line = game_data.readline().strip()
    while line != '': 
        team_name = line
        total_points = []
        team_to_points[team_name] = total_points
        line = game_data.readline().strip()
        
        while line.isdigit():
            total_points.append(int(line))
            line = game_data.readline().strip()
            
            team_to_points[team_name] = total_points
     
    return team_to_points 


input_file = open('/Users/kanishsharma/Downloads/csc148/miscellaneous/Test Code/NHL-data.txt')
get_game_dict(input_file)