# myo-gestures-control
Ability to control windows components &amp; webservices

## Requirements

- [six](https://pypi.python.org/pypi/six) for Python 2 and 3 compatibility
- pip install virtualenv

![Alt text](/window_powershell.PNG?raw=true "Windows Powershell script")

## Windows

git clone git@github.com:NiklasRosenstein/myo-python.git
virtualenv env --no-site-packages
env/Scripts/activate
pip install -e .
$env:Path = $env:Path + ";C:\Users\shafi\Documents\myo\myo-sdk-win-0.9.0"
python myo-python\examples\hello_myo.py

![Alt text](/output.PNG?raw=true "Myo Listener Output")

This project is licensed under the GNU License. 
Copyright &copy; 2015 Shafi Ulla


