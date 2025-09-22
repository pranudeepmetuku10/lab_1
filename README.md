# Lab 1 – MLOps (IE-7374)

This lab focused on setting up the basics of an MLOps workflow. The main tasks were creating a virtual environment, organizing a GitHub repository, writing a simple calculator module, testing it with both `pytest` and `unittest`, and finally automating everything with GitHub Actions.  

The idea was to not just follow instructions mechanically but to also make some modifications so the work reflects my own approach.

---

## Project Structure

lab_1/
│── data/              # placeholder for datasets
│── src/               # source code
│   └── calculator.py
│── test/              # test cases
│   ├── test_pytest.py
│   └── test_unittest.py
│── .github/workflows/ # GitHub Actions workflows
│   ├── pytest_action.yml
│   └── unittest_action.yml
│── README.md
│── .gitignore


---

## What I Changed

To make the project more than just a copy of the starter, I added and adjusted several pieces:

- **Calculator module**  
  - Added `fun5` for division with error handling (raises `ZeroDivisionError` for division by zero).  
  - Added `fun6` for exponentiation.  
  - Added input validation to raise a `TypeError` when non-numeric inputs are provided.  

- **Tests**  
  - Expanded `pytest` tests with parameterized cases to check multiple inputs in a single test.  
  - Added tests for exceptions, including division by zero and invalid input types.  
  - Extended `unittest` with additional tests for `fun5` and `fun6`.  

- **GitHub Actions**  
  - Fixed the import path issue by setting `PYTHONPATH=.` so the `src` folder is visible.  
  - Adjusted pytest to use verbose mode and stop after the first failure for cleaner logs.  
  - Limited unittest to only run the project’s own tests rather than the entire Python environment.  

---

## Results

- **Local runs**  
  - Pytest: all tests passed.  
  - Unittest: 6 tests passed, 1 test failed (`fun4`).  

- **GitHub Actions**  
  - Pytest workflow ran successfully after fixing the path issue.  
  - Unittest workflow produced the same single failing test, as expected.  

---

## About the Failing Test

One of the unittest cases, `test_fun4`, attempts to call `fun4(x, y, z)` with three arguments. My current implementation of `fun4` only takes two arguments. This mismatch raises a `TypeError`: fun4() takes 2 positional arguments but 3 were given

I intentionally left this mismatch in place. The point was to demonstrate how a failing test shows up in continuous integration logs. In a real-world scenario, this is exactly the kind of issue CI/CD is designed to surface.  

---

## Takeaways

Working through this lab gave me practical experience with:  
- Setting up isolated Python environments with `venv`.  
- Organizing a project and repository structure clearly.  
- Writing tests with both `pytest` and `unittest`.  
- Automating tests in GitHub Actions.  
- Understanding how failing tests are reported and how they guide debugging.  

This process reinforced the value of automation in development and gave me a clearer sense of how CI/CD fits into everyday workflows.
