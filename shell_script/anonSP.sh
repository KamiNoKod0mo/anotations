#!/bin/bash

# Definindo códigos de cores ANSI
cor_vermelha='\033[0;31m'
cor_verde='\033[0;32m'
cor_reset='\033[0m'


pingsweep(){
    if [ "$1" == "" ]
    then
        echo -e "${cor_verde}Ping Sweep${cor_reset}"
        echo "Modo de uso: $0 Rede"
        echo "Exemplo: $0 192.168.0"
    else
    echo -e "${cor_verde}Ping Sweep${cor_reset}"
    for host in {1..254};
    do
    ping -c 1 $1.$host | grep "64 bytes" | cut -d " " -f 4 | sed 's/.$//';
    done
    fi
}

#
#li,gt,le,ge,eq,ne
portscan(){
    if [ "$1" == "" ]
    then
        echo -e "${cor_verde}Port Scan${cor_reset}"
        echo "Modo de uso: $0 Rede"
        echo "Exemplo: $0 192.168.0 80"
    else
    echo -e "${cor_verde}Port Scan${cor_reset}"
    for ip in {1..254};
    do
    hping3 -S -p $2 -c 1 $1.$ip 2> /dev/null | grep "flags=SA" | cut -d " " -f 2 | cut -d "=" -f 2;
    done
    fi
}

#env
echo -n "Executar PortScan[ps] ou Ping Sweep[pi]: "
read esc
#echo "$esc"
if [ $esc == 'ps' ]; then
    portscan $1 $2
elif [ $esc == 'pi' ]; then
    pingsweep $1
else
    exit
fi
    


