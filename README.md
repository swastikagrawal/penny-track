# Penny Track

A simple desktop application to track your daily expenses, built with Python and SQLite.

## Features

- Log daily expenses with category, amount, date and note
- Filter expenses by Today, This Week, This Month, This Year or All Time
- View total expenses for any time period
- Delete any transaction
- 16 pre-built expense categories

## Tech Stack

- Python
- CustomTkinter
- SQLite
- Pillow

## Download

Download the latest version: [PennyTrack.exe](https://github.com/swastikagrawal/penny-track/releases/download/v1.0.0/PennyTrack.exe)

## How to Run

1. Clone the repository
2. Create a virtual environment
```
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies
```
   pip install -r requirements.txt
```
4. Run the app
```
   python main.py
```

## Database

Two tables:
- `categories` — stores expense categories
- `transactions` — stores all expense entries

## Author

[Swastik Agrawal](https://github.com/swastikagrawal)
