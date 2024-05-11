if [ -z "$(ls -A data)" ]; then
    ./utils/data_install.sh
fi

python3 -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt