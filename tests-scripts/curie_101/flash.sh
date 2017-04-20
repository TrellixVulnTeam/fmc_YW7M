#!/bin/bash

TEMP_FLASHFILES_FOLDER=$1

echo "Calling sudo dfu-util -a sensor_core -D $TEMP_FLASHFILES_FOLDER/ssbl.signed.bin -d 8087:0aba"
sudo dfu-util -a sensor_core -D $TEMP_FLASHFILES_FOLDER/ssbl.signed.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a x86_app  -R -D $TEMP_FLASHFILES_FOLDER/bootupdater.signed.bin -d 8087:0aba"
sudo dfu-util -a x86_app  -R -D $TEMP_FLASHFILES_FOLDER/bootupdater.signed.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

sleep 20

echo "Calling sudo dfu-util -a fsbl -R     -D $TEMP_FLASHFILES_FOLDER/fsbl_quark.bin -d 8087:0aba"
sudo dfu-util -a fsbl -R     -D $TEMP_FLASHFILES_FOLDER/fsbl_quark.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

sleep 2

echo "Calling sudo dfu-util -a x86_app     -D $TEMP_FLASHFILES_FOLDER/quark.signed.bin -d 8087:0aba"
sudo dfu-util -a x86_app     -D $TEMP_FLASHFILES_FOLDER/quark.signed.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a sensor_core -D $TEMP_FLASHFILES_FOLDER/arc.bin -d 8087:0aba"
sudo dfu-util -a sensor_core -D $TEMP_FLASHFILES_FOLDER/arc.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a factory1    -D $TEMP_FLASHFILES_FOLDER/erase_factory_nonpersistent.bin -d 8087:0aba"
sudo dfu-util -a factory1    -D $TEMP_FLASHFILES_FOLDER/erase_factory_nonpersistent.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a panic       -D $TEMP_FLASHFILES_FOLDER/erase_panic.bin -d 8087:0aba"
sudo dfu-util -a panic       -D $TEMP_FLASHFILES_FOLDER/erase_panic.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a ble_core    -D $TEMP_FLASHFILES_FOLDER/ble_core/image.bin -d 8087:0aba"
sudo dfu-util -a ble_core    -D $TEMP_FLASHFILES_FOLDER/ble_core/image.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Calling sudo dfu-util -a data -R     -D $TEMP_FLASHFILES_FOLDER/erase_data.bin -d 8087:0aba"
sudo dfu-util -a data -R     -D $TEMP_FLASHFILES_FOLDER/erase_data.bin -d 8087:0aba
if [ $? -ne 0 ]; then
  echo "DFU failed"
  exit 1
fi

echo "Flashing succeeded"


