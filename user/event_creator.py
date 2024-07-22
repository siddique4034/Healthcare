import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main(apt, pt_email, dr_email):
      """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
          """
      creds = None
         # The file token.json stores the user's access and refresh tokens, and is
                # created automatically when the authorization flow completes for the first
                  # time.
      if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
                          # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                             creds.refresh(Request())
                    else:
                             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                             creds = flow.run_local_server(port=0)
                                                                          # Save the credentials for the next run
                             with open("token.json", "w") as token:
                                     token.write(creds.to_json())


      try:
          service = build("calendar", "v3", credentials=creds)
          event = {
              'summary': f'Apointment for {apt.required_speciacity} with Dr. {apt.doctor_appointed}',
              'location': '800 Howard St., San Francisco, CA 94103',
              'description': f'Appointment with {apt.doctor_appointed} for curing {apt.required_speciacity} of {apt.patient}.',
              'start': {
                  'dateTime': f'2015-05-28T09:00:00-07:00',
                  'timeZone': 'America/Los_Angeles',
              },
             'end': {
                 'dateTime': '2015-05-28T17:00:00-07:00',
                 'timeZone': 'America/Los_Angeles',
              },
              'recurrence': [
                    'RRULE:FREQ=DAILY;COUNT=2'
              ],
              'attendees': [
                  {'email': dr_email},
                  {'email': pt_email},
              ]
          }

          event = service.events().insert(calendarId='primary', body=event).execute()
          print(f"Event created {event.get('htmlLink')}")

      except HttpError as error:
            print(f"An error occurred: {error}")

