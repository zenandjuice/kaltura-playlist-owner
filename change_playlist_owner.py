import datetime, math, time
from KalturaClient import *
from KalturaClient.Plugins.Core import *

def main():
    client = get_client()

    entry_list = open('change_playlist.txt', 'r')

    for entry in entry_list:
        playlistId, userId = entry.split("\t")
        playlist = KalturaPlaylist()
        playlist.userId = userId.strip()
        update_stats = False
        change_playlist(client, playlistId, playlist, update_stats)

    entry_list.close()


def change_playlist(client, playlistId, playlist, update_stats):
    try:
        result = client.playlist.update(playlistId, playlist, update_stats);
        print(playlistId,"owner changed");

    except Exception as e:
    	print(e)


def get_client():
    config = KalturaConfiguration()
    config.serviceUrl = "https://admin.kaltura.com/"
    client = KalturaClient(config)

    ks = client.session.start(
      "[KALTURA_API]",
      None,
      KalturaSessionType.ADMIN,
      [PID],
      432000,
	"appID:uark-change-owner"
      )
    client.setKs(ks)

    return client

main()
