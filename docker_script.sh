ls /checkout
rm -rf $APP_HOME
mkdir $APP_HOME
cp -a /checkout/. $APP_HOME
gem install jekyll bundler
cd $APP_HOME
bundle install
ls -a
pip3 install -r /myapp/requirements.txt
# python3 /myapp/_doc_builder/update_readme.py
python3 /myapp/_doc_builder/update_meta.py
bundle exec jekyll serve --trace --livereload --host "0.0.0.0"