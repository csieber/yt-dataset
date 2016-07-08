# Raw Experiment Logs

The raw experiment log files can be downloaded from Google Drive [here](https://drive.google.com/file/d/0B1GmpzRMOpwIbUZQeTZ2RnBVMUU/view?usp=sharing) (143 MB). An index file which translates video bytes to frame numbers and seconds of all evaluated videos can be downloaded [here](https://drive.google.com/open?id=0B1GmpzRMOpwIUlJNQndQQklGRnM) (23 MB).

## Structure

The structure of the archive looks as follows:

```
20151027 
        \
        -- 2d0waP14PDk
                       \
                       -- 201507130101cb904
                                            \
                                            -- channelhistogramvalue.csv
                                            -- experimentrun.csv
                                            -- [log files for each run] 
                       -- 20150713010319112
                       -- [experiment runs]
        -- 2ooqNPfSBSA
        -- [..videos..]
         
```

## Data Format Description

```
==== experimentrun.csv ====

^ Field                     ^ Field (long format)                       ^ Type     ^ Description                                                                      ^
| yt_id                     | YouTube video id used in this run         | char     | In this case not a key of Video table to not couple the two tables too tightly.  |
| start                     | Start of the experiment in seconds        | double   | Unix timestamp with at least milliseconds accuracy                               |
| end                       | End of the experiment in seconds          | double   | Unix timestamp "                                                                 |
| successful                | If the video was shown completely         | boolean  |                                                                                  |
| pl_height                 | Height of the player in pixels            | int      |                                                                                  |
| pl_width                  | Width of the player in pixels             | int      |                                                                                  |
| shaping_pattern           | Pattern file                              | char     |                                                                                  |
| vid_category              | Video category / search string            | char     | Query string used for searching YouTube for the videos                           |
|  Reserved for future use                                                                                                                                         ||||
| study                     | A string identifying the study            | char()   | e.g. "LAURENZ1"                                                                  |
| location                  | The location of the measurement           |          | e.g. MUC, US, etc.                                                               |
| forced_itag               | Maximilian study parameter. Forced itag.  | int      |                                                                                  |

==== requestlog.csv ====

The request log contains the (filtered) browser requests for the DASH segments.

^ Field                   ^ Field (long format)                     ^ Type     ^ Description                                                                                                              ^
| exp_run                 | KEY: exp_run id                         | int      | ID of the run.                                                                                                           |
| timestamp               | Request timestamp                       | double   | Timestamp since experiment start in seconds                                                                              |
| itag                    | iTag                                    | int      | Quality level                                                                                                            |
| req_domain              | Request domain                          | char     | Domain name from the request URL                                                                                         |
| req_range_start         | Requested range start (Byte)            | int      |                                                                                                                          |
| req_range_end           | Requested range end (Byte)              | int      |                                                                                                                          |
| resp_http_content_size  | Content-size                            | int      | Content-size from the HTTP response header                                                                               |
| tx_range_end            | Transferred range end (Byte)            | int      | When a connection abort happens, Bytes are only transferred up to tx_range_end (not including the tx_range_end'th Byte)  |
| tx_time                 | Transfer time in seconds                | double   | Time to complete the request (i.e. download time)                                                                        |
| tx_aborted              | Connection aborted                      | boolean  | Was the connection interrupted?                                                                                          |
| tx_md5                  | MD5 Hash of the transferred content     | char     |                                                                                                                          |
| tx_bytehdr              | First 50 Bytes of the received content  | char     | base64 encoded Bytes                                                                                                     |
==== channelhistogramvalue.csv ====

The channel histogram contains the values used for shaping the network connection.

^ Field      ^ Field (long format)                          ^ Type    ^ Description  ^
| exp_run    | KEY: Experiment run                          |         |              |
| timestamp  | Timestamp since experiment start in seconds  | double  | e.g. 2.5     |
| delay      | Channel delay in milliseconds                | int     | e.g. 50      |
| datarate   | Shaping rate of the channel in **Bit/s**     | int     |              |

==== playerlog.csv ====

The player log contains the metrics collected by the browser JavaScript monitor.

^ Field         ^ Field (long format)                                              ^ Type     ^ Description                                                                                           ^
| exp_run       | KEY: Experiment run                                              |          |                                                                                                       |
| timestamp     | Timestamp since experiment start in seconds                      | double   |                                                                                                       |
| video_time    | Video time in seconds as reported by the Player API              | double   | In seconds                                                                                            |
| buffer_level  | buffer level as reported by the Player API :!: Very unreliable!  | double   | In seconds                                                                                            |
| quality       | Played quality :!: Very unreliable!                              |          | Already shows a different quality when there will be switch in the future                             |
| status        | Playback status                                                  | integer  | [[https://developers.google.com/youtube/js_api_reference#Playback_status|YouTube API Status Values]]  |

==== yhtmlelement.csv ====

The YHTMLElement log describes which player element was loaded from the YouTube server.

^ Field    ^ Field (long format)           ^ Type    ^ Description  ^
| exp_run  | KEY: exp_run                  |         |              |
| name     | Name of the element           | char()  |              |
| size     | Size of the element in Bytes  | char()  |              |
| md5      | md5 hash of the element       | char()  |              |
```
