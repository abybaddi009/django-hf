import torch

from pprint import pprint

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ReadingComprehensionSerializer

from .albert import tokenizer, model
from .forms import AskQuestionForm


class AskAPIView(APIView):
    serializer_class = ReadingComprehensionSerializer

    def post(self, request, *args, **kwargs):
        serializer = ReadingComprehensionSerializer(data=request.data)

        if serializer.is_valid():
            question = serializer.data.get("question")
            text = serializer.data.get("reading_comprehension")

            inputs = tokenizer(
                question, text, add_special_tokens=True, return_tensors="pt"
            )
            input_ids = inputs["input_ids"].tolist()[0]

            outputs = model(**inputs)
            pprint(outputs)

            answer_start_scores = outputs.start_logits
            answer_end_scores = outputs.end_logits

            answer_start = torch.argmax(
                answer_start_scores
            )  # Get the most likely beginning of answer with the argmax of the score
            answer_end = (
                torch.argmax(answer_end_scores) + 1
            )  # Get the most likely end of answer with the argmax of the score

            answer = tokenizer.convert_tokens_to_string(
                tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
            )

            print(f"Question: {question}")
            print(f"Answer: {answer}")

            return Response(
                data={
                    "reading_comprehension": text,
                    "question": question,
                    "answer": answer,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ask_question(request):
    # if this is a POST request we need to process the form data
    form = AskQuestionForm()
    answer = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AskQuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # return the answer
            question = form.cleaned_data.get("question")
            text = form.cleaned_data.get("passage")

            inputs = tokenizer(
                question, text, add_special_tokens=True, return_tensors="pt"
            )
            input_ids = inputs["input_ids"].tolist()[0]

            outputs = model(**inputs)
            pprint(outputs)

            answer_start_scores = outputs.start_logits
            answer_end_scores = outputs.end_logits

            answer_start = torch.argmax(
                answer_start_scores
            )  # Get the most likely beginning of answer with the argmax of the score
            answer_end = (
                torch.argmax(answer_end_scores) + 1
            )  # Get the most likely end of answer with the argmax of the score

            answer = tokenizer.convert_tokens_to_string(
                tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
            )

            print(f"Question: {question}")
            print(f"Answer: {answer}")

    return render(request, 'albert/Ask_Question.html', {'form': form, "answer": answer})
