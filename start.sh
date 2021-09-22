echo "Cloning Repo, Please Wait..."
git clone -b alpha https://github.com/mrsammy07/VcVideoPlay.git /VcVideoPlay
cd /VcVideoPlay
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 main.py
