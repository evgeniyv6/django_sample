### django_sample
**django+nginx+gunicorn+docker+docker-compose**

Simple web page with the current datetime

Install docker and docker-compose. Run: ansible-playbook -i ./inventory ./site.yml  --vault-password-file ./vaultkey.txt.
U can combine --tags copy,docker,copy_big,docker_cmp. Then open http://0.0.0.0:8090/date, see ansible/roles/local_docker/defaults/main.yml for the settings.

U can delete the containers and the images with the bash script: ./cleardocker.sh all with the flag all, or with the flag img (to delete the images), the flag ps (to delete the containers)