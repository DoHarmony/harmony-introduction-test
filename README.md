# Harmony — Engineering Candidate Test

Welcome to the Harmony technical test. This repository contains three independent exercises designed to evaluate your ability to read existing code critically, identify design and performance problems, propose clean scalable solutions, and write reliable automated tests.

---

## How to approach this test

- Read the provided code carefully **before** writing anything.
- Identify problems first, then solve them.
- Apply **object-oriented programming**, **clean code principles**, and a **simple but scalable architecture**.
- All code must be Python 3.10+.
- You are free to add new files, classes, or modules — but do not delete or rename existing interfaces.
- Commit your changes with clear, descriptive messages.
- You may use any tools you find useful: Cursor, AI agents, code assistants, linters, anything. There are no restrictions on tooling. What matters is the quality of the final solution and **your own engineering judgment** behind every decision you make.

---

## Project structure

```
harmony-introduction-test/
├── README.md                          ← you are here
├── requirements.txt
│
├── whatsapp_integration/              ← Exercise 1
│   ├── __init__.py
│   ├── interfaces.py                  ← contracts (do not modify)
│   ├── models.py                      ← data models (do not modify)
│   ├── exceptions.py
│   └── whatsapp_service.py            ← the code under review
│
├── sql_optimization/                  ← Exercise 2
│   ├── __init__.py
│   ├── models.py                      ← pseudo schema documentation
│   └── queries.py                     ← the queries under review
│
└── tests/                             ← Exercise 3 (yours to fill)
```

---

## Exercise 1 — WhatsApp Integration Scalability Review

### Context

The file `whatsapp_integration/whatsapp_service.py` contains a implementation of a WhatsApp Business API integration. The code is functional and follows the interfaces defined in `interfaces.py`, but it has several serious problems.

### Your task

1. **Read** `whatsapp_service.py` thoroughly.
2. **Write** an audit about problems and about how you will fix all of them.
2. **Identify** every design problem. Write a short explanation for each issue directly in code comments or in a separate `REVIEW.md` file inside `whatsapp_integration/`.
3. **Refactor** `whatsapp_service.py` (or create a new `whatsapp_service_v2.py` alongside it) with a corrected, production-ready implementation.

## Exercise 2 — SQL Query Optimization

### Context

The file `sql_optimization/queries.py` contains five Python functions, each executing a SQL query against the pseudo schema described in `sql_optimization/models.py`. All five queries return correct results on small datasets but are **poorly optimised** and will degrade badly at scale.

No real database connection is required. Treat the queries as plain SQL strings and focus entirely on their structure and efficiency.

### Your task

For **each of the five queries**:

1. **Identify** all performance problems in the query (and in the surrounding Python code where applicable).
2. **Rewrite** the query so it is efficient and production-ready.
3. **Explain** briefly why each change improves performance (in a comment above the rewritten query or in a `REVIEW.md` inside `sql_optimization/`).

You may also propose new indexes that would support your optimised queries. List them at the bottom of your review.

### Schema reference

```
users        (id, email, name, status, created_at)
orders       (id, user_id, total, status, created_at)
order_items  (id, order_id, product_id, quantity, unit_price)
products     (id, name, description, category_id, price, stock)
categories   (id, name, parent_id)
```

Current indexes: **primary keys only**.

## Exercise 3 — Unit Testing the WhatsApp Integration

### Context

The `whatsapp_integration/` module now has a working implementation — whether the original one, your refactored version, or both. Either way, code without tests is incomplete.

### Your task

Write a complete unit test suite for the WhatsApp integration inside the `tests/` directory.

That is all the information you will receive for this exercise.

---

## Delivery

- Fork or clone this repository and push your solution to a branch named after yourself: `firstname_lastname` (e.g. `sebastian_torres`).
- Open a Pull Request against `main` with a short description of your changes.
- There is no hard time limit, but we expect a focused, quality solution over an exhaustive one.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

Good luck! We look forward to reading your solution.
