import json

from rest_framework.views import APIView
from rest_framework.response import Response
from typing import TypedDict

User = TypedDict('User', {'name': str, 'age': int})


class UsersListCreateView(APIView):
    _users: list[User] = []
    try:
        with open('users.json') as file:
            _users: list[User] = json.load(file)
    except:
        pass

    @classmethod
    def get(cls, *args, **kwargs):
        return Response(cls._users)

    def post(self, *args, **kwargs):
        try:
            with open('users.json', 'w') as file:
                user = self.request.data
                UsersListCreateView._users.append(user)
                json.dump(UsersListCreateView._users, file)
        except Exception as err:
            print(err)
            return Response(f'{err}')
        else:
            return Response('created')
