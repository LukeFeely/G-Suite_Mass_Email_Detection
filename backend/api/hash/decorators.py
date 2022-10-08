from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        hashValue = args[0].request.data.get("hashValue", "")
        #count = args[0].request.data.get("count", "")
        if not hashValue:# and not count:
            return Response(
                data={
                    #"message": "Both hashValue and Count are required to add a song"
                    "message": "A hashValue is required to add a record"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated