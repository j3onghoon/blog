from pyinfra.operations import git, systemd, apt, pip, files, server


apt.update(_sudo=True)
apt.packages(['python3', 'python3-venv', 'nginx', 'certbot', 'python3-certbot-nginx'], _sudo=True)

git.repo('https://github.com/j3onghoon/blog.git', '/home/ubuntu/blog')

pip.venv('/home/ubuntu/venv', python='python3')
pip.packages(requirements='/home/ubuntu/blog/requirements.txt', virtualenv='/home/ubuntu/venv')

server.shell(commands=['/home/ubuntu/venv/bin/python3 /home/ubuntu/blog/j3onghoon/manage.py migrate'])

files.put('j3onghoon/blog/deploy/nginx/nginx.conf', '/etc/nginx/sites-available/j3onghoon.com', _sudo=True)
files.put('j3onghoon/blog/deploy/gunicorn/gunicorn.service', '/etc/systemd/system/gunicorn.service', _sudo=True)
systemd.daemon_reload(_sudo=True)

systemd.service(service='gunicorn.service', reloaded=True, running=True, enabled=True, _sudo=True)
systemd.service(service='nginx.service', reloaded=True, enabled=True, _sudo=True)
server.shell(commands=['sudo certbot --nginx'])

