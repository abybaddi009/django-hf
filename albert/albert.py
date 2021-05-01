from django.conf import settings

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained(settings.BASE_DIR / "bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained(settings.BASE_DIR / "bert-large-uncased-whole-word-masking-finetuned-squad")

# for question in questions:
#     inputs = tokenizer(question, text, add_special_tokens=True, return_tensors="pt")
#     input_ids = inputs["input_ids"].tolist()[0]
    
#     outputs = model(**inputs)
#     answer_start_scores = outputs.start_logits
#     answer_end_scores = outputs.end_logits
    
#     answer_start = torch.argmax(
#         answer_start_scores
#     )  # Get the most likely beginning of answer with the argmax of the score
#     answer_end = torch.argmax(answer_end_scores) + 1  # Get the most likely end of answer with the argmax of the score
    
#     answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    
#     print(f"Question: {question}")
#     print(f"Answer: {answer}")