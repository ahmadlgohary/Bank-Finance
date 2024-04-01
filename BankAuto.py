import pandas as pd
import os
from twilio.rest import Client
from cryptography.fernet import Fernet
from encryption import encrypt_file, decrypt_file


account_sid = os.environ["account_sid"] 
auth_token = os.environ["auth_token"] 
twilio_number = os.environ["twilio_number"] 
target_number = os.environ["target_number"]
encryption_key = os.environ["encryption_key"]
weekly_update = float(os.environ["weekly_update"])
savings_goal = int(os.environ["savings_goal"])
savings_goal_str = os.environ["savings_goal_str"]

key = Fernet(encryption_key)


def send_sms(text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body = f"\n{text}", from_= twilio_number, to = target_number)

file_path = os.path.join(os.getcwd(),"Bank.csv")
decrypt_file(key, file_path)

df = pd.read_csv(file_path)

df.loc[len(df.index)] = [weekly_update,None,None]

df['Total'][0] = sum(df['Income'])

df.to_csv(file_path, index= False)
encrypt_file(key, file_path)


if df['Total'][0] >= savings_goal:
    text = f"Congrats 🎉🎉 you have reached your goal of {savings_goal_str},\n you now have ${df['Total'][0]} in your savings account"
else: 
    text = f"You have ${df['Total'][0]} in your savings account"

send_sms(text)
    

