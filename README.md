# Django Signals

## Overview
Django signals provide a way to notify certain parts of an application when actions occur elsewhere in the framework. This document answers key questions about the behavior of Django signals, specifically whether they run synchronously, in the same thread as the caller, and within the same database transaction.

## Question 1: Are Django Signals Synchronous or Asynchronous by Default?
Django signals are **synchronous by default**. When a signal is triggered, it executes immediately within the same request-response cycle. If the signal function takes a long time to execute, it can delay the response of the main application.

## Question 2: Do Django Signals Run in the Same Thread as the Caller?
Yes, Django signals **run in the same thread as the function that triggered them**. This means that signals do not create separate threads automatically.

## Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?
Yes, by default, Django signals execute **inside the same database transaction** as the caller. If an exception is raised in the signal, and it is triggered within a transaction (`transaction.atomic()`), the **entire transaction will roll back**.

### Handling Signals Asynchronously
To prevent Django signals from blocking execution, you can:
- Use **Celery** to run signals in a background task.
- Use **threading** or **multiprocessing** to execute signals in a separate thread.
- Use `transaction.on_commit()` to delay execution until the transaction is committed.
