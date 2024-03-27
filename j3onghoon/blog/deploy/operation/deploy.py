from pyinfra.operations import git, systemd, apt, pip

apt.packages(['python3', 'nginx'], _sudo=True)

git.repo('git@github.com:j3onghoon/blog.git', '/home/ubuntu/blog')

pip.venv('/home/ubuntu/venv', python='python3')
pip.packages(requirments='/home/ubuntu/blog/requirements.txt', virtualenv='/home/ubuntu/venv')

systemd.daemon_reload(_sudo=True)

systemd.service(service='gunicorn.service', reloaded=True, running=True, enabled=True, _sudo=True)

