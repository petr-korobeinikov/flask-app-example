# Flask application example

## Development setup

### Setup vm

    $ cp Vagrantfile.dist Vagrantfile
    $ vagrant up

### Deploy state of vm

    $ cd ansible
    $ cp ansible.cfg.dist ansible.cfg
    $ ansible-galaxy install -r requirements.yml
    $ ansible-playbook -i inventory/vagrant playbook.yml

### Install requirements

    $ workon <virtualenv-name>
    $ pip install -r requirements.txt

### Install bower components

    $ bower install

### Load fixtures data (aka database sandboxing)

    $ APP_SETTINGS=DevelopmentConfig python manage.py load_fixtures

See `manage.py:load_fixtures()` for more details.
