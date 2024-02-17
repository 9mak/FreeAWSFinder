
# FreeAWSFinder

FreeAWSFinderは、AWSの無料枠リソースを一覧化するためのスクリプトです。

## 機能

- [AWS 無料利用枠](https://aws.amazon.com/jp/free/)からAWSの無料利用枠の情報を取得します。
- Pythonと同じディレクトリに取得した情報を一覧化した`aws_services.txt`を作成します。

## 前提条件

FreeAWSFinderを使用する前に、Python 3.6以上がインストールされている必要があります。また、`requirements.txt`にリストされたパッケージをインストールする必要があります。

## インストール方法

まず、FreeAWSFinderをGitHubからクローンします：

```bash
git clone https://github.com/9mak/FreeAWSFinder.git
cd FreeAWSFinder
```

次に、必要なパッケージをインストールします：

```bash
pip install -r requirements.txt
```

## 使い方

スクリプトを実行してAWSの無料枠リソースを探索します：

```bash
python free_aws_finder.py
```

## 貢献

FreeAWSFinderはオープンソースプロジェクトであり、貢献を歓迎します。バグ報告や機能提案、プルリクエストなどはGitHubの[issues](https://github.com/9mak/FreeAWSFinder/issues)または[pull requests](https://github.com/9mak/FreeAWSFinder/pulls)にてお願いします。

## ライセンス

FreeAWSFinderは[MITライセンス](LICENSE)の下で公開されています。
