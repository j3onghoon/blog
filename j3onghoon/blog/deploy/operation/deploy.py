from pyinfra.operations import git

git.repo('git@github.com:j3onghoon/blog.git', '/home/ubuntu/blog')
