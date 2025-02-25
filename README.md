# Audiobook_Downloader
 A python script to download mp3s from zaudiobooks for Windows and Android

 How to use:
    1. Make sure python is installed
        Windows - https://www.python.org/
        Android - Download Termux and run:
            pkg install python

    2. Install the python requests library
        Windows - in cmd/powershell:
            python -m pip install requests
        Android - in Termux:
            python -m pip install requests
    
    3. Download the Audiobook-Downloader script.

    4. Move the script to a seperate folder.

    5. Go to https://zaudiobooks.com/ and find an audiobook you want to download.

    6. Copy the address to the audiobook, for example:
        https://zaudiobooks.com/the-way-of-kings_t1/
    
    7. Change your working directory to the one where you placed the python script
        Windows - you can right click the folder and click "copy as PATH" and then in cmd/powershell:
            cd "path/to/your/folder"
        Android - Make sure Termux has access file permissions, then in Termux:
            cd ~/storage/shared
        You can then run the following command to view the folders you can go to.
            ls
        Navigate to the folder you put the python script in:
            cd "path/to/your/folder"

    8. Run the script in command line and give the link to your chosen audiobook (using The Way of Kings as an example)
        Windows - in cmd/powershell:
            python audiobook-downloader.py https://zaudiobooks.com/the-way-of-kings_t1/
        Android - in Termux:
            python audiobook-downloader.py https://zaudiobooks.com/the-way-of-kings_t1/
    
    9. The script will download all the mp3 files. You can listen to the audiobook using Smart Audiobook Player on Android to mimic an Audible-like experience. On Windows there isn't any good audiobook players but you could use VLC or transfer the files to your phone to listen on there.