# IEEE SIESGST Smart Village Project

## Setup & Installtion

Make sure you have the latest version of Python installed.

1. Fork this repo
2. Clone your forked repo from github
    ```bash
    git clone <forked-repo-url>
    ```
3. Set remote url
    ```bash
    git remote add upstream https://github.com/ieeesiesgst/ieeesiesgst-smart-village.git
    ```

## Environment setup

```bash
# setup conda enironment
conda create --name <env_name> python

# install requirements
pip install -r requirements.txt
```

## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://localhost:5000/`