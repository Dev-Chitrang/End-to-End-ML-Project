# End-to-End-ML-Project

## Create and activate virtual environment and install required packages (python).
```bash
    python -m venv name_of_environment
    .name_of_environment/Scripts/activate
    pip install -r requirements.txt
```

## Create and activate virtual environment and install required packages (Conda).
```bash
    conda create -n name_of_environment python=3.10 -y
    conda activate name_of_environment
    pip install -r requirements.txt
```

## Create and activate virtual environment and install required packages (uv).
```bash
    uv venv --python 3.10 name_of_environment
    .name_of_environment/Scripts/activate
    uv pip install -r requirements.txt
```