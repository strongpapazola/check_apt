clear
echo '- - - DPKG LOCK - - -'
echo ' Author : strongpapazola'
echo
echo ' 1. Check'
echo ' 2. Kill'
echo ' 3. Hapus Cache'
read -p '> ' pilih
if [ $pilih = '1' ];then
while true
do
	clear
	ps aux | grep apt
	sleep 1
done
elif [ $pilih = '2' ];then
clear
ps aux | grep apt
echo '========================='
read -p 'Masukan ID : ' id
kill -9 $id
#banner
elif [ $pilih = '3' ];then
rm /var/cache/apt/archives/lock
rm /var/lib/apt/lists/lock
rm /var/lib/dpkg/lock
else
echo Abort.
fi
