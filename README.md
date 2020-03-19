# jira-reports

Project to extract information and build reports from jira in pdf. 

It shall contain a main file called report.py and it is to be executed like this:

```
python reports.py
```

A file named report-yyyy_mm_dd_hh.pdf it is to be generated in $HOME/Documents/jira/reports
If the folder does not exist it shall be created. For instance, on in 2020/11/21 at 14:37 the file shall be named report-2020_11_21_14.pdf

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
