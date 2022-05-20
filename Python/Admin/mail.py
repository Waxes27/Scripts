from __future__ import print_function
import base64
import filecmp

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_message(service,msgId):
    txt = service.users().messages().get(userId='me', id=msgId).execute()
    return txt

def get_message_by_label(service,labelId,nextPage=""):
    txt = service.users().threads().list(userId='me', labelIds=labelId, maxResults=200).execute()
    return txt


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me',maxResults=1000).execute()
        messages = results.get('messages', [])

        if not messages:
            print('No labels found.')
            return
        counter = 0

        for message in messages:

            counter += 1
            txt = get_message(service,message['id'])
            txt = get_message_by_label(service,"Label_561763887185572634")
            # print(txt)
            # print(len(txt["threads"]))
            # print(txt['nextPageToken'])
        # exit()
            

            for i in txt["threads"]:
                try:
                    txt = get_message(service,i['id'])
                    # print(txt)
                except:
                    continue
                # print(service.users().messages().attachments().get(userId='me', messageId=i['id'],id=part['body']['attachmentId']).execute())
                
                
                payload = txt['payload']
                headers = payload['headers']

                for d in headers:
                    # print(d)
                    if d['name'] == 'Subject':
                        subject = d['value']
                    if d['name'] == 'From':
                        sender = d['value']
                # print(sender)
                if "Label_561763887185572634" in txt['labelIds']:

                    # if "student" in sender:
                    parts = payload['parts']
                    for part in parts:
                        if part['filename']:
                            file = service.users().messages().attachments().get(userId='me', messageId=message['id'],id=part['body']['attachmentId']).execute()['data']
                            file_data = base64.urlsafe_b64decode(file.encode('UTF-8'))
                            # print(part['filename'])
                            if not os.path.exists(sender):
                                os.mkdir(sender)
                            path = sender+"/"+part['filename']
                            # print(path)
                            
                            if not os.path.exists(path):
                                if ".eml" not in path:
                                    with open(path, 'wb') as f:
                                        f.write(file_data)
                                        print(f"written to: {path}")
                            else:
                                if ".eml" not in path:

                                    if not os.path.exists("tmp"):
                                        os.mkdir("tmp")
                                    os.mkdir("tmp/"+sender)

                                    with open("tmp"+"/"+path, 'wb') as f:
                                        f.write(file_data)

                                        if filecmp.cmp(path,"tmp/"+path):
                                            
                                            print(filecmp.cmp(path,"tmp/"+path))
                                            print(path)
                                        elif ".eml" not in path:
                                            # input(f"Check {path}")
                                            # input("write")
                                            path = path + str(time.time()) + ".pdf"
                                            with open(path, 'wb') as f:
                                                f.write(file_data)
                                            print(f"overwritten to: {path}")
                                # input("next")
                                os.system("rm -rf tmp")
                
        


    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()