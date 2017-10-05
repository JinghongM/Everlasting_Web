# Ruby on Rail installation
This is an introduction about how to install Ruby and its web framework Ruby on Rails.'

----------------------------

## Install rvm
The first step is to install rvm, the full name is Ruby Version Manager, which is a good ruby management tool
```sh
curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
curl -sSL https://get.rvm.io | bash -s stable
```
Check installation
```sh
rvm -v
```
-----------------------------

## Install Ruby
After we install rvm, we can esasily install ruby
```sh
rvm intall ruby
```
You also can re-install ruby by 'rvm reinstall ruby' and delete ruby by 'rvm remove ruby'
Check whether installation ls successful
```sh
ruby -v
```
```sh
ruby -e 'p"hello ruby"'
```
-----------------------------

## Install Rails
Now, it is time for us to install rails

```sh
gem install rails
```
Check version
```sh
rails -v
```

## Change Database of Ruby On Rails to Mysql
As we know, ROR uses its own db 'sqlite' as its default database, but we need to change it to our mysql database.
First, we need to install mysql-client and mysql-server.
Second, we need to install some mysql dependencies such as:
```sh
sudo apt-get install libmysqlclient-dev       in Ubuntu
```
or
```sh
sudo yum install mysql-devel                   in Red Hat/CentOS
```
Keep in mind, the version of dependencies should corresponse to mysql's version.

Finally, install mysql2 driver by 'gem' command
```sh
gem install mysql2 -- --with-mysql-lib='The directory which is your mysql lib'
```
if you get this information, it means success:

Building native extensions with: '--with-mysql-lib=/usr/lib64/mysql'
This could take a while...
Successfully installed mysql2-0.4.9
Parsing documentation for mysql2-0.4.9
Installing ri documentation for mysql2-0.4.9
Done installing documentation for mysql2 after 0 seconds

## Create web application by use mysql database
```sh
rails new server -d mysql
```
# A good tutorial Web
http://codepany.com/blog/rails-5-how-to-create-ruby-on-rails-project-mysql-git/
