import Utils
from MainScores import score_server

def Add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        scores_file = open(Utils.SCORES_FILE_NAME, 'r+')
        score = scores_file.read()
        scores_file.truncate(0)
        scores_file.close()
        scores_file = open(Utils.SCORES_FILE_NAME, 'w')
        score_update = int(score) + POINTS_OF_WINNING
        scores_file.write(str(score_update))
        scores_file.close()
    except:
        scores = open(Utils.SCORES_FILE_NAME, 'w')
        scores.write(POINTS_OF_WINNING)
        scores.close()
    score_server()

