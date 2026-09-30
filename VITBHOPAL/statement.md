# Project Statement

## Problem Statement
People who travel, study abroad, shop online or do business with other countries often need to know how much a foreign amount is worth in their own currency. Exchange rates change every day, so old rates from books or memory are not reliable. Many online converters are full of ads or are difficult to use. There is a need for a simple tool that gives the latest exchange rate quickly and remembers the previous conversions.

## Scope of the Project
- A console (command line) application written in Python.
- Converts money between 30 currencies using live rates from the Frankfurter API (European Central Bank data).
- Includes a currency list, a search option and a saved conversion history.
- Includes input validation, error handling, logging and unit tests.
- Out of scope: graphical interface, historical rate charts, offline rates, cryptocurrency.

## Target Users
- Students and travellers
- Online shoppers who buy from foreign websites
- Small business owners dealing with foreign clients
- Beginners who want to learn how a Python project uses an API

## High-Level Features
1. Convert an amount from one currency to another using the latest live rate.
2. Show the list of all supported currencies with names and symbols.
3. Search a currency by its name or code.
4. Save the conversion history in a file and show it later.
5. Clear the history.
6. Validate all inputs and handle network errors without crashing.
7. Write events and errors in a log file.
