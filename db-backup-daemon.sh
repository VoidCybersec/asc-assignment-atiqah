FILE=asc_secure2-backup-`date +"%Y%m%d"`.sql
DATABASE=asc_secure2
USER=root
PASS=1101

mysqldump --opt --user=${USER} --password=${PASS} ${DATABASE} > /home/void/Documents/asc-assignment-atiqah/sql-backup/${FILE}