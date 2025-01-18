# 使用官方的 Python 3.10 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将项目的依赖文件复制到容器中
COPY requirements.txt /app/

# 安装 Python 项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录的所有文件复制到容器的工作目录
COPY . /app/

# 设置环境变量，告诉 Flask 在生产环境中运行
ENV FLASK_ENV=production

# 设置 Flask 默认端口
EXPOSE 5000

# 启动 Flask 应用
CMD ["python", "app.py"]
