# ChatBot
#Step one install the requirements.txt with 
pip install -r requirements.txt --> This will install the libaries needed

#Step two 
Make a .env file and add this line GROQ_API_KEY = YOURAPIKEY
Replace YOURAPIKEY with your groc key

#Step three
To run this code you need your own virtual enviroment 
Run these commands in the terminal 
venv/Scripts/activate
streamlit run frontend/app.py

This will run the code, if you look at models.json you can see all the models 
When deployment is done, all models can be accessed with the drop down. 
