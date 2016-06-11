#!/bin/bash
cd ..
project_root=$(pwd)

echo "Project root is $project_root"

echo "Please type the name of your project:"

read project_name

echo "Creating virtual envinronment.."
virtualenv --no-site-packages --prompt="($project_name)" venv
echo "Success.."

echo "Installing dependencies.."
source ./venv/bin/activate
pip install -r ./install/req.txt
echo "Success.."

echo "Installing models.."
python manage.py migrate

mkdir media && mkdir media/answers

echo "Creating superuser.."
python manage.py createsuperuser

echo "Setup is done."
