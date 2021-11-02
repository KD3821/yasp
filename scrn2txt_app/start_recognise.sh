#!/bin/bash
scp /home/dk/PycharmProjects/yasp_api/screen_text/blabla.png root@185.178.44.143:/root/yasp/screen_text/
ssh root@185.178.44.143 <<'ENDSSH'
bash /root/virt_env_wrapper3.sh
ENDSSH
scp root@185.178.44.143:/root/yasp/screen_text/blabla_done.txt /home/dk/2035_practice/yasp_final/
mv /home/dk/PycharmProjects/yasp_api/screen_text/blabla.png /home/dk/2035_practice/yasp_final/
