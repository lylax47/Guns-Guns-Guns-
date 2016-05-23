import pprint

from googleapiclient.discovery import build


def main():
  service = build("customsearch", "v1",
            developerKey="AIzaSyCzi_hdGulgbBdQ9W4Qp6Pe3pzzUhi1lXQ")

  res = service.cse().list(
      q='gun control',
      cx='010770280927322544470:aaqvdbloxhw',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()