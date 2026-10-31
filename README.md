# QA Automation Demo

UI aur API test automation framework.

## Tech Stack
Python, Selenium, Pytest, Requests, GitHub Actions

## Features
- Page Object Model
- Data-driven tests (parametrize)
- UI tests: login, checkout (saucedemo.com)
- API tests (jsonplaceholder)
- HTML report
- CI pipeline

## Setup
pip install -r requirements.txt

## Run
pytest -v --html=report.html --self-contained-html

## Structure
conftest.py, pages/ (page objects), tests/ (test cases)