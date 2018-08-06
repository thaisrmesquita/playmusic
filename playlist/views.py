from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from playlist.models import Record
from playlist.serializers import RecordSerializer


@api_view(['GET', 'POST'])
def record_list(request):
    if request.method == 'GET':
        records = Record.objects.all()
        records_serializer = RecordSerializer(records, many=True)
        return Response(records_serializer.data)
    elif request.method == 'POST':
        record_serializer = RecordSerializer(data=request.data)
    if record_serializer.is_valid():
        record_serializer.save()
    return Response(record_serializer.data, status=status.HTTP_201_CREATED)
    return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def record_detail(request,pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        record_serializer = RecordSerializer(record)
        return Response(record_serializer.data)
    elif request.method == 'PUT':
        record_serializer = RecordSerializer(record, data=request.data)
        if record_serializer.is_valid():
            record_serializer.save()
            return Response(record_serializer.data)
        return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)