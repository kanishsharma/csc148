"""Week 8 Perform - Part 2"""

# file name: w08_markus.py
#
# Complete the following steps:
#  (1) Complete the following function according to its docstring.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101
#      w08_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When you are convinced that your function is correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.
#
#      NOTE: To test this function, you will need to have your test .txt files
#      in the same folder.
#
#      You can use the sample_games.txt file to test your code, and you should
#      also test with some other files to convince yourself your code is working
#      correctly.
#
#      Tip: some programs like Notepad may show the .txt file all on one line.
#      You can try opening your .txt files in Wing101 instead.
#
#      You do not need to submit your .txt files.
#
# This problem is based on the Structured Files exercise from Week 7 Lecture,
# with two major changes:
# 1. The function should now return a dictionary with team names as keys and
#    the points as the values.
# 2. Team names may be repeated in the file, and should be combined into one
#    values list.
#
# Hint: Start with your code from the Week 7 points_per_game function.
# Make sure you have that code working, and you understand how it works,
# before making the changes for this new function.


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
input_file = open('NHL-data.txt')
get_game_dict(input_file)