# Flaskr - User Login & Register - Cart System

*In this application, you can find a simple flask template along with the cart system, admin panel, user login processes.*

## Install & Usage

- *Clone the repository*
```
git clone https://github.com/erkamesen/Flask-CartSystem.git
```
- *Change Directory*
```
cd ./Flask-CartSystem/
```

### Without Docker

- *Set your own virtual environment*
```
python3 -m venv venv
```
*Linux & MacOS*
```
source venv/bin/activate
```
*Windows*
```
.\venv\Scripts\activate
```

- *Install dependecies*
```
pip3 install -r requirements.txt
```

- *Run server*
```
python3 app.py
```

### With Docker

- *Build your image*
```
docker build -t <image_name> .
```
- *Run image*
```
docker run -p 8000:8000 <image_name>
```
- *Now you can connect to the server on http://127.0.0.1:8000*

