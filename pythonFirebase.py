from firebase import firebase
from flask import Flask, request, jsonify, make_response

firebase = firebase.FirebaseApplication('https://loginreact-f8c1d.firebaseio.com')
class FirebaseUI():
    @classmethod
    def getData(self):
        result = firebase.get('/estado/login', None)
        print(result)
        return jsonify(result)

