from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient , errors

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']
todos_collection = db["todos"]

class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        try:
            todos = list(todos_collection.find({}, {"_id": 0}))
            return Response(todos, status=status.HTTP_200_OK)

        except errors.PyMongoError as db_error:
            return Response(
                {"error": "Database read error", "details": str(db_error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            return Response(
                {"error": "Unexpected server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        try:
            task = request.data.get("task", "").strip()
            if not task:
                return Response(
                    {"error": "Task is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            todos_collection.insert_one({"task": task})

            return Response(
                {"message": "Task created successfully", "task": task},
                status=status.HTTP_201_CREATED
            )

        except errors.PyMongoError as db_error:
            return Response(
                {"error": "Database write error", "details": str(db_error)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            return Response(
                {"error": "Unexpected server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )    