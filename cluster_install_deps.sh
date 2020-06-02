sudo apt-get install -y safe-rm

python -m pip install pysnooper
python -m pip install BitVector
python -m pip install xxhash
python -m pip install pyspark

mkdir -p /tmp/compress_research
rm -rf /tmp/compress_research
gsutil cp -r gs://compress-cluster/compress_research /tmp
chmod 777 /tmp/compress_research/cluster_start.py

export PYSPARK_PYTHON=python3