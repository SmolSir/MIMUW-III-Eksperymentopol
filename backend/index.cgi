#!/home/bartosz/studia/M-I-semestr/Eksperymentopol/backend/.venv/bin/python3

from wsgiref.handlers import CGIHandler

from app import application

CGIHandler().run(application)
