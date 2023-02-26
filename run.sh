#!/bin/bash
sudo pipenv shell
pip install -r requirements.txt
nohup streamlit run --server.port 8501 app.py &

