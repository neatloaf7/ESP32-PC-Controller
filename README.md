# ESP32-PC-Controller
Small touch screen interface for controlling PC using the ES3C28P dev kit

Board documentation [here](https://www.lcdwiki.com/2.8inch_ESP32-S3_Display)

# To Do
- Case
  - Finish LED diffuser layer
  - Design stand
- Firmware
  - UI
    - Create button and seek bar classes
    - Finalize theming
    - Implement album cover art
    - Implement touch controls
    - Implement status led
  - Serial
    - Create serial communication protocol
    - Figure out how to enable cdc data stream while being able to switch to REPL stream
    - Decode album art serial stream
- Software
  - Create python script(s) for linux and windows
    - Implement SMTC for windows, playerctl for linux
    - Implement API for liking and shuffling and album art
      - Conversely do all spotify api calls
    - Convert album art to bmp and send over serial
    - Identify correct device when plugged in
