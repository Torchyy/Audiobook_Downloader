# Audiobook Downloader
 A python script to download mp3s from zaudiobooks for Windows and Android.

## How to use
### 0. Windows or Android
 You can run this program on either OS, but if you are not tech savvy I recommend doing everything on Windows then transferring your files over to your phone.
 
### 1. Make sure python is installed
 #### Windows:
  Download and install [Python](https://www.python.org/).
 #### Android:
  Download [Termux](https://play.google.com/store/apps/details?id=com.termux) from the Playstore and run `pkg install python`

### 2. Install the python requests library
 #### Windows:
 In cmd/powershell run `python -m pip install requests`
 #### Android:
 In Termux run `python -m pip install requests`

### 4. Download the Audiobook Downloader script

### 5. Move the script to a seperate folder

### 6. Go to [zaudiobooks](https://zaudiobooks.com/) and find an audiobook you want to download

### 7. Copy the address to the audiobook, for example:
 `https://zaudiobooks.com/the-way-of-kings_t1/`

### 8. Change your working directory to the one where you placed the python script
 #### Windows:
 You can right click the folder that contains Audiobook_Downloader.py and click "show more options" > "copy as PATH" and then in cmd/powershell run `cd "path/to/your/folder"`
 #### Android:
 Make sure Termux has access file permissions, then in Termux run `cd ~/storage/shared`
 You can then run the following command to view the folders you can go to `ls`
 Navigate to the folder you put the python script in `cd "path/to/your/folder"`

### 9. Run the script in command line and give the link to your chosen audiobook
I am using The Way of Kings as an example, replace the way of link with your own.
 #### Windows:
 In cmd/powershell run `python audiobook-downloader.py https://zaudiobooks.com/the-way-of-kings_t1/`
 #### Android
 In Termux run `python audiobook-downloader.py https://zaudiobooks.com/the-way-of-kings_t1/`

### 10. Done
The script will download all the mp3 files. You can listen to the audiobook using [Smart Audiobook Player](https://play.google.com/store/apps/details?id=ak.alizandro.smartaudiobookplayer) on Android to have an Audible-like experience. On Windows there isn't any good audiobook players but you could use VLC media player or transfer the files to your phone to listen on there.
