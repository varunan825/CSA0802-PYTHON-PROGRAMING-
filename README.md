# CSA08 Python Programming – Four Assignments (CO2–CO5)

**Student:** Varunan K  
**Registration Number:** 1924260055  
**Department:** B.Tech Artificial Intelligence and Data Science  
**Year:** First Year

This folder contains separate, runnable Python source files for the four uploaded assignment sets:
- `Assignment_CO2` – control flow, strings, functions and recursion (7 programs)
- `Assignment_CO3` – lists, tuples, dictionaries, sets and data structures (7 programs)
- `Assignment_CO4` – file processing, exceptions, modules and validation (5 programs)
- `Assignment_CO5` – data cleaning, SQLite, analysis, profiling and AI examples (5 programs)

## Requirements
- Python 3.10 or later recommended.
- CO2–CO4 use the Python standard library.
- CO5 also uses only the Python standard library (`csv`, `io`, `sqlite3`, `random`, `time`, `logging`, `cProfile`, `re`, etc.).
- No external packages are required.

Check your Python version:
```bash
python --version
```

## How to run
Open a terminal in this folder. Run any task using:
```bash
python Assignment_CO2/Task01_electricity_subsidy.py
python Assignment_CO3/Task01_rainfall_analysis.py
python Assignment_CO4/Task01_mess_bill_file_processing.py
python Assignment_CO5/Task01_clean_air_quality_data.py
```
Replace the path with the required assignment/task file. On some systems use `python3` instead of `python`.

## File organisation
Each task is a separate `.py` file. Programs that request input will prompt in the terminal. Other programs use the sample data shown in the uploaded answer PDFs.

## Important notes
1. The source PDFs sometimes contain formatting/indentation issues caused by document layout. The Python files here have been arranged with valid Python indentation so they can run.
2. The CO2 subsidy example uses an `if-elif-else` chain so a household receives one decision only. The registration-number validator removes spaces and hyphens and converts letters to uppercase before checking.
3. Timings from benchmark programs depend on your computer and Python version. Record your own results; do not copy a timing as a universal result.
4. Review each program and understand it before submission. Run every task yourself and capture your own output screenshots if required by your faculty.
5. The code is based on the uploaded CO2, CO3, CO4 and CO5 code/output PDFs. Where the uploaded output had malformed indentation, the indentation was corrected without changing the task's intended operation.

## Suggested GitHub repository
`CSA08-1924260055-Assignment2` (the uploaded CO2 assignment brief specifically requests this repository name; confirm with your faculty whether CO3–CO5 should be added to the same repository).

## Suggested commit workflow
```bash
git init
git add README.md requirements.txt Assignment_CO2 Assignment_CO3 Assignment_CO4 Assignment_CO5
git commit -m "Add Python assignment source files CO2 to CO5"
```
