# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/xenial64"
    config.vm.box_check_update = true

    config.vm.network "forwarded_port", guest:8000, host:8000
    config.vm.network "forwarded_port", guest:80, host:8080
    config.vm.network "forwarded_port", guest:5432, host:65432

    config.ssh.insert_key = true
    config.ssh.forward_agent = true

    config.vm.synced_folder "./", "/usr/local/apps"
end
