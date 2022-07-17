#!/bin/bash
# Date : 2020/11/26
# Author : Kaimin
# Description : This is a program to create Pipeline environment.

# !!!!!!!! Please move to location which you want to install !!!!!!!

# Install Git
sudo yum install git-all

# Download & Install SeqTK
git clone https://github.com/lh3/seqtk.git;
cd seqtk; make

# Download Trimmomatic
wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip
unzip Trimmomatic-0.39.zip

# Download FLASH
wget http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz
tar zxvf FLASH-1.2.11-Linux-x86_64.tar.gz

# Download & Install Python3.8
wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
tar zxvf Python-3.8.7.tgz
cd Python-3.8.7
./configure
make
make install

# Install & Upgrad Pip
python -m pip --version
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install -U pip

# Download & Install Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
sh Anaconda3-2020.11-Linux-x86_64.sh
conda update conda
conda update anaconda
conda create -n python38 python=3.8
conda create -n python27 python=2.7

# Download & Install Qiime2
wget https://data.qiime2.org/distro/core/qiime2-2020.11-py36-linux-conda.yml
conda env create -n Qiime2 --file qiime2-2020.11-py36-linux-conda.yml
rm qiime2-2020.11-py36-linux-conda.yml
exit