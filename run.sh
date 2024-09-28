pip install -r requirements.txt
pytest test_qod_web.py -v -s
pytest --html=report.html