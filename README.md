# rasa-chatbot

## Python version 3.7.4


```
python3 -m venv --system-site-packages ./venv
source ./venv/bin/activate
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip install rasa[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```


Used http://gamon.webfactional.com/regexnumericrangegenerator/ to generate range regex


Looks like there is sometime an issue with shell when selecting items from menu. For some weird reason the menu for price works in interactive mode but sometime it does not work in `shell`. Reference for the issue 
https://forum.rasa.com/t/using-buttons-and-selecting-them-in-interactive-learning/3920/8




So please test using custom messages.



All the dependencies used for the bots are in `requirements.txt`


## Commands


To Train

```
rasa train
```


To run actions

```
rasa run actions
```

To test
```
rasa test
```