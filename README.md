#### 项目简介

`flask-chatbot` 是一个基于 Flask 框架和 Docker 容器化的 AI 聊天机器人项目。该项目通过自然语言处理（NLP）技术和语音合成功能，允许用户与聊天机器人进行文本和语音互动。

#### 功能特点

- **语音识别与语音反馈**：支持语音输入和语音输出，用户可以通过语音与聊天机器人交互。
- **即时聊天**：使用 Flask 构建的 RESTful API，允许用户输入文本与机器人进行对话。
- **Docker 容器化**：提供 Docker 镜像和容器，轻松部署和运行该聊天机器人应用。
- **支持中文**：聊天机器人支持中文输入和语音输出。

#### 技术栈

- **Flask**：Python 微框架，用于构建 API。
- **Speech Recognition**：用于语音识别，将语音转换为文本。
- **Speech Synthesis**：用于将文本转化为语音输出。
- **Docker**：容器化部署，简化开发、测试和生产环境的配置与管理。

#### 安装与运行

1. **克隆仓库**：

   ```
   git clone https://gitclone.com/github.com/benson80/flask-chatbot.git
   ```

2. **构建 Docker 镜像**：

   ```
   docker build -t flask-chatbot .
   ```

3. **运行 Docker 容器**：

   ```
   docker run -p 5000:5000 flask-chatbot
   ```

4. 访问 `http://localhost:5000` 即可与聊天机器人进行交互。

#### 使用方式

- 通过浏览器访问该应用，输入文本与聊天机器人对话。
- 支持语音输入与语音反馈，提供更加生动的交互体验。

#### 开发者支持

- 欢迎提交 Issue 或 Pull Request 来贡献代码。
- 如有任何问题，可以通过 GitHub Issues 或邮件联系我们。
