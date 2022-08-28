# @Author: Hengyu Shang(shanghengyu997@outlook.com)
# @License: MIT License
# @Last Modified by: Hengyu Shang(shanghengyu997@outlook.com)
# @Last Modified time: 2022-08-28
# @Version: v0.1

source $(dirname $(readlink -f "$0"))/toy_env.sh

alias bupt_gw_on="curl -d 'user=${BUPT_GW_USER}&pass=${BUPT_GW_PASS}' http://10.3.8.211/login"
alias bupt_gw_off="curl http://10.3.8.211/logout"
alias bupt_portal_on="curl -d 'user=${BUPT_GW_USER}&pass=${BUPT_GW_PASS}' http://10.3.8.216/login"
alias bupt_portal_off="curl http://10.3.8.216/logout"
alias bupt_vpn_on="echo ${BUPT_GW_PASS} | sudo nohup openconnect --protocol=gp --user=2020110887 --passwd-on-stdin vpn.bupt.edu.cn > ~/log/bupt_vpn.log 2>&1"
alias vpn_off="sudo pkill openconnect"
alias proxy_on="export ALL_PROXY=http://${PROXY_HOST}:${PROXY_PORT}; \
export HTTP_PROXY=http://${PROXY_HOST}:${PROXY_PORT}; \
export HTTPS_PROXY=http://${PROXY_HOST}:${PROXY_PORT}; \
export all_proxy=http://${PROXY_HOST}:${PROXY_PORT}; \
export http_proxy=http://${PROXY_HOST}:${PROXY_PORT}; \
export https_proxy=http://${PROXY_HOST}:${PROXY_PORT};"
alias proxy_off="unset ALL_PROXY;unset HTTP_PROXY;unset HTTPS_PROXY;unset all_proxy;unset http_proxy;unset https_proxy;"
alias wget_proxy="wget -c -e use_proxy=yes -e http_proxy=${PROXY_HOST}:${PROXY_PORT} -e https_proxy=${PROXY_HOST}:${PROXY_PORT} -P ~/Downloads"
alias get_ip="curl ipinfo.io"

alias bark="curl https://api.day.app/${BARK_TOKEN}/${HOSTNAME}/bark"
bark_msg() {
    if [[ $1 == '-' ]]; then
        body=""
        while read line; do
            body="${body}${line}\n"
        done
    else
        body=$1
    fi
    body=${body//'\n'/%0A}
    body=${body:0:800}
    curl -d "title=${HOSTNAME}&device_key=${BARK_TOKEN}&body=${body}" -X "POST" "https://api.day.app/push"
    return 0
}

alias cp="cp -i"
