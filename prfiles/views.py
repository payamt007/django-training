from django.shortcuts import render

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import os
import magic
from rest_framework.views import APIView


class UploadHandlerView(APIView):
    """
    A view that can accept POST requests with File content.
    """
    parser_classes = [FileUploadParser]

    # def post(self, request, format=None):
    #    return Response({'received data': request.data})

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        print('file recieved here')
        # print(os.stat(file_obj))
        #file_type = file_obj.content_type.split('/')[0]
        #file_type = magic.from_buffer(open(file_obj, "rb").read(2048))

        # print(file_type)

        m = magic.Magic()
        #m.getparam
        tp = m.from_buffer(file_obj.read(2048))
        print(tp)

        # with open('files/name.jpg', 'wb+') as destination:
        #    for chunk in file_obj.chunks():
        #        destination.write(chunk)
        #    print(magic.from_file(destination.name, mime=True))

        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204, data={"done": True})
