# Django integration with Huggingface models for Q&A

This simple project outlines the methodology for integrating an huggingface model with Django for Q&A

## Description

The project contains a rest api end-point and a form which will enable the users to submit text passage and pose a question related to the passage.

The [large uncased bert model](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad) from huggingface has been used to generate an answer.

## Getting Started

### Dependencies

* Install the dependencies mentioned in the requrirements.txt


### Installing

* Clone the repository
* Create and activate your virtual environment
* Install the dependencies
`pip install requirements.txt`
* Clone the [model](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad) to your `BASE_DIR`
* Set the model's path in the `albert/albert.py`
```
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForQuestionAnswering.from_pretrained(model_path)
```
* Run the server
`python manage.py runserver`
* Navigate to http://localhost:8000/albert/ask/ for the html page
* Navigate to http://localhost:8000/albert/ask/api/ for the Rest API end-point

## To-do

The following features are planned:

* Annotator
* Model trainer
* Document store with ranking and retreival

## Authors

Contributors names and contact info

Abhishek Baddi [@abybaddi009](https://twitter.com/abybaddi009/)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the Burgerware License - see the LICENSE.md file for details
