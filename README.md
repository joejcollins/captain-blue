# Captain Scarlet

## WSL Ubuntu 18.04



```
sudo apt-get install google-cloud-sdk=272.0.0-0
sudo apt-get install python3.7
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
sudo apt install python3-pip python3-setuptools python3.7-venv
sudo dpkg-reconfigure locales
python3 -m venv env
source env/bin/activate
pip install  -r requirements.txt
python main.py
```