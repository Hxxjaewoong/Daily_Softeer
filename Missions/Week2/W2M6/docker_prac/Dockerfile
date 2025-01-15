# Base image
FROM python:3.9-slim

# Copy local files to container
COPY W1M1.ipynb /app/
COPY mtcars.csv /app/

# Install JupyterLab
RUN pip install --no-cache-dir jupyterlab pandas
# 필수 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean

# Python 라이브러리 설치
RUN pip install --no-cache-dir \
jupyterlab pandas matplotlib seaborn scikit-learn

# Set working directory
WORKDIR /app

# Expose port for JupyterLab
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter-lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

