#!/bin/bash

# SSH 데몬 시작
service ssh start

# Hadoop 환경 변수 설정
source /etc/profile

# NameNode 포맷 (최초 실행 시만)
if [ ! -d "/data/dfs/name" ]; then
    hdfs namenode -format
fi

# Hadoop 서비스 시작
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh

# 컨테이너가 종료되지 않도록 대기
tail -f /dev/null