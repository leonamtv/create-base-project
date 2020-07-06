#!/bin/bash

echo $1

if [ -z $1 ]
then
	echo "vazio"
elif [ $1 == "." ]
then
	echo "aqui"
else
	mkdir -p $1
	cd $1
	touch teste.txt
fi

