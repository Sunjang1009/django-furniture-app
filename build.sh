# Install dependencies
pip3 install -r deps.txt

# run migration
python3 manage.py migrate

python3 manage.py collectstatic --no-input