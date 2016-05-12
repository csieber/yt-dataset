#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import datetime
import dateutil.relativedelta

# PUT YOUR DEVELOPER KEY HERE
DEVELOPER_KEY = "## PUT YOUR KEY HERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(searchString, maxResults):

    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Only consider videos between one and 9 month old.
    notAfter  = datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
    notBefore = datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-9)

    parameters = {              'q': searchString,
                             'type': "video",
                             'part': "id",
                       'maxResults': maxResults,
                  'videoEmbeddable': "true",
                  'videoSyndicated': "true",
                            'order': "viewCount",
                  'videoDefinition': "high",
                   'videoDimension': "2d",
                  'publishedBefore': notAfter.isoformat("T").split(".")[0] + "Z",
                   'publishedAfter': notBefore.isoformat("T").split(".")[0] + "Z"}

    print(parameters)

    search_response = youtube.search().list(**parameters).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result["id"]["videoId"])

    for videoId in videos:

        video_response = youtube.videos().list(id=videoId, part='contentDetails').execute()

        print("Video: %s, length: %s" % (videoId, video_response["items"][0]["contentDetails"]["duration"]))

if __name__ == "__main__":

    argparser.add_argument("--query", help="Search string", default="music video")
    argparser.add_argument("--max-results", help="Max YouTube results", default=25)

    args = argparser.parse_args()

    try:
        youtube_search(args.query, args.max_results)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
