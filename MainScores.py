from flask import Flask

import Utils


def score_server():
    try:
        scores_file = open("C:\\Users\\roig\\Desktop\\Scores\\Scores.txt", 'r+')
        score = scores_file.read()
        scores_file.close()

        app = Flask(__name__)

        @app.route("/")
        def HTML_Score():
            return f"""         
            <html>
            <head>
            <title>Scores Game</title>
             </head>
            <body>
               <h1>The score is <div id="score">{score}</div></h1>
               </body>
            </html>
              """

        app.run(port=5000)

    except:
        def HTML_Score():
            return f"""
       <html>
           <head>
          <title>Scores Game</title>
           </head>
           <body>
           <body>
          <h1><div id="score" style="color:red">{Utils.BAD_RETURN_CODE}</div></h1>
           </body>
             </html>"""

        app.run(port=5000)
