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
