# qa-challenge

## Configuration

To run tests in this project python is required.
I recommend using package and environment management such as Conda. Visit [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 
for installer information.

## Creating an environment

```bash
$ conda create -n qa-challenge python=3.8 
$ conda activate qa-challenge
$ pip install -r requirements.txt
```

## Running a test using pytest

```bash
$ cd /qa-challenge
$ pytest tests/ --html=./report/report-qa-challenge.html
```
 