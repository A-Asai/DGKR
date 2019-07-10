# CalMorph Galaxy

## これはどんなレポジトリ？
- Galaxyに実装するためのスクリプトを基本的に置いてあります。

## 背景
- 再現性の危機(reproduciblity crisis)は計算科学の分野においても、解析環境の違いから起こっている。
- しかしながら、解析における再現性は(解析内容にランダム性がある場合を除き)、解析環境を一致させることで保つことができる。
- ただ、この解析環境を同一にすることにはある程度のコンピューターリテラシーが求められ、バイオ分野においてはこのリテラシーに達している人材は他分野に比べて少ない。
- 本研究では、この解析環境を同一にすることのハードルを下げ、誰でも簡単に目的の解析環境を持つことができるようなモデルを構築し、提案する。
- メモ
	- 解析を行いたくても研究室に機材がないためデータが取れない
	- 安価な解析システムを構築する
	- ただ、これは重い解析ができない気がする。
	- 比較的簡易な解析であれば研究室内で行えるようにする。
	- 解析の再現性をどう数値化するか。
	- メモ部分の根拠(論文)を探す。
	- 研究に関する秘匿性とのバランスも考慮して、開発したツールを公開しない方法を用いる(勿論再現性という点においては解析はオープンにすべきである)。

## ソフトウェア、ハードウェア類の簡単な説明
### Galaxy
- 主にゲノム解析分野で用いられているオープンソース解析プラットフォーム。公共Galaxyと呼ばれるものはカスタムすることはできないがURLを入力すれば使用できる。
- 本研究で用いるDocker Galaxyはカスタム(ツールの追加や見た目の変更など)がしやすく、拡張性が高い。
- Docker Galaxyは仕組みを理解すればゲノム解析に限らず、ありとあらゆるプログラムをGUIで動かせ、ワークフローに組み込むことができる。
- 利点に関しては今度どこかに書きます。ググってください。
### Docker
- 非常に雑に言うと、PCの中に仮想PCを立てるソフトウェア。
- 「コンテナ」という概念を用いる。
- これまでの「仮想PC」異なり、1アプリケーションごとにコンテナという仮想環境を用意するため、非常に軽量である。
### Kubernetes
- 勉強中
- 複数のDockerコンテナを複数のPCで一体となって動かす？ソフトウェア。
- クラスター技術に関連する。
- 以下に記載するラズパイにて、クラスターを構成する際に使用する予定。
### Raspberry Pi
- 勉強中
- シングルボードコンピューター
- 非常に安価で、小型であり、省電力である。
- スペックは微妙であるが、複数のラズパイを1つのPCとして動かせば(クラスター化すれば)必要なスペックは満たされると考えられる。
- 使用したいラズパイはおそらく日本では8月以降発売されるであろう(Raspberry Pi 4 (RAM4GB))で台数は4台以上。値段としては1台あたりおそらく8000~9000円台。
### GitHub
- 勉強中?
- 簡単に説明するのが今の理解力では難しいのでググってほしい。
- 本研究では、使用するデータや、開発したスクリプトなどを全てまとめるために使用している。
- また、Docker Hub用にも使用する予定(Docker fileをここから持ってくるようにする)。

## 必要なもの
- 解析環境を同一にすることをより簡単にするためにDocker(Docker Compose)を用いる。
- 解析を簡単にするためにGalaxyを用いる。
- メモ(必要によって追加)
	- 安価に解析システムを構築するためにRaspberry Piを用いる。
	- クラスター化のためにKubernetesを用いる。
	- 言語レベルから再現性を高めるためにCWLを用いる。

## 目標
- DockerをインストールしたPC上で1行コマンドを実行するだけで、解析環境が構築されるようにする。
- 解析自体もGUIでかつクリック数回で完了するようにする。
- R言語の追加

## 手法(暫定)
- Dockerのインストール
- Galaxyのインストール
- Docker Galaxy コンテナ内にてRのインストール
- 解析スクリプトをRやPythonで開発、対応するXMLファイルもそれぞれ開発
- Galaxyのconfigを修正
- ワークフローの作成
- ワークフロー、各ツール、Rが入ったGalaxy解析環境(Docker image)を作成する
- Raspberry Pi クラスタの構築
- クラスターに作成したDocker imageをインストール
- 再現性の検証

## 具体的にやること(暫定)

## 進捗やメモ
### 190521
- Dockerのインストール
- Galaxyコンテナ(bgruening/galaxy-stable)のインストール
### 190624
- Galaxyコンテナ内でのRのインストール
### 190626
- Galaxy上で実際にRのツールが機能するのかを検証するために、Rを用いたHelloWorldツール(helloworld_r.R)と対応するXMLファイル(helloworld_r.xml)を作成し、Galaxy内で実行した。
- XMLファイルの作成に苦戦したが、正常に動作した。
### 190628
- 本研究用のプライベートレポジトリをGithub上で作成。
### 190701
- README.md(このページ)の内容を書き始めた。
### 190702
- ツールを開発する上での基本的なルールとして **ワークフローを複数用意しないといけないような仕様のものは作らない** のが大事である。
### 190703
- config/tool_conf.xml 内を変更して、cutとcatツールをGalaxy上で表示されるようにした。
	- hiddenをfalseにするだけ。
- cutを使用してみた結果、以下の問題点が浮かび上がってきた
	- 指定された列だけが残る仕様になっている。
	- XMLかPerlのファイルをいじる必要がある。
- GitHubにデータを移行した。
### 190704
- GitHubのこのページにそろそろ画像を挿入して分かりやすくしていきたい。
### 190710
- 元々プライベートレポジトリだった本内容を少し編集してこちらに移動した。
