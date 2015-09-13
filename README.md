# myo-gestures-control
Ability to control windows components &amp; webservices

## Requirements

- [six](https://pypi.python.org/pypi/six) for Python 2 and 3 compatibility
- pip install virtualenv

# Windows Evironment Setup using powershell
$env:Path = $env:Path + ";C:\Users\shafi\Documents\myo\myo-sdk-win-0.9.0"

### Windows

git clone git@github.com:NiklasRosenstein/myo-python.git
virtualenv env --no-site-packages
env/Scripts/activate
pip install -e .
set PATH=%PATH%;.\myo-sdk-win-0.9.0\bin
python myo-python\examples\hello_myo.py


This project is licensed under the GNU License. Copyright &copy; 2015 Shafi Ulla

