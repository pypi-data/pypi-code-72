from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from bluedot_rest_framework.wechat import OfficialAccount
from apps.user.models import User
from apps.user.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([])
def event_register_template(request):
    token = request.data.get('token', None)
    event_id = request.data.get('event_id', None)
    unionid = request.data.get('unionid', None)
    first = request.data.get('first', None)
    keyword1 = request.data.get('keyword1', None)
    keyword2 = request.data.get('keyword2', None)
    keyword3 = request.data.get('keyword3', None)
    remark = request.data.get('remark', None)

    if token == 'KJHQJKBLJ4NIAQS9NRMITOUBHBF0EBM9':
        user_data = User.objects.filter(unionid=unionid).first()
        if user_data:
            template_data = {
                'user_id': user_data.offiaccount_openid,
                'template_id': 'vL7xuyNGeMkdbXj0cx-ZEGtTV64X2CCtwA0spohgtWc',
                'data': {
                    "first": {
                        "value": first,
                        "color": "#173177"
                    },
                    "keyword1": {
                        "value": keyword1,
                        "color": "#173177"
                    },
                    "keyword2": {
                        "value": keyword2,
                        "color": "#173177"
                    },
                    "keyword3": {
                        "value": keyword3,
                        "color": "#173177"
                    },
                    "remark": {
                        "value": remark,
                        "color": "#173177"
                    }
                },
                'url': f'https://spmi.bluewebonline.com/html/index.html?id={event_id}',
                'mini_program': None
            }
            result = OfficialAccount.message.send_template(**template_data)
            return Response({'code': '1000', 'msg': 'success'})
    return Response({'code': '1001', 'msg': 'Server Error'})
