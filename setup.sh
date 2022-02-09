#!/bin/sh

PLATFORM=`uname -a | awk -F ' ' '{print $1}'`

echo "===Upgrade pip==="
python3 -m pip install --upgrade pip

echo "===Platform: $PLATFORM==="
echo "===Install package dependency==="
if [[ $PLATFORM == "Darwin" ]]; then
	CPU_BRAND=`sysctl -n machdep.cpu.brand_string`
	if [[ ${CPU_BRAND} == "Apple M1" ]]; then
		pip3 install -r requirements_M1.txt
	else
		pip3 install -r requirements.txt
	fi
elif [ $PLATFORM == "Linux" ]; then
    pip3 install -r requirements.txt
else
	echo "Unsupport platform '$PLATFORM'"
fi
