from rest_framework import serializers

from main.models import AboutImage, AboutUs, Advantage, Footer, Help, News, Offerta, Question, Slider, SliderImage


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sliders_images'] = SliderImageSerializer(instance.sliders_images.all(), many=True, context=self.context).data
        return representation

class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = ('image',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AboutUsImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation   

class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = "__all__"


class OffertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offerta
        fields = "__all__"



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'answer')

class HelpSerializer(serializers.ModelSerializer):
    help = QuestionSerializer(many=True)
    class Meta:
        model = Help
        fields = "__all__"


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['header_num', 'header_img', 'footer_img', 'info', 'num', 'mail', 'instagram', 'whatsapp', 'telegram']


    
class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"


