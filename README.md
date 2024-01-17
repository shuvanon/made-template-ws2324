# Analysis of the Relationship Between Weather Conditions and Traffic Offense Frequencies

## Project Overview
This study investigates the correlation between weather conditions and road speed limits within the Bonn city area. Additionally, it examines instances of traffic fines resulting from exceeding speed limits, exploring their relationship with temperature, wind, and precipitation on specific dates throughout the year 2022, spanning from January to December.

## Project Structure
```bash
├───examples
│       data-exploration-example.ipynb
│       final-report-example.ipynb
│       project-plan-example.md
│
├───exercises
│       exercise1.py
│       exercise2.jv
│       exercise3.py
│
└───project
    │   exploration.ipynb
    │   pipeline.sh
    │   project-plan.md
    │   report.ipynb
    │   requirements.txt
    │   tests.sh
    │
    ├───data
    │       .gitkeep
    │
    ├───data_pipeline
    │   │   config.yaml
    │   │   extract.py
    │   │   load.py
    │   │   mobilithek.py
    │   │   pipeline.py
    │   │   power_api.py
    │   │   transform.py
    │   │   __init__.py
    │   │
    │   
    └───tests
        │   test_extractor.py
        │   test_loader.py
        │   test_pipeline.py
        │   test_transformer.py
        │   __init__.py
```
## Key project files and their functions:
* `project/pipeline.sh`: It will run an automated ETL pipeline that creates a SQLite database named analysis.sqlite that contains required data.
* `project/tests.sh` : It will run the test cases for the ETL pipeline.

## Project Setup

1. Clone the repository:

```
git clone git@github.com:shuvanon/made-template-ws2324.git
```

2. Create a virtual environment:

```
python3.11 -m venv <env_name>
```

3. Activate the virtual environment:

```
source <env_name>/bin/activate
``` 

4. Install requirements:

```
pip install -r requirements.txt
```

5. Run data pipeline
```
python //data_pipeline/pipeline.py
```

6. Run Test
```
pytest -r project/tests
```
