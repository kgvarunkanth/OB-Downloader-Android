# Youtube-Downloader-Android(New Feature: Torrent Downloader)
  It is a Termux based command line Youtube video and audio and also Torrent downloader using Binaries: yt-dlp, ffmpeg and Transmission GTK.
  
# Features:
 YOUTUBE:
  * Multi-Threaded download
  * Single file or entire Yt playlist download
  * Supports Youtube Music too
  * Audio are downloaded along with Thumbnails and Meta Data
  * Video mode supports upto 4K resolution download
  * Audio mode supports all codecs
  * Best mode for hazel free quick download
  * Advance mode for Advanced users
  * This script also supports few other video streaming platforms too..
 TORRENT:
  * Torrents can be downloaded by just sharing magnet using termux
 
# Installation:
  1. Install termux from playstore or with link: https://play.google.com/store/apps/details?id=com.termux
  2. Type the commands or just copy and paste in termux:
        1) pkg up -y
        2) pkg install git -y
        3) git clone https://github.com/DrDelin/Youtube-Downloader-Android
        4) cd Youtube-Downloader-Android
        5) sh install.sh

# Usage

  YOUTUBE:
    * Select SHARE option in the video or playlist you wants to download
    * Select TERMUX in the options to share
    * Rest is self explainatory in Program
  
  YOUTUBE MUSIC:
    * Similar to youtube feature select share in req song or playlist
    * Select Termux
    * Type the required audio codec
    * Enjoy
   
  TORRENT:
     * For torrent download itorrents app from play store or using link: https://play.google.com/store/apps/details?id=com.icodelife.itorrentsearch&hl=en_IN&gl=US
     * It is a torrent searching platform from famous torrent searching engines like piratebay rabg etc..
     * Search your torrent 
     * Select share option followed by select Termux
     * File starts downloading
     * After 100% download Select Ctrl and C (ctrl + c) in termux to avoid seeding or data loss
     
  