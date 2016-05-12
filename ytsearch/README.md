# YouTube search tool

Small script to query YouTube for videos watching the criteria used in the IFIP Networking 2016 study. Based on the YouTube Search API [1].

```bash
python3 ytsearch.py --query "minecraft" --max-results=5
```

Example output:

```bash
Video: JMpYYMtyKnM, length: PT31M17S
Video: NmhqqTF1BCU, length: PT14M57S
Video: jkJaGaEC6yk, length: PT20M19S
Video: jhR1LjWhW-8, length: PT9M36S
Video: 28hHCAyCRiw, length: PT14M34S
```

**Note** To use this script, add your API developer key to the ytsearch.py script.

## References

[1] https://developers.google.com/youtube/v3/docs/search/list

