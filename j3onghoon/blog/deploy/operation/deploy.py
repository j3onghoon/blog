from pyinfra.operations import git, systemd

git.repo('git@github.com:j3onghoon/blog.git', '/home/ubuntu/blog')

systemd.daemon_reload(_sudo=True)

systemd.service(service='gunicorn.service', reloaded=True, running=True, enabled=True, _sudo=True)
