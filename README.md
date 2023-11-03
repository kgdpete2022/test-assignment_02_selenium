# test-assignment_02_selenium
Test assignment mini-project as part of skills assessment by a potential employer.

Note: Scenarios 1 and 2 work as planned, scenario 3 hasn't been completed as ChromeDriver blocks the download of .exe files (throws an alert which I couldn't work around).

## To install and run

1. Clone the repository to your computer:
```
git https://github.com/kgdpete2022/test-assignment_02_selenium.git
```

2. Setup and run the virtual environment:
```
python -m venv venv
source venv/Scripts/activate
```

3. Install dependencies:
```
pip install requirements.txt
```

4. Run pytest:
```
pytest <tests/filename>
```