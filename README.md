# Juno Download Crawler


Crawls [Juno Download](http://www.junodownload.com "Juno Download") and collects data on the entire back catalogue of music singles.

Fields collected:
- Artist
- Title
- Record label
- Catalog number
- Release date
- Music genre
- Individual track names
- mp3 sample urls

Example output code:

```json
[
  {
    "_type": "JunoCrawlerItem",
    "catalog_number": "SB 215-0",
    "title": "Tell Me",
    "release_date": "10 Sep 08",
    "artist": "CLEAR VIEW feat JESSICA",
    "label": "Songbird Holland",
    "tracks": [
      [
        "Tell Me - (6:43)",
        "http://www.junodownload.com/MP3/SF1354749-02-01-01.mp3"
      ],
      [
        "Tell Me (Max Graham remix) - (8:49)",
        "http://www.junodownload.com/MP3/SF1354749-02-01-02.mp3"
      ]
    ],
    "genre": "Progressive House"
  }
]
```
