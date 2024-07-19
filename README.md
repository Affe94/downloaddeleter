Scan download folder and target folder for same files and removes duplacates from download folder.
Download folder and target folder have to be specified in docker-compose.yml file.
Example:
```
services:
  downloaddeleter:
    image: downloaddeleter
    volumes:
      - c:\test_downloads:/downloads
      - c:\test_destination:/destination
    build:
      context: .
      dockerfile: ./Dockerfile

```

