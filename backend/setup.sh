if [ -d ./.venv ]; then
    echo "Using existing .venv"
else
    echo "Creating new .venv"
    python3 -m venv ./.venv
fi
source ./.venv/bin/activate

echo "Installing requirements..."
pip3 install -r ./requirements.txt >/dev/null

echo "Updating index.cgi file..."
python_path=$(which python3)
echo $python_path
python_path_escaped=$((echo $python_path|sed -r 's/([\$\.\*\/\[\\^])/\\\1/g'|sed 's/[]]/\[]]/g')>&1)
sed -i -e "1s/.*/#!$python_path_escaped/g" ./index.cgi

GREEN='\033[0;32m'
NC='\033[0m' # No Color
printf "${GREEN}DONE${NC}\n"