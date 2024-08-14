Gmail Email Retriever
=====================

This Python script connects to a Gmail account using the IMAP protocol, retrieves emails from a specified sender, and displays the sender's address, subject, date, and plain text content.

Features
--------

-   Connects securely to Gmail using IMAP and SSL.
-   Retrieves and displays emails from a specific sender.
-   Decodes and displays email subjects, even if they contain special characters.
-   Handles multipart emails, focusing on plain text content.

Prerequisites
-------------

-   **Python 3.x**
-   Required libraries: `imaplib`, `email`, `yagmail`

Installation
------------

1.  **Ensure Python 3.x is installed.**

2.  **Install the required libraries:**

    Since `imaplib` and `email` are part of Python's standard library, no need for installation. However, if you don't have `yagmail` installed, you can install it using pip:

    bash

    Copy code

    `pip install yagmail`

3.  **IMAP Access:** Ensure that IMAP access is enabled for your Gmail account.

Configuration
-------------

Replace the placeholder values in the script with your Gmail account details:

-   **EMAIL:** Your Gmail address
-   **PASSWORD:** Your Gmail password (Note: Store your password securely. Consider using environment variables or a password manager.)
-   **IMAP_SERVER:** The IMAP server address (`imap.gmail.com`)
-   **IMAP_PORT:** The IMAP port (`993` for SSL)

Usage
-----

1.  **Save the script** as a Python file (e.g., `email_retriever.py`).

2.  **Run the script** from your terminal:

    bash

    Copy code

    `python email_retriever.py`

    The script will print the sender, subject, date, and plain text content of each email from the specified sender.

Code Overview
-------------

The script connects to the Gmail server using IMAP, logs in with the provided credentials, and selects the inbox. It searches for emails from a specific sender, decodes the subject, and extracts the plain text content.

### Example Output


```From: devkarthik300@gmail.com
Subject: Test Email
Date: Wed, 13 Aug 2024 15:30:00 +0000
This is the plain text content of the email.
```

Security Considerations
-----------------------

-   **Password Management:** Avoid hardcoding your password directly in the script. Use environment variables or a password manager for better security.
-   **Sensitive Information:** Ensure your script does not expose sensitive information in public repositories.

Foot Notes
----------------

-   This script focuses on plain text content. You might need to modify the code to handle HTML content or attachments.
-   Consider implementing error handling to gracefully manage exceptions that might occur during the email retrieval process.

License
-------

This project is licensed under the MIT License. 
