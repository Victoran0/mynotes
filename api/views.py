from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import updateNote, getNoteDetails, deleteNote, getNoteList, createNote

# Create your views here.

@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        return Response(getNoteList(request))

    if request.method == 'POST':
        return Response(createNote(request))


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        return Response(getNoteDetails(request, pk))


    if request.method == 'PUT':
        return Response(updateNote(request, pk))

    if request.method == 'DELETE':
        return deleteNote(request, pk), Response("Note was deleted")

