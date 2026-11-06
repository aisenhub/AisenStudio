<div align="center">

# AisenStudio 💸

### オールインワン AI ショート動画生成ツール

動画の<b>テーマ</b>または<b>キーワード</b>を指定するだけで、MoneyPrinterTurbo が台本の生成、素材のマッチング、字幕と BGM の作成を行い、高画質のショート動画を出力します。

[![Version](https://img.shields.io/github/v/release/aisenhub/AisenStudio?color=blue&label=version)](https://github.com/aisenhub/AisenStudio/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/aisenhub/AisenStudio/releases/latest)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Downloads](https://img.shields.io/github/downloads/aisenhub/AisenStudio/total)](https://github.com/aisenhub/AisenStudio/releases/latest)

<a href="https://www.star-history.com/aisenhub/AisenStudio"><img src="https://api.star-history.com/badge?repo=aisenhub/AisenStudio" alt="Star History Rank" style="height: 55px;" height="55"/></a>

日本語 | [English](README-en.md) | [简体中文](README.md) | [リリース](https://github.com/aisenhub/AisenStudio/releases) | [Issues](https://github.com/aisenhub/AisenStudio/issues)

</div>

## スクリーンショット 🖥️

<h4 align="center">WebUI</h4>

![](docs/webui-en.jpg)

<h4 align="center">API</h4>

![](docs/api.jpg)

---

## 機能 🎯

### 制作フロー

- [x] **AI エージェント、WebUI、API、CLI** の 4 つの利用方法を提供し、手軽な動画制作から自動化ワークフローへの組み込みまで対応
- [x] テーマから台本、ナレーション、素材、字幕、BGM、編集までを自動化し、各工程で独自コンテンツを使用することも可能
- [x] **複数動画の一括生成**、タスク履歴、生成設定と API キーのインポート・エクスポート・復元に対応

### 台本とモデルプロバイダー

- [x] AI による**多言語動画台本**の生成・リライトに加え、独自台本の利用にも対応
- [x] [Kimi / Moonshot AI](https://platform.kimi.ai)、[OpenAI](https://platform.openai.com/api-keys)、[Anthropic Claude](https://platform.claude.com/settings/keys)、[Google Gemini](https://aistudio.google.com/app/apikey)、[DeepSeek](https://platform.deepseek.com/api_keys)、[Alibaba Cloud Qwen](https://qwen.ai/apiplatform)、[Microsoft Azure OpenAI](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/OpenAI)、[ByteDance VolcEngine Ark](https://console.volcengine.com/ark)、[xAI Grok](https://console.x.ai/)、[MiniMax](https://platform.minimax.io/)、[Xiaomi MiMo](https://platform.xiaomimimo.com/docs/zh-CN/quick-start/first-api-call) などの主要なモデルサービスに対応
- [x] [Shengsuan Cloud](https://www.shengsuanyun.com)、[APIMart](https://apimart.ai)、[Cloudflare AI Gateway](https://dash.cloudflare.com/)、[Alibaba ModelScope](https://modelscope.cn/docs/model-service/API-Inference/intro)、[AIHubMix](https://aihubmix.com/)、[AIML API](https://aimlapi.com/app/keys)、[EvoLink](https://evolink.ai/dashboard/keys)、[OpenRouter](https://openrouter.ai/settings/keys)、[API Route](https://www.api-route.com/)、[Ollama](https://ollama.com/)、[Claude Code サブスクリプション](https://code.claude.com/docs)、[OneAPI](https://github.com/songquanpeng/one-api)、[LiteLLM](https://docs.litellm.ai/docs/providers)、[Groq](https://console.groq.com/keys)、[Pollinations AI](https://enter.pollinations.ai/) などの統合ゲートウェイ、集約サービス、ローカルランタイムに対応

### 動画・画像素材

- [x] 手持ちの**ローカル画像・動画**をアップロードできるほか、[Pexels（無料）](https://www.pexels.com/api/)、[Pixabay（無料）](https://pixabay.com/api/docs/)、[Coverr](https://coverr.co/developers?ctx=header_navigation) の高画質ストック素材を利用可能
- [x] [Metaso MiniMax H3](https://metaso.cn) によるテキスト動画生成に対応し、`768P`／`2K`、4～15 秒の素材を `9:16`、`16:9`、`1:1` の 3 種類のアスペクト比で生成可能
- [x] [Shengsuan Cloud AI Video](https://www.shengsuanyun.com) で複数の AI 動画素材を生成し、プロジェクトのナレーション、字幕、編集フローで 1 本の動画に合成可能
- [x] [Volcano Engine Ark Seedance](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey) をネイティブに統合し、台本の各セグメントから一貫した動画素材を生成可能
- [x] [WaveSpeed AI](https://wavespeed.ai) によるテキスト動画生成で、台本のキーワードからオリジナル素材を作成可能
- [x] [OFox](https://ofox.ai) のマルチモデルテキスト動画生成に対応し、1 つの API キーで Seedance、Wan などのモデルを利用可能
- [x] 非同期の [MuAPI](https://muapi.ai) テキスト動画 API で 3～12 秒の AI 素材を生成し、Endpoint、アスペクト比、解像度、ポーリングを設定可能
- [x] [OpenAI 互換の画像生成](https://platform.openai.com/docs/guides/image-generation)サービスや独自の画像ゲートウェイを接続し、生成画像を動きのある動画クリップに変換可能
- [x] クリップの長さ、フレームへの合わせ方、素材の使用順を調整し、アスペクト比や構成に合わせた編集が可能

### ナレーション・字幕・BGM

- [x] 自動ナレーション、音声ファイルのアップロード、音声なしの 3 つの方式に対応し、音声サンプルとナレーション全体をプレビュー可能
- [x] **Edge TTS（無料・API キー不要）**、Azure Speech、SiliconFlow、Google Gemini、Xiaomi MiMo、MiniMax、ElevenLabs、Chatterbox、Kokoro、Fish Audio、ModelBest VoxCPM などの音声サービスに対応
- [x] 字幕を自動生成し、フォント、位置、色、サイズ、縁取り、背景スタイルを調整可能
- [x] ランダム、ローカル、AI 生成の BGM に対応し、音量を個別に調整可能

### 出力と公開

- [x] 縦型 `9:16（1080×1920）`、横型 `16:9（1920×1080）`、正方形 `1:1（1080×1080）` に対応
- [x] 動画生成後、**TikTok、Instagram、YouTube Shorts** へワンクリックで自動公開可能

## 動作環境 📦

- 推奨プラットフォーム: Windows 10 以降、macOS 11 以降、または主要な Linux ディストリビューション
- ローカル環境へのデプロイには Python 3.11 以降が必要です。Python 3.11 を推奨します
- GPU は必須ではありませんが、ローカルでの文字起こしや動画処理を高速化したい場合、一括生成をより快適に行いたい場合には推奨されます

| 項目   | 最低   | 推奨           | 最適           |
| ------ | ------ | -------------- | -------------- |
| CPU    | 4 コア | 6〜8 コア      | 8 コア以上     |
| メモリ | 4 GB   | 8 GB           | 16 GB 以上     |
| GPU    | 不要   | VRAM 4 GB 以上 | VRAM 8 GB 以上 |

- 主にクラウド LLM、クラウド TTS、オンライン素材ソースを利用する場合は、GPU よりも CPU とメモリのほうが重要です
- `faster-whisper`、一括生成、負荷の高いローカル処理を利用する場合は、GPU によってスループットが目に見えて向上します

## クイックスタート 🚀

### おすすめの手順

- 手動でのインストールや設定をしたくない場合: AI エージェントで動画を生成する
- Python がインストール済みで、すぐに使いたい場合: [pip で公式パッケージをインストール](#pip-で公式パッケージをインストール)
- Windows ユーザー: まずはワンクリックパッケージを使うのが最短で試せます
- ソースコードからのデプロイや開発: `uv` で環境と依存関係を管理します
- より独立した実行環境が欲しい場合: Docker でデプロイします

### AI エージェントで動画を生成する

お使いの AI エージェントが Skill ドキュメントを読み、ローカルのターミナルを操作できるなら、以下のプロンプトを送ってください。エージェントが MoneyPrinterTurbo のインストールと設定を行い、動画を生成して、動画ファイルのパスを返します。未設定の必須 API キーだけを尋ねてきます。このワークフローは現在 macOS と Windows に対応しています。

```text
Use this Skill: https://raw.githubusercontent.com/aisenhub/AisenStudio/main/docs/skill/SKILL.md
Create a video with the topic "How AI is changing everyday life."
```

### Google Colab で実行する

ローカル環境を用意せずに MoneyPrinterTurbo を試したいですか？ Google Colab で直接実行できます！

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aisenhub/AisenStudio/blob/main/docs/MoneyPrinterTurbo.ipynb)

### Windows

GitHub Releases から最新の Windows 用ワンクリックパッケージをダウンロードし、そのまま展開してください。

- [最新の Windows 用ワンクリックパッケージをダウンロード](https://github.com/aisenhub/AisenStudio/releases/latest)

> 同ページの **Assets** から `.7z` ファイルをダウンロードしてください。GitHub が
> 自動生成する `Source code (zip)` / `Source code (tar.gz)` はソースコードのみで、
> 展開しても `webui.bat` だけが現れ、`start.bat` と `update.bat` は含まれません。

ダウンロード後は、まず `update.bat` を**ダブルクリック**して**最新のコード**に更新し、その後 `start.bat` をダブルクリックして起動することを推奨します

起動するとブラウザーが自動的に開きます（真っ白な画面になる場合は **Chrome** または **Edge** の利用を推奨します）

### macOS / Linux

以下のローカルセットアップまたは Docker の手順を参照してください。

## インストールとデプロイ 📥

### pip で公式パッケージをインストール

公式の PyPI パッケージ名は **[mpt](https://pypi.org/project/mpt/)** で、`harry0703` が管理しています。
PyPI 上の `MoneyPrinterTurbo` という名前のパッケージは第三者が管理しています。

リポジトリのクローンは不要です。Python 3.11 以降が必要で、Python 3.11 を推奨します。

**① 仮想環境を作成して有効化する**

macOS / Linux:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**② インストールして起動する**

```shell
python -m pip install mpt
mpt webui
```

WebUI がブラウザーで自動的に開きます。
ポートを指定し、ブラウザーを開かずに実行する場合は `mpt webui --port 8503 --headless` を使用してください。
CLI での動画生成については `mpt cli --help` を参照してください。

**③ サービスを設定し、保存先を確認する**

初回起動時に `config.toml` が自動作成されます。
オンラインのモデル、素材、音声サービスを利用する前に、WebUI の基本設定で必要な API キーを入力してください。
インストール版の設定と生成ファイルは、既定では以下の場所に保存されます:

| OS | データディレクトリ |
| --- | --- |
| macOS | `~/Library/Application Support/MoneyPrinterTurbo` |
| Windows | `%LOCALAPPDATA%\MoneyPrinterTurbo` |
| Linux | `~/.local/share/MoneyPrinterTurbo` または `$XDG_DATA_HOME/MoneyPrinterTurbo` |

起動前に `MPT_HOME` を設定すると、保存先を変更できます。
生成された動画は、そのディレクトリ内の `storage/tasks` に保存されます。
更新するには仮想環境を有効化して `python -m pip install --upgrade mpt` を実行してください。

### ソースコードからデプロイする場合の前提条件

- ローカル環境へのデプロイには Python 3.11 以降が必要です
- Windows では、プロジェクトのパスに非 ASCII 文字、特殊文字、スペースを含めないでください

#### ① プロジェクトをクローンする

```shell
git clone https://github.com/aisenhub/AisenStudio.git
```

#### ② 初期設定を行う

初回起動時に `config.example.toml` から `config.toml` が自動作成されるため、設定ファイルを手動で作成する必要はありません。クラウド LLM、オンライン素材、AI 動画などのサービスを利用する前に、WebUI の基本設定で対応する API キーを入力してください。

### Docker でデプロイ 🐳

#### ① Docker コンテナを起動する

Docker が未インストールの場合は、先に [Docker Desktop をダウンロードしてインストール](https://www.docker.com/products/docker-desktop/)してください。
Windows をお使いの場合は、Microsoft のドキュメントを参照してください:

1. [WSL をインストールする](https://learn.microsoft.com/en-us/windows/wsl/install)
2. [WSL で Docker コンテナを使用する](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)

```shell
cd AisenStudio
docker compose -f docker-compose.release.yml up
```

> 既定では `docker-compose.release.yml` を推奨します。GitHub Container Registry からビルド済みイメージ `ghcr.io/aisenhub/AisenStudio:latest` を取得します。
> ローカルでイメージをビルドする必要がある場合は、これまでどおり `docker compose up` を実行できます。
> 初回起動の前に、`config.example.toml` を `config.toml` にコピーしておくと、コンテナにマウントされます。

#### ② WebUI にアクセスする

ブラウザーで http://127.0.0.1:8501 を開きます

#### ③ API ドキュメントにアクセスする

ブラウザーで http://127.0.0.1:8080/docs または http://127.0.0.1:8080/redoc を開きます

> API はデフォルトで同一オリジンのブラウザーアクセスのみを許可します。別のブラウザーフロントエンドから API を直接呼び出す場合に限り、環境変数 `CORS_ALLOWED_ORIGINS` へ信頼するオリジンを設定してください（例: `http://localhost:3000,https://frontend.example.com`）。curl、Postman、n8n、その他のサーバー側クライアントは CORS の影響を受けません。

### 手動でデプロイ 📦

#### ① Python の仮想環境を作成する

[uv](https://docs.astral.sh/uv/) を使って Python 環境と依存関係を管理します。本プロジェクトは Python 3.11 以降に対応しており、以下の例では Python 3.11 を使用します。

```shell
git clone https://github.com/aisenhub/AisenStudio.git
cd AisenStudio
uv python install 3.11
uv sync --frozen
```

`uv` をまだ使っていない場合は、これまでどおり `venv + pip` も利用できます。

```shell
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

補足:

- 現在は `pyproject.toml` が主要な依存関係の定義ファイルです。
- `uv.lock` が解決済みの環境を固定するため、既定では `uv sync --frozen` を推奨します。
- `requirements.txt` は従来の `pip` によるインストールのためだけに残されています。

#### ② WebUI を起動する 🌐

以下のコマンドは MoneyPrinterTurbo プロジェクトの`ルートディレクトリ`で実行する必要がある点に注意してください

###### Windows

```powershell
.\webui.bat
```

`webui.bat` は CMD から実行することもできます。
`webui.bat` は、プロジェクトの `.venv` またはポータブルパッケージに同梱された Python を優先して使用します。プロジェクトの Python が見つからず、`uv` がインストールされている場合は、自動的に `uv run streamlit` にフォールバックします。
同じ LAN 内の別の端末から WebUI にアクセスできるようにするには、`webui.bat` を実行する前に `set MPT_WEBUI_HOST=0.0.0.0` を実行してください。

###### macOS または Linux

```shell
sh webui.sh
```

このスクリプトは、プロジェクトの仮想環境または `uv` を自動的に使用し、利用可能なローカルポートを選択します。同じ LAN 内の別の端末からアクセスできるようにするには、次のように実行します:

```shell
MPT_WEBUI_HOST=0.0.0.0 sh webui.sh
```

起動するとブラウザーが自動的に開きます

#### ③ API サービスを起動する 🚀

```shell
uv run python main.py
```

仮想環境を手動で有効化済みの場合は、これまでどおり次のように実行できます:

```shell
python main.py
```

#### ④ CLI のみのモード（ブラウザー不要） ⌨️

ブラウザーやポートフォワーディングが利用できない場合は、コマンドラインから直接動画を生成できます。最もシンプルな生成コマンドは次のとおりです:

```shell
uv run python cli.py --video-subject "How AI is changing everyday life"
```

コマンドの完全なリファレンス、パラメーターの説明、使い方については、次を実行してください:

```shell
uv run python cli.py --help
```

複数のタスクを順番に実行するには、`--batch-file` で UTF-8 の JSON 配列または
JSONL マニフェストを指定します。CLI オプションが共通の既定値となり、各オブジェクトで
`VideoParams` フィールドを上書きできます。

```shell
uv run python cli.py --batch-file ./tasks.json --stop-at video
```

マニフェストは最大 100 タスク、1 MiB までです。最初のタスクを開始する前に全項目と
ローカルファイルを検証し、個別タスクが失敗しても後続タスクを続行して最後に JSON
サマリーを出力します。マニフェスト内の相対音声・ローカル素材パスはマニフェストの
ディレクトリを基準に解決されます。

## ナレーション・字幕・BGM 🎙️

### 音声合成

WebUI の **Azure TTS V1** は **Edge TTS** を利用しており、無料かつ API キー不要です。MoneyPrinterTurbo は **Azure TTS V2**、**SiliconFlow TTS**、**Google Gemini TTS**、**Xiaomi MiMo TTS**、**ElevenLabs TTS**、セルフホストの **Chatterbox TTS**、セルフホストの **Kokoro TTS**、**Fish Audio TTS**、および音声なしモードにも対応しています。

WebUI でプロバイダーと音声を選択し、必要な認証情報については画面の案内に従ってください。Edge TTS に API キーは不要です。[Azure TTS V2](https://portal.azure.com/) やその他のクラウドプロバイダーでは、それぞれのプラットフォームで発行した認証情報が必要です。利用可能な Edge TTS の音声は[音声リスト](./docs/voice-list.txt)で確認できます。

### 字幕生成

字幕の生成モードは 2 種類あります:

- **edge**: TTS のタイムスタンプを利用します。GPU なしで高速に動作し、既定のモードです。
- **whisper**: より正確な字幕のタイムラインが必要な場合に、ローカルの `faster-whisper` による文字起こしを利用します。モデルは初回利用時にダウンロードされます。

モードを切り替えるには `config.toml` の `subtitle_provider` を設定します。Whisper は既定で約 3 GB の `large-v3` モデルを使用します。より小さく高速な約 1.6 GB の `large-v3-turbo` モデルを使う場合:

```toml
[app]
subtitle_provider = "whisper"

[whisper]
model_size = "large-v3-turbo"
```

> 初回利用時、Whisper は Hugging Face からモデルを自動的にダウンロードします。自動ダウンロードに失敗する場合は、[Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v3) から `whisper-large-v3` を手動でダウンロードしてください。

モデルを展開したら、ディレクトリ全体を `.\AisenStudio\models` に配置します。最終的なパスは `.\AisenStudio\models\whisper-large-v3` になります:

```
AisenStudio
  ├─models
  │   └─whisper-large-v3
  │          config.json
  │          model.bin
  │          preprocessor_config.json
  │          tokenizer.json
  │          vocabulary.json
```

### BGM

動画の BGM は、プロジェクトの `resource/songs` ディレクトリにあります。

> 現在のプロジェクトには YouTube 動画由来の既定の音楽がいくつか含まれています。著作権上の問題がある場合は削除してください。

### 字幕フォント

動画の字幕描画に使うフォントは、プロジェクトの `resource/fonts` ディレクトリにあります。独自のフォントを追加することもできます。

## よくある質問 🤔

<details>
<summary>RuntimeError: No ffmpeg exe could be found</summary>

通常、ffmpeg は自動的にダウンロードされ、検出されます。
しかし、環境の問題で自動ダウンロードができない場合は、次のようなエラーが発生することがあります:

```
RuntimeError: No ffmpeg exe could be found.
Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.
```

この場合は、[gyan.dev](https://www.gyan.dev/ffmpeg/builds/) から FFmpeg をダウンロードして展開し、`ffmpeg_path` に実際のインストールパスを設定してください。

```toml
[app]
# 実際のパスに合わせて設定してください。Windows のパス区切り文字は \\ である点に注意してください
ffmpeg_path = "C:\\ffmpeg\\bin\\ffmpeg.exe"
```

</details>

<details>
<summary>OSError: [Errno 24] Too many open files</summary>

これはシステムのオープンファイル数の上限が原因です。システムのファイルオープン数の上限を変更することで解決できます。

現在の上限を確認します:

```shell
ulimit -n
```

低すぎる場合は、例えば次のように引き上げます:

```shell
ulimit -n 10240
```

</details>

<details>
<summary>Whisper モデルのダウンロードに失敗する</summary>

```
LocalEntryNotFoundError: Cannot find an appropriate cached snapshot folder for the specified revision on the local disk and
outgoing traffic has been disabled.
To enable repo look-ups and downloads online, pass 'local_files_only=False' as input.
```

または

```
An error occurred while synchronizing the model Systran/faster-whisper-large-v3 from the Hugging Face Hub:
An error happened while trying to locate the files on the Hub and we cannot find the appropriate snapshot folder for the
specified revision on the local disk. Please check your internet connection and try again.
Trying to load the model directly from the local cache, if it exists.
```

解決方法: [Hugging Face からモデルを手動でダウンロードする方法を参照してください](#字幕生成)

</details>

## フィードバックと提案 📢

- [issue](https://github.com/aisenhub/AisenStudio/issues) または [pull request](https://github.com/aisenhub/AisenStudio/pulls) を送っていただけます。

## ライセンス 📝

[`LICENSE`](LICENSE) ファイルをクリックしてご覧ください
