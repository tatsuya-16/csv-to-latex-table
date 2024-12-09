# CSV to LaTeX tableコンバーター

## 概要

このPythonスクリプトは，CSVファイルをLaTeXテーブルに変換し，LaTeXドキュメントへのデータ挿入を容易にします．テーブルのフォーマットに柔軟性があり，特殊文字のエスケープも処理します．

## 特徴

- CSVファイルをLaTeXテーブル形式に変換
- カスタムテーブルのキャプションとラベルをサポート
- アンダースコアなどの特殊文字をエスケープ
- 行間に水平線を追加

## 必要条件

- Python 3.x
- `csv`モジュール（標準ライブラリ）
- `argparse`モジュール（標準ライブラリ）

## 使用方法

```bash
python csv_to_latex.py --input_file 入力.csv --output_file 出力.tex --caption "マイテーブルのキャプション" --label "tab:マイテーブル" --columns "|l|l|l|l|l|"
```

### コマンドライン引数

- `--input_file`: 入力CSVファイルのパス（必須）
- `--output_file`: 出力テキストファイルのパス（必須）
- `--caption`: LaTeXテーブルのキャプション文字（必須）
- `--label`: LaTeXドキュメント内で参照するためのラベル（必須）
- `--columns`: 列のフォーマット文字列（必須）
  - 例: `"|l|l|l|l|l|"` は5つの左揃えの列と縦線を持つテーブルを作成

## 例

### 入力CSV（`データ.csv`）
```
名前,年齢,都市,国,職業
太郎,30,東京,日本,エンジニア
花子,25,大阪,日本,デザイナー
```

### コマンド
```bash
python csv_to_latex.py --input_file データ.csv --output_file テーブル.tex --caption "サンプルデータ" --label "tab:サンプル" --columns "|l|c|l|l|l|"
```

### 生成されるLaTeXの出力（`テーブル.tex`）
```latex
\begin{table}[ht]
    \centering
    \small
    \caption{サンプルデータ}
    \label{tab:サンプル}
    \begin{tabular}{|l|c|l|l|l|}
        \hline
        名前 & 年齢 & 都市 & 国 & 職業 \\
        \hline \hline
        太郎 & 30 & 東京 & 日本 & エンジニア \\
        \hline
        花子 & 25 & 大阪 & 日本 & デザイナー \\
        \hline
    \end{tabular} 
\end{table}
```

### コンパイル結果
<img width="287" alt="スクリーンショット 2024-12-09 20 52 41" src="https://github.com/user-attachments/assets/9643b9fa-04fa-4e87-b08f-2b3f1f373fed">

## 注意点

- スクリプトは出力ファイルに追記するため，実行前に出力ファイルが空またはない状態であることを確認してください
- データ内のアンダースコアは自動的に `\_` にエスケープされ，適切なLaTeXレンダリングを行います
- CSVの最初の行はヘッダー行として扱われ，二重の水平線が追加されます
- 2行目以降は行ごとに水平線が追加されます
