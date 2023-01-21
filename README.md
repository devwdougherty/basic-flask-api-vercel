# basic-flask-api-vercel

# Setup

## Project

1. py -3 -m venv venv
2. venv\Scripts\activate
3. Add the requirements.txt file
4. Freeze it: ```pip3 freeze > requirements.txt```


## Flask

export FLASK_APP=index.py
export FLASK_ENV=development

# Vercel

1. Type ```vercel``` in project root folder. Follow up with deploy configurations.
2. Add the vercel.json file
3. Run ```vercel --prod```

