import csv
import argparse

# コマンドライン引数のパーサーを作成
parser = argparse.ArgumentParser(description='CSV to LaTeX converter')
parser.add_argument('--input_file', type=str, required=True, help='Input CSV file')
parser.add_argument('--output_file', type=str, required=True, help='Output LaTeX file')
parser.add_argument('--caption', type=str, required=True, help='Caption for the LaTeX table')
parser.add_argument('--label', type=str, required=True, help='Label for the LaTeX table')
parser.add_argument('--columns', type=str, required=True, help='Column format for the LaTeX table (e.g., "|l|l|l|l|l|")')

args = parser.parse_args()

# 入力csvファイル
input_file = args.input_file

# 出力txtファイル
output_file = args.output_file

# 先頭のLaTeXコード
latex_code_start = rf"""
\begin{{table}}[ht]
    \centering
    \small
    \caption{{{args.caption}}}
    \label{{{args.label}}}
    \begin{{tabular}}{{{args.columns}}}
        \hline
"""

# 末尾のLaTeXコード
latex_code_end = r"""
    \end{tabular} 
\end{table}
"""

# 先頭のLaTeXコードをテキストファイルに書き込む
with open(output_file, 'a', encoding='utf-8') as outfile:
    outfile.write(latex_code_start)

# CSVファイルを処理
with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, quotechar='"', skipinitialspace=True)
    with open(output_file, 'a', encoding='utf-8') as outfile:
        for i, row in enumerate(reader):
            # データの文字列内に"_"がある場合は，"\_"とする
            escaped_row = [cell.replace('_', r'\_') for cell in row]
            # データの間に"&"を挿入し、末尾に"\\"
            formatted_row = " & ".join(escaped_row) + " \\\\"
            outfile.write("        " + formatted_row + "\n")
            if i == 0:
                outfile.write("        \hline \hline" + "\n")
            else:
                outfile.write("        \hline" + "\n")

# 末尾のLaTeXコードをテキストファイルに書き込む
with open(output_file, 'a', encoding='utf-8') as outfile:
    outfile.write(latex_code_end)

print("Processing complete.")
