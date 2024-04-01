# Bank-Finance

 Welcome to my Automated Personal Finance app! Here, I present a Python script that utilizes APIs, encryption, and CI/CD deployment, to send text messages with my savings account status on Fridays at 4:00 AM EST. 
 This script seamlessly manages a CSV file with the following capabilities:

1. **Decryption**: Utilizes cryptographic techniques to decrypt CSV files securely using a Symmetric key.

2. **Pandas Integration**: Utilizes pandas library to read and manipulate CSV data.

3. **Updating and Saving**: Updates the CSV data and ensures changes are saved back to the file.

4. **Encryption for Data Privacy**: Implements encryption using a Symmetric key, maintaining data confidentiality throughout the process.

5. **Twilio API Integration**: Demonstrates integration with the Twilio API to send text messages, providing weekly  notifications for updates.

## Requirements

To run this program, Install the following:
- Python 3
- pandas
- cryptography
- Twilio Python library

## Executing The Program 

1. Clone this Repo
2. Install the libraires `pip install pandas, cryptography, twilio`
3. Prepare a CSV file to be processed and place it in the same directory as the script.<br>
    **CSV Format**
    |Income|Total|
    |:-----|:----|
    |*X amount*|*sum of Income columns*|
    |*Y amount*|
    |*Z amount*|
4. Add your tokens, target, weekly_update, etc
   ```
    account_sid      =  'Your twilio key here'
    auth_token       =  'Your twilio key here'
    twilio_number    =  'Your twilio number here'
    target_number    =  'Your phone number here'
    weekly_update    =  'weekly amount added'
    savings_goal     =  'your savings goal'
    savings_goal_str =  'saving goal as a string, 1k, 2k etc'
    encryption_key   =  'your encryption key'
   ``` 
   Keep these values safe.
   I have mine encrypted in the environment varibles 
5. Execute the script: `python BankAuto.py`


