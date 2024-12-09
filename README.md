# CSV to LaTeX Table Converter
[日本語版README](https://github.com/tatsuya-16/csv-to-latex-table/blob/main/README_JP.md)

## Overview

This Python script converts a CSV file into a formatted LaTeX table, making it easy to include tabular data in LaTeX documents. It provides flexibility in table formatting and handles special LaTeX character escaping.

## Features

- Converts CSV files to LaTeX table format
- Supports custom table captions and labels
- Allows flexible column formatting
- Escapes special characters like underscores
- Adds horizontal lines between rows

## Requirements

- Python 3.x
- `csv` module (standard library)
- `argparse` module (standard library)

## Usage

```bash
python csv_to_latex.py --input_file input.csv --output_file output.tex --caption "My Table Caption" --label "tab:mytable" --columns "|l|l|l|l|l|"
```

### Command-line Arguments

- `--input_file`: Path to the input CSV file (required)
- `--output_file`: Path to the output LaTeX file (required)
- `--caption`: Caption text for the LaTeX table (required)
- `--label`: Label for referencing the table in LaTeX document (required)
- `--columns`: Column formatting string (required)
  - Example: `"|l|l|l|l|l|"` creates a table with 5 left-aligned columns with vertical lines

## Example

### Input CSV (`data.csv`)
```
Name,Age,City,Country,Occupation
John,30,New York,USA,Engineer
Alice,25,London,UK,Designer
```

### Command
```bash
python csv_to_latex.py --input_file data.csv --output_file table.tex --caption "Sample Data" --label "tab:sample" --columns "|l|c|l|l|l|"
```

### Generated LaTeX Output (`table.tex`)
```latex
\begin{table}[ht]
    \centering
    \small
    \caption{Sample Data}
    \label{tab:sample}
    \begin{tabular}{|l|c|l|l|l|}
        \hline
        Name & Age & City & Country & Occupation \\
        \hline \hline
        John & 30 & New York & USA & Engineer \\
        \hline
        Alice & 25 & London & UK & Designer \\
        \hline
    \end{tabular} 
\end{table}
```

### Compiled Result
<img width="297" alt="スクリーンショット 2024-12-09 20 56 26" src="https://github.com/user-attachments/assets/4b22d1d3-01a0-4f7d-a0f9-dc5a2a951f68">

## Notes

- The script appends to the output file, so ensure the output file is empty or non-existent before running
- Underscores in data are automatically escaped to `\_` for proper LaTeX rendering
- The first row of the CSV is treated as a header row and has a double horizontal line
- Subsequent rows have a single horizontal line
