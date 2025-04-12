import instaloader
import csv
import os
import time
from getpass import getpass

#replace with your instagram username
USERNAME = "your_insta"  #your instagram username

#prompt for password securely
PASSWORD = getpass("enter your instagram password: ")  #securely input your password

#initialize instaloader
L = instaloader.Instaloader()

#try to log in with the username and password
try:
    L.login(USERNAME, PASSWORD)  #attempt to log in
    L.save_session_to_file()  #save the session so you don’t need to log in again
    print("login successful and session saved.")
except Exception as e:
    print(f"error logging in: {e}")  #show error if login fails
    exit()

#try loading the saved session
try:
    L.load_session_from_file(USERNAME)  #load the saved session
    print("session loaded successfully.")
except Exception as e:
    print(f"could not load session: {e}")  #show error if session loading fails
    exit()

try:
    #get profile data
    profile = instaloader.Profile.from_username(L.context, USERNAME)  #fetch profile info using the username

    print("fetching the accounts you follow...")
    following = set(profile.get_followees())  #get the list of accounts you follow
    time.sleep(5)  #short delay to avoid instagram blocking

    print("fetching your followers...")
    followers = set(profile.get_followers())  #get the list of your followers
    time.sleep(5)  
  
    print("comparing followers and following...")
    not_following_back = following - followers  

    #generate a unique filename for the report
    output_file = "followers_report.csv" 
    i = 1
    while os.path.exists(output_file):  
        output_file = f"followers_report_{i}.csv"  #create a new file name if the original one exists
        i += 1

    #write the data to a CSV file
    with open(output_file, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["type", "username"])  

        for user in following:
            writer.writerow(["you follow", user.username])  

        for user in followers:
            writer.writerow(["follows you", user.username])  
          
        for user in not_following_back:
            writer.writerow(["doesn't follow back", user.username])  
          
    print(f"done! {len(not_following_back)} users don’t follow you back.")
    print(f"report saved as: {output_file}") 

except Exception as e:
    print(f"error during data collection: {e}")  #show error if data collection fails
