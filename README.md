<div align="center">

# AisenStudio 💸

### 一站式 AI 短视频生成工具

只需提供视频<b>主题</b>或<b>关键词</b>，即可自动生成视频脚本、匹配素材、生成字幕和背景音乐，并合成高清短视频。

[![Version](https://img.shields.io/github/v/release/aisenhub/AisenStudio?color=blue&label=version)](https://github.com/aisenhub/AisenStudio/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/aisenhub/AisenStudio/releases/latest)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Downloads](https://img.shields.io/github/downloads/aisenhub/AisenStudio/total)](https://github.com/aisenhub/AisenStudio/releases/latest)

<a href="https://www.star-history.com/aisenhub/AisenStudio"><img src="https://api.star-history.com/badge?repo=aisenhub/AisenStudio" alt="Star History Rank" style="height: 55px;" height="55"/></a>

简体中文 | [English](README-en.md) | [日本語](README-ja.md) | [版本发布](https://github.com/aisenhub/AisenStudio/releases) | [问题反馈](https://github.com/aisenhub/AisenStudio/issues)

</div>

## 界面预览 🖥️

<h4 align="center">WebUI</h4>

![](docs/webui.jpg)

<h4 align="center">API</h4>

![](docs/api.jpg)

---

## 功能特性 🎯

### 创作入口与工作流

- [x] 提供 **AI Agent、WebUI、API 和 CLI** 四种使用方式，既能快速上手，也能接入自动化流程
- [x] 从主题自动完成脚本、配音、素材、字幕、配乐和剪辑，也支持在每个环节使用自定义内容
- [x] 支持 **批量生成多条成片**、任务历史记录，以及生成设置与 API Key 的导入、导出和恢复

### 脚本与模型服务

- [x] 支持 AI 自动生成或改写 **多语言视频脚本**，也可以直接使用自定义脚本
- [x] 支持 [Kimi / Moonshot AI](https://platform.kimi.com)、[OpenAI](https://platform.openai.com/api-keys)、[Anthropic Claude](https://platform.claude.com/settings/keys)、[Google Gemini](https://aistudio.google.com/app/apikey)、[DeepSeek](https://platform.deepseek.com/api_keys)、[阿里云通义千问](https://dashscope.console.aliyun.com/apiKey)、[Microsoft Azure OpenAI](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/OpenAI)、[火山引擎方舟](https://console.volcengine.com/ark)、[xAI Grok](https://console.x.ai/)、[MiniMax](https://platform.minimaxi.com/) 和 [小米 MiMo](https://platform.xiaomimimo.com/docs/zh-CN/quick-start/first-api-call) 等主流模型服务
- [x] 兼容 [胜算云](https://www.shengsuanyun.com)、[APIMart](https://apimart.ai)、[Cloudflare AI Gateway](https://dash.cloudflare.com/)、[魔搭 ModelScope](https://modelscope.cn/docs/model-service/API-Inference/intro)、[AIHubMix](https://aihubmix.com/)、[AIML API](https://aimlapi.com/app/keys)、[EvoLink](https://evolink.ai/dashboard/keys)、[OpenRouter](https://openrouter.ai/settings/keys)、[API Route](https://www.api-route.com/)、[Ollama](https://ollama.com/)、[Claude Code 订阅](https://code.claude.com/docs)、[OneAPI](https://github.com/songquanpeng/one-api)、[LiteLLM](https://docs.litellm.ai/docs/providers)、[Groq](https://console.groq.com/keys) 和 [Pollinations AI](https://enter.pollinations.ai/) 等统一网关、聚合平台和本地运行环境

### 视频与图片素材

- [x] 支持上传自己的 **本地图片和视频**，也可从 [Pexels（免费）](https://www.pexels.com/api/)、[Pixabay（免费）](https://pixabay.com/api/docs/) 和 [Coverr](https://coverr.co/developers?ctx=header_navigation) 获取高清库存素材
- [x] 支持 [秘塔 MiniMax H3](https://metaso.cn) 文生视频，可生成 `768P`/`2K`、4～15 秒的原始素材，并适配 `9:16`、`16:9` 和 `1:1` 三种画幅
- [x] 支持 [胜算云 AI 视频](https://www.shengsuanyun.com)，可生成多段 AI 视频素材，并沿用项目的配音、字幕和剪辑流程合成成片
- [x] 原生接入 [火山引擎方舟 Seedance](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey)，可根据脚本片段生成连贯的视频画面
- [x] 支持 [WaveSpeed AI](https://wavespeed.ai) 文生视频，可根据脚本关键词快速生成原创素材
- [x] 支持 [OFox](https://ofox.ai) 多模型文生视频，一个 API Key 即可调用 Seedance、Wan 等模型
- [x] 通过异步 [MuAPI](https://muapi.ai) 文生视频接口生成 3～12 秒 AI 视频素材，并支持配置 Endpoint、画幅、分辨率和轮询参数
- [x] 支持 [OpenAI 兼容文生图](https://platform.openai.com/docs/guides/image-generation)，可连接云端服务或自定义图片网关，并将生成图片转换为动态视频片段
- [x] 支持调整片段时长、画面适配方式和素材匹配顺序，以适配不同画幅和叙事节奏

### 配音、字幕与配乐

- [x] 支持自动配音、上传配音和无配音三种方式，并提供音色试听与完整配音预览
- [x] 集成 **Edge TTS（免费、无需 API Key）**、Azure Speech、SiliconFlow、Google Gemini、小米 MiMo、MiniMax、ElevenLabs、Chatterbox、Kokoro、Fish Audio 和 ModelBest VoxCPM 等配音服务
- [x] 支持自动生成字幕，可调整字体、位置、颜色、大小、描边和背景样式
- [x] 支持随机、本地及 AI 生成背景音乐，并可独立控制音量

### 成片与发布

- [x] 支持竖屏 `9:16（1080×1920）`、横屏 `16:9（1920×1080）` 和方形 `1:1（1080×1080）`
- [x] 支持一键 **跨平台发布**，生成完成后可自动上传至 **TikTok、Instagram 和 YouTube Shorts**

## 配置要求 📦

- 建议系统：Windows 10、macOS 11.0 或更高版本，以及主流 Linux 发行版
- 本地部署需要 Python 3.11 或更高版本，推荐使用 Python 3.11
- GPU 不是必需项，但如果你希望本地转录、更快的视频处理或更顺畅的批量生成体验，建议使用带显存的独立显卡

| 项目 | 最低配置 | 推荐配置        | 理想配置        |
| ---- | -------- | --------------- | --------------- |
| CPU  | 4 核     | 6 到 8 核       | 8 核及以上      |
| RAM  | 4 GB     | 8 GB            | 16 GB 及以上    |
| GPU  | 非必须   | 4 GB 显存及以上 | 8 GB 显存及以上 |

- 如果你主要依赖云端 LLM、云端 TTS 和在线素材源，CPU 与内存比 GPU 更重要
- 如果你启用 `faster-whisper`、批量生成或更重的本地处理链路，GPU 会明显提升速度

## 快速开始 🚀

### 推荐使用方式

- 不想手动安装和配置：直接使用 AI Agent 生成视频
- 已有 Python 环境，想直接安装使用：[通过 pip 安装官方包](#通过-pip-安装官方包)
- Windows 用户：优先使用一键启动包，适合快速体验
- 需要源码部署或二次开发：使用 `uv` 管理环境和依赖
- 想要隔离运行环境：优先使用 Docker 部署

### 使用 AI Agent 生成视频

如果你的 AI Agent 支持读取 Skill 文档并操作本地终端，可以直接发送下面这段话。Agent 会自动完成安装、配置和视频生成；只有缺少必要的 API Key 时才会向你询问，完成后会返回生成的视频文件路径。目前支持 macOS 和 Windows。

```text
使用这个 Skill：https://raw.githubusercontent.com/aisenhub/AisenStudio/main/docs/skill/SKILL.md
帮我生成一个主题为“人工智能如何改变普通人的日常生活”的视频。
```

### 在 Google Colab 中运行

免去本地环境配置，点击直接在 Google Colab 中快速体验 MoneyPrinterTurbo

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aisenhub/AisenStudio/blob/main/docs/MoneyPrinterTurbo.ipynb)

### Windows 一键启动包

下载一键启动包，解压直接使用（路径不要有 **中文**、**特殊字符**、**空格**）

- [下载最新 Windows 一键启动包](https://github.com/aisenhub/AisenStudio/releases/latest)

> 请在页面下方的 **Assets** 区域下载 `.7z` 压缩包。GitHub 自动生成的
> `Source code (zip)` / `Source code (tar.gz)` 只是源码，解压后只有 `webui.bat`，
> 不含 `start.bat` 和 `update.bat`。

下载后，建议先**双击执行** `update.bat` 更新到**最新代码**，然后双击 `start.bat` 启动

启动后，会自动打开浏览器（如果打开是空白，建议换成 **Chrome** 或者 **Edge** 打开）

## 安装部署 📥

### 通过 pip 安装官方包

官方 PyPI 包名为 **[mpt](https://pypi.org/project/mpt/)**，由 `harry0703` 维护。
PyPI 上名为 `MoneyPrinterTurbo` 的包由第三方维护。

无需克隆仓库，需要 Python 3.11 或更高版本，推荐使用 Python 3.11。

**① 创建并激活虚拟环境**

macOS / Linux：

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**② 安装并启动**

```shell
python -m pip install mpt
mpt webui
```

WebUI 会自动打开浏览器。指定端口且不自动打开浏览器时，运行
`mpt webui --port 8503 --headless`；使用 CLI 生成视频前，可查看 `mpt cli --help`。

**③ 配置服务与管理文件**

首次启动会自动创建 `config.toml`。使用在线模型、素材或语音服务前，请在 WebUI
基础设置中填写相应的 API Key。安装版默认将配置和生成文件保存在：

| 系统 | 数据目录 |
| --- | --- |
| macOS | `~/Library/Application Support/MoneyPrinterTurbo` |
| Windows | `%LOCALAPPDATA%\MoneyPrinterTurbo` |
| Linux | `~/.local/share/MoneyPrinterTurbo`，或 `$XDG_DATA_HOME/MoneyPrinterTurbo` |

可在启动前设置 `MPT_HOME` 更改目录，生成的视频位于其中的 `storage/tasks` 下。
后续升级时，在已激活的虚拟环境中运行 `python -m pip install --upgrade mpt`。

### 源码部署前提条件

- 本地部署需要 Python 3.11 或更高版本
- Windows 用户建议避免使用包含中文、特殊字符或空格的项目路径

#### ① 克隆代码

```shell
git clone https://github.com/aisenhub/AisenStudio.git
```

#### ② 首次配置

首次启动时，项目会根据 `config.example.toml` 自动创建 `config.toml`，无需手动创建配置文件。使用云端大模型、在线素材或 AI 视频等服务前，请在 WebUI 的基础设置中填写对应的 API Key。

### Docker 部署 🐳

#### ① 启动 Docker

如果尚未安装 Docker，请先[下载并安装 Docker Desktop](https://www.docker.com/products/docker-desktop/)。

Windows 用户可以参考微软的文档：

1. [安装 WSL](https://learn.microsoft.com/zh-cn/windows/wsl/install)
2. [在 WSL 中使用 Docker 容器](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-containers)

```shell
cd AisenStudio
docker compose -f docker-compose.release.yml up
```

> 默认推荐使用 `docker-compose.release.yml`，它会直接拉取 GitHub Container Registry 上的预构建镜像：`ghcr.io/aisenhub/AisenStudio:latest`。
> 如果你需要本地重新构建镜像，可以继续使用 `docker compose up`。
> 首次启动前，请将 `config.example.toml` 复制为 `config.toml`，供容器挂载使用。

#### ② 访问 WebUI

打开浏览器，访问 http://127.0.0.1:8501

#### ③ 访问 API 文档

打开浏览器，访问 http://127.0.0.1:8080/docs 或者 http://127.0.0.1:8080/redoc

> API 默认仅允许同源网页访问。只有独立网页前端需要从其他来源直接调用 API 时，才应通过环境变量 `CORS_ALLOWED_ORIGINS` 配置可信来源，例如 `http://localhost:3000,https://frontend.example.com`。curl、Postman、n8n 和其他服务端调用不受 CORS 限制。

### 手动部署 📦

> 视频教程

- [完整的使用演示](https://v.douyin.com/iFhnwsKY/)
- [如何在 Windows 上部署](https://v.douyin.com/iFyjoW3M)

#### ① 创建虚拟环境

推荐使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境和依赖。项目支持 Python 3.11 或更高版本，以下示例使用 Python 3.11。

```shell
git clone https://github.com/aisenhub/AisenStudio.git
cd AisenStudio
uv python install 3.11
uv sync --frozen
```

如果你暂时不使用 `uv`，也可以继续使用 `venv + pip`

```shell
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

说明：

- `pyproject.toml` 是主依赖定义文件
- `uv.lock` 是锁文件，建议默认执行 `uv sync --frozen`
- `requirements.txt` 仅保留给旧的 `pip` 安装方式兼容使用

#### ② 启动 WebUI 🌐

注意需要到 MoneyPrinterTurbo 项目 `根目录` 下执行以下命令

###### Windows

```powershell
.\webui.bat
```

在 CMD 中也可以执行 `webui.bat`。
`webui.bat` 会优先使用项目 `.venv` 或一键包内置 Python；如果没有找到项目 Python，但已安装 `uv`，会自动切换为 `uv run streamlit`。
如需允许局域网内其他设备访问 WebUI，可以先执行 `set MPT_WEBUI_HOST=0.0.0.0`，再运行 `webui.bat`。

###### macOS 或 Linux

```shell
sh webui.sh
```

脚本会自动使用项目虚拟环境或 `uv`，并选择可用的本地端口。如需允许局域网内其他设备访问，可以执行：

```shell
MPT_WEBUI_HOST=0.0.0.0 sh webui.sh
```

启动后，会自动打开浏览器（如果打开是空白，建议换成 **Chrome** 或者 **Edge** 打开）

#### ③ 启动 API 服务 🚀

```shell
uv run python main.py
```

如果你已经手动激活了虚拟环境，也可以直接执行：

```shell
python main.py
```

#### ④ 纯命令行方式（无浏览器）⌨️

如果你无法使用浏览器或端口转发，可以直接在命令行生成视频。最简单的完整视频生成命令如下：

```shell
uv run python cli.py --video-subject "人工智能如何改变日常生活"
```

字幕样式和配音参数按以下优先级取值：**命令行显式参数 > `config.toml` 中
`[ui]` 保存的 WebUI 设置 > 内置默认值**。其余生成设置（如背景音乐、视频数量、
段落数量等）不会自动沿用 WebUI 的保存值。若 WebUI 中选择了上传自备音频，
命令行需要显式传入 `--custom-audio-file`，因为音频路径不会被保存。

如需查看完整命令、参数说明和使用方法，可以执行：

```shell
uv run python cli.py --help
```

如需顺序执行多个任务，可通过 `--batch-file` 提供 UTF-8 JSON 数组或 JSONL
清单。CLI 参数作为全局默认值，每个对象可覆盖 `VideoParams` 字段：

```shell
uv run python cli.py --batch-file ./tasks.json --stop-at video
```

清单最多包含 100 个任务且不超过 1 MiB。所有条目会在第一个任务启动前完成
参数与本地文件预检；单个任务运行失败不会阻止后续条目，结束后会输出统一的
JSON 汇总。清单中的相对自定义音频与本地素材路径以清单目录为基准。

## 配音、字幕与配乐 🎙️

### 语音合成

WebUI 中的 **Azure TTS V1** 基于 **Edge TTS**，免费且无需 API Key。项目同时支持 **Azure TTS V2**、**SiliconFlow TTS**、**Google Gemini TTS**、**小米 MiMo TTS**、**MiniMax TTS**、**ElevenLabs TTS**、自托管 **Chatterbox TTS**、自托管 **Kokoro TTS**、**Fish Audio TTS**、[ModelBest VoxCPM TTS](https://platform.modelbest.cn/console/docs/api/audio)，以及无配音模式。

可直接在 WebUI 中选择 Provider 和音色，并按照界面提示填写所需凭据。Edge TTS 不需要 API Key；[Azure TTS V2](https://portal.azure.com/) 及其他云端服务需要对应平台的凭据。Edge TTS 音色可查看：[音色列表](./docs/voice-list.txt)。

ModelBest VoxCPM 需要填写 API Key 和支持 `speech_synthesis` 的模型 ID。服务以 SSE 返回 WAV 音频，项目会自动转换为视频流水线使用的 MP3。除了普通文本合成，还可以上传参考音频复刻说话人音色；开启“保留参考音频的节奏与情绪”后，默认复用这段音频并要求填写其准确逐字稿，也可另选一段节奏与情绪示范，通过 `prompt_audio` 和 `prompt_text` 延续演绎。WebUI 可使用本地 Whisper 自动生成可编辑的逐字稿草稿。上传文件最大 20 MiB，转换后的单个 WAV 最大 5 MiB。参考素材仅用于当前浏览器会话和任务，不写入配置、预设、任务历史或日志。

### 字幕生成

当前支持两种字幕生成方式：

- **edge**：使用 TTS 时间戳生成字幕，速度快，不需要 GPU，默认使用该模式。
- **whisper**：使用本地 `faster-whisper` 转写音频，适用于需要更准确字幕时间轴的场景。首次使用时需要下载模型。

在 `config.toml` 中修改 `subtitle_provider` 即可切换模式。Whisper 默认使用约 3 GB 的 `large-v3`；如需更小、更快的模型，可以使用约 1.6 GB 的 `large-v3-turbo`：

```toml
[app]
subtitle_provider = "whisper"

[whisper]
model_size = "large-v3-turbo"
```

> 首次使用 Whisper 时，程序会自动从 Hugging Face 下载模型。如果当前网络无法自动下载，可以从 [Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v3) 手动下载 `whisper-large-v3`。

下载并解压后，将整个目录放到 `.\AisenStudio\models`，最终路径应为 `.\AisenStudio\models\whisper-large-v3`：

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

### 背景音乐

用于视频的背景音乐，位于项目的 `resource/songs` 目录下。

> 当前项目里面放了一些默认的音乐，来自于 YouTube 视频，如有侵权，请删除。

### 字幕字体

用于视频字幕的渲染，位于项目的 `resource/fonts` 目录下，你也可以放进去自己的字体。

## 常见问题 🤔

<details>
<summary>RuntimeError: No ffmpeg exe could be found</summary>

通常情况下，ffmpeg 会被自动下载，并且会被自动检测到。
但是如果你的环境有问题，无法自动下载，可能会遇到如下错误：

```
RuntimeError: No ffmpeg exe could be found.
Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable.
```

此时可以从 [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) 下载 FFmpeg。解压后，将 `ffmpeg_path` 设置为实际安装路径即可。

```toml
[app]
# 请根据你的实际路径设置，注意 Windows 路径分隔符为 \\
ffmpeg_path = "C:\\ffmpeg\\bin\\ffmpeg.exe"
```

</details>

<details>
<summary>OSError: [Errno 24] Too many open files</summary>

这个问题是由于系统打开文件数限制导致的，可以通过修改系统的文件打开数限制来解决。

查看当前限制

```shell
ulimit -n
```

如果过低，可以调高一些，比如

```shell
ulimit -n 10240
```

</details>

<details>
<summary>Whisper 模型下载失败</summary>

```
LocalEntryNotFoundError: Cannot find an appropriate cached snapshot folder for the specified revision on the local disk and
outgoing traffic has been disabled.
To enable repo look-ups and downloads online, pass 'local_files_only=False' as input.
```

或者

```
An error occurred while synchronizing the model Systran/faster-whisper-large-v3 from the Hugging Face Hub:
An error happened while trying to locate the files on the Hub and we cannot find the appropriate snapshot folder for the
specified revision on the local disk. Please check your internet connection and try again.
Trying to load the model directly from the local cache, if it exists.
```

解决方法：[查看如何从 Hugging Face 手动下载模型](#字幕生成)

</details>

## 反馈建议 📢

- 可以提交 [issue](https://github.com/aisenhub/AisenStudio/issues) 或者 [pull request](https://github.com/aisenhub/AisenStudio/pulls)。

## 许可证 📝

点击查看 [`LICENSE`](LICENSE) 文件
