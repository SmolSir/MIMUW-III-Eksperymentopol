# from flask import Flask, request
# from datetime import date
# from db_models import WordClassified, DaysWord, Ranking, Session

# import json
# import random

# application = Flask(__name__)


# @application.route('/')
# def index():
#     with Session.begin() as session:
#         guess = request.args.get("guess")
#         if not guess:
#             return json.dumps({"error": True, "text": "Could not find guess"})

#         with open("slowa.json", encoding="utf-8") as word_list_file:
#             word_list = json.load(word_list_file)
#             if guess.lower() not in word_list:
#                 return json.dumps({"error": True, "text": "Guess is not a valid word"})

#         guess = guess.upper()

#         todays_word = todays_guess(session)

#         answer = check_guess(guess, todays_word.word)

#         username = request.args.get("username")
#         current_streak = request.args.get("current_streak")

#         # Update activity statistics and ranking in db
#         todays_word.guesses += 1
#         if all(el == 2 for el in answer):
#             todays_word.solves += 1
#             if username:
#                 player_ranking = session.query(Ranking).filter(Ranking.username == username).one_or_none()
#                 if not player_ranking:
#                     return json.dumps({"error": True, "text": "Could not find user"})
#                 player_ranking.total_wins += 1
#                 player_ranking.max_streak = max(player_ranking.max_streak, int(current_streak) + 1)

#     return json.dumps(answer)


# def check_guess(guess, word):
#     answer = [0, 0, 0, 0, 0]
#     tmp_word = word
#     for i in range(5):
#         if word[i] == guess[i]:
#             answer[i] = 2
#             tmp_word = tmp_word.replace(word[i], "", 1)

#     for i in range(5):
#         if answer[i] != 2 and guess[i] in tmp_word:
#             tmp_word = tmp_word.replace(guess[i], "", 1)
#             answer[i] = 1

#     return answer


# def todays_guess(session):
#     todays_word_ob = session.query(DaysWord).filter(DaysWord.date == date.today()).one_or_none()
#     if not todays_word_ob:
#         todays_word_ob = DaysWord(date=date.today(), word=get_random_word(session), solves=0, guesses=0)
#         session.add(todays_word_ob)
#     return todays_word_ob


# def get_random_word(session):
#     words = session.query(WordClassified).filter(WordClassified.correct > 0).filter(WordClassified.wrong == 0).all()
#     return random.choice(words).word.upper()


# @application.route("/help_needed")
# def get_word_for_classification():
#     with Session.begin() as session:
#         words = session.query(WordClassified).filter(WordClassified.correct + WordClassified.wrong == 0).all()
#         return json.dumps({"word": random.choice(words).word, "count": len(words)}, ensure_ascii=False)


# def classify_word(word, classed):
#     with Session.begin() as session:
#         word_ob = session.query(WordClassified).filter(WordClassified.word == word).one_or_none()
#         if not word_ob:
#             return json.dumps({"error": True, "text": "Could not find word to classified"})
#         if classed == "correct":
#             word_ob.correct += 1
#         elif classed == "wrong":
#             word_ob.wrong += 1
#         else:
#             return json.dumps({"error": True, "text": "Could not find word to classified"})
#         return json.dumps({"error": False, "text": "Words db updated"})


# @application.route("/help_done")
# def classify_word_endpoint():
#     word = request.args.get("word")
#     classed = request.args.get("class")
#     return classify_word(word, classed)


# @application.route("/todays_word")
# def todays_word_endpoint():
#     with Session.begin() as session:
#         return json.dumps({"word": todays_guess(session).word})


# def get_ranking(how_many, ranking_type):
#     with Session.begin() as session:
#         data = []
#         if (ranking_type == "total_wins"):
#             ranking = session.query(Ranking).order_by(Ranking.total_wins.desc()).limit(how_many).all()
#             data = [[el.username, el.total_wins] for el in ranking]
#         elif (ranking_type == "max_streak"):
#             ranking = session.query(Ranking).order_by(Ranking.max_streak.desc()).limit(how_many).all()
#             data = [[el.username, el.max_streak] for el in ranking]
#         return data


# @application.route("/ranking")
# def get_ranking_endpoint():
#     how_many = int(request.args.get("how_many"))
#     ranking_type = request.args.get("ranking_type")
#     return json.dumps(get_ranking(how_many, ranking_type))


# @application.route("/add_user")
# def add_user():
#     username = request.args.get("username")
#     total_wins = int(request.args.get("total_wins"))
#     max_streak = int(request.args.get("max_streak"))
#     with Session.begin() as session:
#         user = session.query(Ranking).filter(Ranking.username == username).one_or_none()
#         if user:
#             return json.dumps({"error": True, "text": "Username taken"})
#         player_ranking = Ranking(username=username, total_wins=total_wins, max_streak=max_streak)
#         session.add(player_ranking)
#     return "{}"
