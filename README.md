# ResumeAnalyzer
# Resume Analyzer Application

## Overview
This application analyzes resumes to extract key information such as name, email, skills, and education. It uses Python, Streamlit for the frontend, and a MySQL database for data storage.

## Setup Instructions

### Prerequisites
- Python 3.10 or 3.11
- MySQL Server (local or remote)
- XAMPP (for local Apache and MySQL server management)
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/jasminedorathy/resumeanalyzer.git
   cd resumeanalyzer
   ```

2. Create and activate a Python virtual environment:
   ```
   python -m venv myenv
   myenv\Scripts\activate   # Windows
   source myenv/bin/activate  # macOS/Linux
   ```

3. Install required Python packages:
   ```
   pip install -r App/requirements.txt
   ```

4. Ensure MySQL server is running:
   - If using XAMPP, start Apache and MySQL from the XAMPP Control Panel.
   - If ports 80 or 3306 are in use, change Apache port to 8080 and MySQL port to 3307 (see below).

### Changing Apache and MySQL Ports in XAMPP

- To change Apache port:
  - Open `xampp/apache/conf/httpd.conf`
  - Find the line `Listen 80` and change it to `Listen 8080`
  - Find the line `ServerName localhost:80` and change it to `ServerName localhost:8080`
  - Save and restart Apache.

- To change MySQL port:
  - Open `xampp/mysql/bin/my.ini`
  - Find the line `port=3306` and change it to `port=3307`
  - Save and restart MySQL.

### Running the Application Locally

1. Ensure your MySQL database is set up and accessible.
2. Update database connection settings in `App.py` if needed.
3. Run the Streamlit app:
   ```
   streamlit run App/App.py
   ```
4. Access the app in your browser at `http://[localhost:8501](http://localhost:8501/)`

## Deployment

- For deployment on Streamlit Cloud, use Python 3.10 or 3.11.
- Ensure `python-docx` is included in `requirements.txt`.
- Use a remote database instead of a local one, as Streamlit Cloud cannot access local databases.

## Troubleshooting

- If Apache or MySQL fail to start, check for port conflicts and change ports as described above.
- For database connection errors, verify MySQL server is running and credentials are correct.

## Contact

For further assistance, please contact [jasminedorathyvasantharaj@gmail.com].
