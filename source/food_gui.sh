#!/bin/bash

func_help() {
  echo -e "A simple calculator written on Python2/PyQt4"
  echo -e "\nUsage: food_gui [ -h | --help ] [ -v | --version ]" 
  echo -e "\nAdditional parametrs:"
  echo -e "  -h  --help        - show this help and exit"
  echo -e "  -v  --version     - show version and exit"
  echo -e "\nSee \"man 1 food_gui\" for more details"
  exit 0
}
func_ver() {
  echo -e "                      Food GUI"
  echo -e "A simple calculator written on Python2/PyQt4"
  echo -e "Version : 1.2.1                      License : GPL"
  echo -e "                                        by arcanis"
  echo -e "                      E-mail : esalexeev@gmail.com"
  exit 0
}

until [ -z $1 ]; do
  if [ "$1" = "-h" ]; then
    func_help; fi
  if [ "$1" = "--help" ]; then
    func_help; fi
  if [ "$1" = "-v" ]; then
    func_ver; fi
  if [ "$1" = "--version" ]; then
    func_ver; fi
  shift
done

python2 /usr/lib/python2.7/site-packages/food_gui.py
