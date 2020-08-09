#!/bin/bash

python3 search.py
cd ./image_retrieval/
python3 gifTojpg.py
python3 resize.py
docker run --gpus all --rm --name newDocker -d -it --privileged -e DISPLAY=$DISPLAY --net=host -v /home/musab/upwork/adrian\ teasdale/test:/root/work ufoym/deepo:latest bash
docker exec -w /root/work/image_retrieval/ newDocker python3 image_retrieval.py
docker stop newDocker