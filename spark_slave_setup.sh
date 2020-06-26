sudo apt-get install -y safe-rm
sudo apt-get install -y git
sudo apt-get install -y screen
sudo apt-get install -y unzip
sudo apt-get install -y gcc g++ make
sudo apt-get install -y zlib-devel
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl https://pyenv.run | bash
export PATH="~/.pyenv/bin:$PATH"
pyenv install 3.6.9
pyenv global 3.6.9
eval "$(pyenv init -)"
python --version

pip install --upgrade pip
python -m pip install pysnooper
python -m pip install BitVector
python -m pip install xxhash
python -m pip install pyspark
export PYSPARK_PYTHON=python3

echo "deb http://ppa.launchpad.net/linuxuprising/java/ubuntu bionic main" | sudo tee /etc/apt/sources.list.d/linuxuprising-java.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 73C3DB2A
sudo apt-get update
sudo apt-get install -y oracle-java14-installer
sudo apt-get install -y oracle-java14-set-default

wget http://apache.mirror.amaze.com.au/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
tar -xvzf "spark-2.4.5-bin-hadoop2.7.tgz"
cd spark-2.4.5-bin-hadoop2.7/sbin

screen -S spark_slave
./start-slave.sh spark://your_ip_here:7077



