Creat a virtual environment

    python3 -m venv env
    source venv/Scripts/activate

    pip install -r requirements.txt

    deactivate


To creat the exe to start the app ran on windows/bash

    touch bootstrap.sh

Set to exe
    chmod +x bootstrap.sh

Save to bootstrap.sh

export FLASK_APP=app.py
export FLASK_DEBUG=0
source venv/Scripts/activate
flask run -h 0.0.0.0



Run the App
./bootstrap.sh

export FLASK_DEBUG=1 To run tests