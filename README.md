# ChatBot
#Step one install the requirements.txt with 
pip install -r requirements.txt --> This will install the libaries needed
Use this link to help set up .venv your virtual enviroment https://code.visualstudio.com/docs/python/environments#:~:text=Using%20the%20Create%20Environment%20command,environment%20types%3A%20Venv%20or%20Conda.

#Step two 
Make a .env file and add this line GROQ_API_KEY = YOURAPIKEY
Replace YOURAPIKEY with your groc key
Also add your own DB Cred
EX --> 
DB_USER=username
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=DBname


#Step three
To run this code you need your own virtual enviroment 
Run these commands in the terminal 
venv/Scripts/activate
streamlit run frontend/app.py

This will run the code, if you look at models.json you can see all the models 
When deployment is done, all models can be accessed with the drop down. 
