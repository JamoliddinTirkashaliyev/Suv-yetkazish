from rest_framework import serializers

from .models import *

from rest_framework.serializers import ModelSerializer



class SuvSerializers(ModelSerializer):
    class Meta:
        model = Suv
        fields = "__all__"
    def validated_litr(self, litr):
        if str(litr) > '19 litr':
            raise serializers.ValidationError("Yoshingiz mos kelmaydi!")
        return litr

class MijozSerializers(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"

class AdminSerializers(ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

    def validated_yosh(self, yosh):
        if int(yosh) > 19:
            raise serializers.ValidationError("Yoshingiz mos kelmaydi!")
        return yosh


class HaydovchiSerializers(ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"


class BuyurtmaSerializers(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def to_representation(self, instance):
        buyurtma = super(BuyurtmaSerializers, self).to_representation(instance)
        umumi_narx = Suv.objects.filter(buyurtma__id=buyurtma['id'])*buyurtma.miqdor
        buyurtma.update({"so'm": umumi_narx})
        return buyurtma

    def validated_mijoz_qarz(self, qarz):

        if int(qarz) > 500000:
            raise serializers.ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        return qarz


