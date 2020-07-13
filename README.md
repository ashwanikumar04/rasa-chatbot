# rasa-chatbot



```
python3 -m venv --system-site-packages ./venv
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip install rasa[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```


Used http://gamon.webfactional.com/regexnumericrangegenerator/ to generate range regex

https://forum.rasa.com/t/using-buttons-and-selecting-them-in-interactive-learning/3920/8

All the dependencies used for the bots are in `requirements.txt`


## Commands

To Train nlu

```
rasa train nlu
```

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