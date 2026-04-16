# WSAA Coursework

A collection of labs and assignments for the Web Services Applications and Architecture (WSAA) course.

## Project Structure

```
WSAA-coursework/
├── assignments/          # Course assignments
│   ├── assignment2-carddraw.ipynb       # Card drawing assignment
│   ├── assignment03-cso.ipynb           # CSO API data assignment
│   ├── assignment04-github.py           # GitHub API assignment
│   └── config.py                        # Configuration (API keys)
│
└── labs/                 # Lab exercises
    ├── Lab_2:RepresentingData.ipynb     # Data representation lab
    ├── Lab_2:Trains.ipynb               # Train data processing lab
    ├── lab_4_api.ipynb                  # GitHub API lab
    └── config.py                        # Configuration (API keys)
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   - Create `assignments/config.py` and `labs/config.py` with:
     ```python
     apikeys = {
         "githubkey": "your_github_token_here"
     }
     ```
   - Or set environment variables: `GITHUB_TOKEN` or `GITHUB_KEY`

3. **Run assignments:**
   ```bash
   # Python script
   python assignments/assignment04-github.py
   
   # Jupyter notebooks
   jupyter notebook assignments/assignment03-cso.ipynb
   ```

## Assignments

- **assignment2-carddraw**: Card drawing operations — completed
- **assignment03-cso**: Working with CSO (Central Statistics Office) API
- **assignment04-github**: GitHub API interactions using PyGithub

## Labs

- **Lab 2:RepresentingData**: Data representation and manipulation
- **Lab 2:Trains**: XML/CSV train data processing
- **lab_4_api**: GitHub API exploration

## Requirements

- Python 3.8+
- Jupyter Notebook
- PyGithub
- Requests
- pandas

See `requirements.txt` for full dependencies.