## Date parser

Dateparser is a Python library that makes it easy to parse strings into datetime objects. I have used it in several projects. 

Here is an example of how to use dateparser:

{% gist 60293b2bb9a03c64396d4d597a0fd6b3 %}

In this example, we first import the dateparser module. Then, we use the search function to find and parse a date in the string. Compare to spacy NLP date detection model, I feel it slower but more accurate. 

{% gist fa82b3149212d603e7af9483d7d762a7 %}