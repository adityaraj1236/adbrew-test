from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os, re
from pymongo import MongoClient , errors

logger = logging.getLogger(__name__)

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']
todos_collection = db["todos"]
def validate_task(task: str):
    if not isinstance(task, str):
        return "Task must be a string"

    task = task.strip()

    if len(task) == 0:
        return "Task cannot be empty"

    if len(task) > 200:
        return "Task must be under 200 characters"
    if re.search(r"[<>;$]", task):
        return "Task contains invalid characters"

    return None
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
            task = request.data.get("task", "")

            validation_error = validate_task(task)
            if validation_error:
                return Response(
                    {"error": validation_error},
                    status=status.HTTP_400_BAD_REQUEST
                )

            todos_collection.insert_one({"task": task.strip()})

            return Response(
                {"message": "Task created successfully", "task": task},
                status=status.HTTP_201_CREATED
            )

        except errors.PyMongoError as db_error:
            logger.error(f"Mongo Write Error: {db_error}")
            return Response(
                {"error": "Database write error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            logger.exception("Unexpected POST error")
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )