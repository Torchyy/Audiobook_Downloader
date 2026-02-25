# Audiobook Downloader
- A python script to download mp3s from [naudios](https://naudios.com) for Windows and Android.

## Windows or Android
- You can run this program on either OS, but if you are not tech savvy I recommend doing everything on Windows then transferring your files over to your phone.

## How to use
### 1. Make sure python is installed
#### Windows:
- Download and install [Python](https://www.python.org/).
#### Android:
- Download [Termux](https://play.google.com/store/apps/details?id=com.termux) from the Playstore and run `pkg install python`

### 2. Install the python requests library
#### Windows:
- In cmd/powershell run `python -m pip install requests`
#### Android:
- In Termux run `python -m pip install requests`

### 4. Download the script
- [Audiobook Downloader](https://github.com/Torchyy/Audiobook_Downloader/releases/download/v1.0.0/audiobook-downloader.py)

### 5. Move the script to a seperate folder

### 6. Find the ZAudiobook you want to download
- [naudios](https://naudios.com)

### 7. Copy the address to the audiobook, for example:
- `https://naudios.com/watch/202602258571`

### 8. Change your working directory to the one where you placed the python script
#### Windows:
- You can right click the folder that contains Audiobook_Downloader.py and click "show more options" > "copy as PATH" and then in cmd/powershell run `cd "path/to/your/folder"`
#### Android:
- Make sure Termux has access file permissions, then in Termux run `cd ~/storage/shared` to get to your primary storage
- You can view the folders you can go to by running `ls`
- Navigate to the folder you put the python script in `cd "path/to/your/folder"`

### 9. Run the script
- I am using The Way of Kings as an example, replace it link with your own.
#### Windows:
- In cmd/powershell run `python audiobook-downloader.py https://naudios.com/watch/202602258571`
#### Android
- In Termux run `python audiobook-downloader.py https://naudios.com/watch/202602258571`

### 10. Done
- The script will download all the mp3 files. You can listen to the audiobook using [Smart Audiobook Player](https://play.google.com/store/apps/details?id=ak.alizandro.smartaudiobookplayer) on Android to have an Audible-like experience. On Windows you could use [Audibly](https://github.com/rstewa/Audibly), VLC media player, or transfer the files to your phone to listen on there.
