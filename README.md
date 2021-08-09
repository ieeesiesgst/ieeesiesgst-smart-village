# IEEE SIESGST Smart Village Project

<p align="center">
  <img src="website/static/img/logo/IEEE SIESGST_white.png" alt='IEEE logo' width="200" /> 
  <img src="website/static/img/logo/ISV-LOGO-white.png" alt='ISV logo' width="200" /> 
</p>

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
python main.py
```

## Viewing The App

Go to `http://localhost:5000/`