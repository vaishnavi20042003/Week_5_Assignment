# Data Pipeline Project Repository
🛠️ Modular Data Engineering Solutions
Welcome to a collection of modular, plug-and-play Python solutions designed to simplify and automate common data engineering tasks—from database operations to format conversions and workflow automation.
Each folder in this repository encapsulates a dedicated, independent use case that you can run or adapt to fit your pipeline needs.

🗂️ What’s Inside

📦 Convert_Data/ — Export DB Tables to Multiple Formats
Extracts data from a MySQL database and outputs it in various formats:

CSV — Easily handled by spreadsheets and simple tools

Parquet — Ideal for analytics with optimized columnar storage

Avro — Great for data serialization and schema evolution

✅ Use Cases: Reporting, Big Data pipelines, warehousing, cross-platform interoperability



🔁 dbClone/ — Full Database Replication
Clones an entire MySQL database by dynamically replicating:

Table structures (DDL)

Data content (DML)

Ensures both schema and data are identical across environments.

✅ Use Cases: Backups, staging-to-prod sync, cross-environment migration



🎯 dbSelective/ — Targeted Table/Column Transfer
Move only what you need — this script allows you to specify:

Exact table names

Specific columns within each table

✅ Use Cases: Data minimization, privacy compliance, custom extracts for business logic



⏱️ Triggers/ — Automate Workflows with Triggers
Set up automation with:

Time-based triggers — Run tasks on fixed schedules

Event-based triggers — React to file arrivals or database updates in real time

✅ Use Cases: Scheduled backups, real-time data sync, notification systems



👥 customer.sql — Sample Schema for Demo Purposes
Includes SQL for creating and populating a basic People table used in multiple demos.

To use:

SOURCE customer.sql;
📌 Perfect for setting up a quick test or example run.



📌 How to Write, Test & Automate a Python Script with Cron
Want to automate your data workflow to run daily, send reports, or trigger alerts? Here's how to go from writing a script to scheduling it with cron.


✅ Step 1: Install Python & pip (if not already installed)
Check if Python and pip are installed:

python3 --version
pip3 --version
If not, install them:


sudo apt update
sudo apt install python3 python3-pip





✅ Step 2: Install Required Python Package
If your script connects to MySQL, install the connector:

pip3 install mysql-connector-python



✅ Step 3: Set Up Gmail App Password (for Email Automation)
⚠️ Never use your actual Gmail password in scripts.

Visit Google Account Security

Enable 2-Step Verification

Go to App Passwords

Choose:

App: Mail

Device: Other (Custom) → Name it e.g., cron-script

Generate and copy the 16-character password
You'll use this in your script to authenticate SMTP.



✅ Step 4: Create Your Python Script
Use a text editor like nano:

nano /home/your_username/db_report_email.py
Write your Python code to extract, format, and send data (e.g., as an email report).



✅ Step 5: Make Script Executable (Optional)
chmod +x /home/your_username/db_report_email.py



✅ Step 6: Test the Script Manually

python3 /home/your_username/db_report_email.py
Expected Output:

Email sent successfully!
If errors occur, they'll be printed in the terminal for debugging.




✅ Step 7: Automate with Cron (Schedule Script Execution)
Edit your crontab:


crontab -e
Add the following line to run the script every day at 9:00 AM:


0 9 * * * /usr/bin/python3 /home/your_username/db_report_email.py
Find your correct Python path using:


which python3
