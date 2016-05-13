# YouTube - Dataset of 10k evaluated video views

A dataset of over 10k evaluated YouTube video streaming sessions collected at the end of 2015 in a testbed at Technical University of Munich, Germany. Published on IFIP Networking Conference in 2016, Vienna, Austria ([Paper Download](http://www.lkn.ei.tum.de/forschung/publikationen/dateien/Sieber2016SacrificingEfficiencyforQuality.pdf)).

## Files

 * *data/ifip\_networking.csv.gz*: Dataset in CSV format.
 * *data/ifip\_networking.arff.gz*: Dataset in [ARFF](http://www.cs.waikato.ac.nz/ml/weka/arff.html) format for use with [WEKA](http://www.cs.waikato.ac.nz/~ml/)

## Columns / Metric Description

Refer to [METRICS.md](METRICS.md) for a detailed description of the columns in the dataset.

## Notebooks

We provide the following notebooks as guideline to the dataset:

  * [avg\_quality](notebooks/avg_quality.ipynb): How to plot network shaping to average quality

## Raw Experiment Logs

Information about the raw experiment logs can be found in [RAW.md](RAW.md).

## YouTube Video Selection Tool

Please see [here](ytsearch/README.md) for a description and the script how we automatically selected the videos.

## CITATION

If you are using this dataset for scientific publications, please cite the following paper:

Christian Sieber, Poul Heegaard, Tobias Hoßfeld, Wolfgang Kellerer, *Sacrificing Efficiency for Quality of Experience: YouTube’s Redundant Traffic Behavior *, IFIP Networking 2016, Vienna, Austria

Bibtex:

```
@INPROCEEDINGS{sieber16sacrificing,
  author="Christian Sieber and Poul E. Heegaard and Tobias {Ho{\ss}feld} and Wolfgang Kellerer",
  title="Sacrificing Efficiency for Quality of Experience: {YouTube's} Redundant Traffic Behavior",
  booktitle="IFIP Networking 2016 Conference (Networking 2016)",
  address="Vienna, Austria",
  month={May},
  year=2016
}
```

