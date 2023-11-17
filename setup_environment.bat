@echo off


conda create --name datathon2023 python=3.10 -y
conda activate datathon2023
conda install --file requirements.txt



echo Installation completed.
