# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2560
    v.cpus = 2
  end

  config.vm.network "public_network"

  config.vm.provision "shell", inline: <<-SHELL
    sysctl -w net.ipv6.conf.all.disable_ipv6=1
    sysctl -w net.ipv6.conf.default.disable_ipv6=1
    sysctl -w net.ipv6.conf.lo.disable_ipv6=1
  SHELL

  config.vm.provision :docker
  config.vm.provision :docker_compose

  config.vm.provision "shell", inline: <<-SHELL
    apt-add-repository --yes --update ppa:ansible/ansible
    apt-get install ansible conntrack --yes
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
    dpkg -i minikube_latest_amd64.deb
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    minikube start
    minikube addons enable ingress
  SHELL
end
