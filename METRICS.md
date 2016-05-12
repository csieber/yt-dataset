# Dataset Metrics

One row in the CSV file equals one experiment run. The following table gives a brief description of all columns in the dataset.

## General & Target Metrics

### General

| Column               | Description                                               |
| -------------------- | --------------------------------------------------------- |
| run_id               | A unique identifier of the run.                           |
| run_id_nr            | A unique numeric identifier of the run.                   |
| run_start            | Unix timestamp of start of the experiment run.            |
| run_date             | Date (as string) the experiment run was started.          |
| run_length           | Duration of the whole run including set-up etc.           |
| run_length_ratio     | run_length / vid_length                                   |
| run_overlength       | run_length - vid_length                                   | 

### Redundant Traffic (RT)

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


