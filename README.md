# jira-reports

Project to extract information and build reports from jira in pdf. 

It shall contain a main file called report.py and it is to be executed like this, you need **python version 3.4+**:

```
python reports.py <project-number>
```

A file named report_$HOURhMINUTESmin.pdf it is to be generated in $HOME/Documents/jira/reports/$year/$month/$day
If the folder does not exist it shall be created. For instance, on in 2020/11/21 at 14:37 the file shall be named report_14h37min.pdf

# Setup

1. Install and set the virtual enviroment

```
python -m venv env
source env/bin/activate
```

For more information on python virtual enviroments: https://realpython.com/python-virtual-environments-a-primer/

2. Install the packages required
   
```
pip install -r requirements.txt
```

3. Install wkhtmltopdf:

* Debian/Ubuntu:

```
sudo apt-get install wkhtmltopdf
```

* macOS:

```
brew install caskroom/cask/wkhtmltopdf
```

4. Create a file called .env in directory **home/$user**, set your jira credentials in it, like this:

```
WORKSPACE=https://myServer.myDomain.net/

EMAIL=myEmail@myDomain.com

TOKEN=42isTheNumberOfLife
```

# Args for each project

## 1. TI - Correlation between number of open issues vs priority
## 2. CLIEN - (in production)

# Report

The result expected is a pdf file containing:

- a bar plot of the number_of_open_issues vs priority
- a table containing every issue, its priority, how long since its creation and an indicator if the issue is within the time of resolution.

Table example:

| issue | priority | time | warn |
| ----- | -------- | ---- | ---- |
| issue-1 | medium | 100  | green |
| issue-3 | high   | 90   | red |
| issue-7 | highest | 10  | green |
| issue-11 | lowest | 123124 | green |

## Issues Resolution Time

- highest: 24 hours
- high: 72 hours
- medium: 120 hours
- low: no time for resolution
- lowest: it will not be solved
