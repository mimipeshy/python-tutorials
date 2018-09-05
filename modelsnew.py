from flask import Flask, jsonify, make_response
from flask_restful import Api, request, abort

app = Flask(__name__)
api = Api(app)

user = []
user_id = 1


rides = {}
ride_id = 1
#
# requests = {}
# request_id = 1


class Users():
    def __init__(self, first_name, last_name, username, email, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    global users
    global user_id

    def get_all_users(self):
        """this retrieves all users"""
        return users

    def get_one_user(self, user_id):
        """gets a specific user using id"""
        if users in user_id:
            user = users[user_id]
        return user

    def create_new_user(self, username, first_name, last_name, email, password, confirm_password):
        """this creates a new user"""
        if not request.json or not 'user' in request.json:
            abort(400)
        user = [
            {
                "id": users[-1]['id'] + 1,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "password": password,
                "confirm_password": confirm_password
            }
        ]
        users.append(user)
        return jsonify({'user': user}), 201
        # return make_response(jsonify({"successfully created a user": user}), 201)
        # # user = {
        # #     "first_name": first_name,
        # #     "last_name": last_name,
        # #     "username": username,
        # #     "email": email,
        # #     "password": password,
        # #     "confirm_password": confirm_password
        # # }
        # #
        # # # users[user_id] = user
        # # # user_id = len(user_id)+1
        #
        # return make_response(jsonify({"successfully created a user": user}), 201)

    def update_user(self, user_id):
        """this updates a user details"""
        pass

    def delete_user(self, user_id):
        """deletes one user"""
        if user_id in users:
            del users[user_id]
            return make_response(jsonify({"message": "user successfully deleted"}), 200)


class Rides:
    def __init__(self, ride, driver_id, departure_time, numberplate, maximum, status):
        self.ride = ride
        self.driver_id = driver_id
        self.departure_time = departure_time
        self.numberplate = numberplate
        self.maximum = maximum
        self.status = status

    @classmethod
    def create_ride(cls, ride, driver_id, departuretime, numberplate, maximum, status="pending"):
        """Creates a new ride"""

        cls(ride, driver_id, departuretime, numberplate, maximum, status)
        return make_response(jsonify({"message": "ride has been successfully created"}), 201)

    def update_ride(ride_id, ride, driver_id, departuretime, numberplate,
                    maximum):
        """this updates a ride"""
        pass

    def start_ride(ride_id, driver_id):
        """starts a ride"""
        pass

    @staticmethod
    def delete_ride(ride_id):
        """Deletes a ride"""
        for ride in rides:
            if ride[0] == ride_id:
                return make_response(jsonify({"message": "ride has been successfully deleted"}), 200)
            return make_response(jsonify({"message": "user does not exists"}), 404)

    def get_ride(ride_id):
        """Gets a particular ride"""
        if ride_id.ride != []:
            ride= ride_id.ride[0]
            info = {ride[0] : {"ride": ride[1],
                                "driver_id": ride[2],
                                "departure_time": ride[3],
                                "cost": ride[4],
                                "maximum": ride[5],
                                "status": ride[6]}}
            return make_response(jsonify({"ride" : info}), 200)
        return make_response(jsonify({"message" : "ride does not exists"}), 404)

    def get_all_rides(self):
        """Gets all rides"""
        all_rides = []
        for ride in rides:
            info = {ride[0] : {"ride": ride[1],
                                "driver_id": ride[2],
                                "departure_time": ride[3],
                                "cost": ride[4],
                                "maximum": ride[5],
                                "status": ride[6]}}
            all_rides.append(info)
        return make_response(jsonify({"All rides" : all_rides}), 200)
