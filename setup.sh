if [ -d ./.venv ]; then
    echo "Using existing .venv"
else
    echo "Creating new .venv"
    python3 -m venv ./.venv
fi
source ./.venv/bin/activate

echo "Installing requirements..."
pip3 install -r ./requirements.txt >/dev/null

GREEN='\033[0;32m'
NC='\033[0m' # No Color
printf "${GREEN}DONE${NC}\n"
