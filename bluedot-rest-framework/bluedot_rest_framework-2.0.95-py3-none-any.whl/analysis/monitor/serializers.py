from rest_framework import serializers
from .models import AnalysisMonitor
from rest_framework.serializers import CharField, IntegerField, JSONField


class AnalysisMonitorSerializer(serializers.ModelSerializer):
    page_event_key = CharField(required=False)
    page_event_type = CharField(required=False)
    page_keywords = JSONField(required=False)
    user_ip = CharField(required=False)
    user_agent = JSONField(required=False)
    user_network = CharField(required=False)
    unionid = CharField(required=False)
    openid = CharField(required=False)
    _type = CharField(required=False)

    def create(self, validated_data):
        request = self.context['request']
        ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
            'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        validated_data['user_ip'] = ip
        return self.Meta.model.objects.create(**validated_data)

    class Meta:
        model = AnalysisMonitor
        fields = '__all__'
