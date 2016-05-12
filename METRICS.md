# Dataset Metrics

One row in the CSV file equals one experiment run. The following table gives a brief description of all columns in the dataset.

## General

| Column               | Description                                               |
| -------------------- | --------------------------------------------------------- |
| run_id               | A unique identifier of the run.                           |
| run_id_nr            | A unique numeric identifier of the run.                   |
| run_start            | Unix timestamp of start of the experiment run.            |
| run_date             | Date (as string) the experiment run was started.          |
| run_length           | Duration of the whole run including set-up etc.           |
| run_length_ratio     | run_length / vid_length                                   |
| run_overlength       | run_length - vid_length                                   | 

## Redundant Traffic (RT)

| Column                | Description                                               |
| --------------------- | --------------------------------------------------------- |
| rnd_traffic_boolean   | if redundant traffic > 0                                  |
| rnd_traffic           | Redundant traffic (RT) in percent.                        |
| rnd_traffic_sec       | Sum of segment duration discarded in playback seconds.    |
| rnd_traffic_bytes     | Sum of segment sizes discarded in Bytes.                  |

## Loss in quality due to RT

| Column               | Description                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------ |
| gain_possible_ql     | Avg. quality level possible based on downloaded data. <br>Determined using isotonic regression.  |
| gain_ql_diff         | gain_possible_ql - pl_avg_assumed_quality_ql                                                     |
| gain_ql_diff_perc    | gain_ql_diff / pl_avg_assumed_quality_ql                                                         |

## Player / Playback Metrics

| Column                         | Description                                               |
| ------------------------------ | --------------------------------------------------------- |
| pl_detected                    | If the measurement system detected the player object.     |
| pl_version                     | First three digits of player MD5 hash.                    |
| pl_avg_assumed_quality_ql      | Average (assumed) quality level (starting from 0)         |
| pl_avg_pl_quality_ql           | Average quality level as reported by player (start 0)     |
| pl_buffering_events            | Number of observed buffering events.                      |
| pl_buffering_boolean           | pl_buffering_events > 0                                   |
| pl_norm_buf_events             | Number of observed buffering events (per minute)          |
| pl_assumed_switches            | Number of assumed quality switches.                       |
| pl_guessed_switches            | Number of guessed quality switches. Unreliable!           |
| pl_estimated_switches          | round((assumed + guessed) / 2). Unreliable!               |
| pl_norm_est_switches           | pl_estimated_switches (per minute)                        |
| pl_switches_boolean            | pl_estimated_switches > 0                                 |
| pl_time_spent_itagXXX          | Time spent on itag XXX.                                   |
| pl_time_spent_norm_itagXXX     | Time spent on itag XXX / vid_length                       |
| pl_avg_req_size                | Average requested segment size (bytes)                    |
| pl_avg_req_size_sec            | Avg. req. segm. size (seconds). -1 if never requested     |

## Network Metrics

| Field                   | Description                            |
| ----------------------- | -------------------------------------- |
| net_avg_shaping_rate    | Average shaping rate in Bytes/s.       |
| net_dl_total            | Total downloaded Bytes.                |
| net_played_bytes        | (Assumed) Bytes shown to the user.     |

## Video Metrics

| Field                | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| yt_id                | YouTube-ID of the video.                                   |
| content_id           | Random numeric video id. Only valid per csv export.        |
| vid_category         | Video category (e.g. ‘music’)                              |
| vid_length           | Video length in seconds.                                   |
| vid_category_id      | Random numeric category id. Only valid per csv export.     |
| hbm1                 | HTTP-Adaptive Bitrate Deviation Metric v1.                 |
| hbm2                 | HTTP-Adaptive Bitrate Deviation Metric v2.                 |
| br_distance_metric   | Bit-rate distance metric.                                  |
| br_non_monoton       | True if the bit-rate of a higher layer < lower layer.      |
| br_avg_iXXX          | Average bit-rate of itag XXX.                              |
| br_avg_norm_iXXX     | Average bit-rate of itag XXX norm. by avg. shaping         |
| br_std_iXXX          | Std of itag XXX.                                           |


