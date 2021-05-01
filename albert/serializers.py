from rest_framework import serializers

class ReadingComprehensionSerializer(serializers.Serializer):
    reading_comprehension = serializers.CharField(style={'base_template': 'textarea.html'})
    question              = serializers.CharField()