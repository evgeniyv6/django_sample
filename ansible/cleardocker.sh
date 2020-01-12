#!/bin/bash

###################################################
# Flags:                                          #
# ps  - delete containers                         #
# img - delete images                             #
# all - stop, delete containers -> delete images  #
###################################################

declare -a docker_ps_array=`docker ps -a | grep -v -i -e grep -e container | awk '{print $1}' | tr '\n' ' '`
declare -a docker_img=`docker images | grep -v -i -e grep -e reposi | awk '{print $3}' | tr '\n' ' '`
echo  "docker ps - ${docker_ps_array[@]}"
echo  "docker images - ${docker_img[@]}"

func_usage() {
  cat<<EOF>&2
choose ps or img or all flag
EOF
}

clear_ps() {
for i in ${docker_ps_array[@]};do
  docker stop ${i} > /dev/null 2>&1
  docker rm ${i}
done
}
clear_img() {
for j in ${docker_img[@]};do
  docker rmi ${j}
done
}

main() {
  case "$1" in
     ps)
       clear_ps; exit 0
     ;;
     img)
       clear_img; exit 0
     ;;
     all)
       clear_ps;
       clear_img;
       exit 0
     ;;
     *) func_usage; exit 0;
  esac
}
main $@     
exit 0
