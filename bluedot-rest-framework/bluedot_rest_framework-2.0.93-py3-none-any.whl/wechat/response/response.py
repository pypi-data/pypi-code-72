from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from wechatpy import parse_message, create_reply, utils
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from bluedot_rest_framework.analysis.monitor.models import AnalysisMonitor
from .. import OfficialAccount
from ..handle import WeChatUserSet
from .models import WeChatResponseMaterial, WeChatResponseEvent


class Response(APIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echo_str = request.GET.get('echostr')
        token = settings.WECHAT['OFFIACCOUNT']['TOKEN']
        utils.check_signature(token, signature, timestamp, nonce)
        return HttpResponse(echo_str)

    def post(self, request, *args, **kwargs):
        msg = parse_message(request.body)
        msg_dict = msg.__dict__['_data']
        data = {
            '_type': '微信响应日志',
            'user_openid': msg_dict['FromUserName'],
            'wechat_user_name': msg_dict['ToUserName'],
            'wechat_appid': settings.WECHAT['OFFIACCOUNT']['APPID'],
            'wechat_name': '',
            'wechat_event_key': '',
            'wechat_event_msg': '',
            'wechat_event_type': msg_dict['MsgType']
        }
        if 'EventKey' in msg_dict:
            data['wechat_event_key'] = msg_dict['Event']
        if 'Content' in msg_dict:
            data['wechat_event_msg'] = msg_dict['Content']
        elif msg_dict['MsgType'] == 'event':
            data['wechat_event_msg'] = msg_dict['EventKey']

        AnalysisMonitor.objects.create(**data)
        default_subscribe_text = """感谢关注"""

        default_subscribe_text_queryset = WeChatResponseEvent.objects.filter(
            event_type=0).first()
        if default_subscribe_text_queryset:
            queryset = WeChatResponseMaterial.objects.get(
                pk=queryset.material_id)
            default_subscribe_text = queryset.content

        if msg.type == 'text':
            queryset = WeChatResponseEvent.objects.filter(
                text=msg_dict['Content']).first()
            if queryset:
                queryset = WeChatResponseMaterial.objects.get(
                    pk=queryset.material_id)
                default_subscribe_text = queryset.content

        elif msg.type == 'event':
            if msg_dict['Event'] == 'unsubscribe':
                WeChatUserSet(
                    openid=msg_dict['FromUserName']).handle_subscribe(0)
            elif msg_dict['Event'] == 'SCAN' or msg_dict['Event'] == 'subscribe_scan':
                queryset = WeChatResponseEvent.objects.filter(
                    event_key=msg_dict['EventKey']).first()
                if queryset:
                    queryset = WeChatResponseMaterial.objects.get(
                        pk=queryset.material_id)
                    default_subscribe_text = queryset.content
            if 'subscribe' in msg_dict['Event']:
                WeChatUserSet(
                    openid=msg_dict['FromUserName']).handle_subscribe(1)

        reply = create_reply(default_subscribe_text, msg)
        response = HttpResponse(
            reply.render(), content_type="application/xml")
        return response
