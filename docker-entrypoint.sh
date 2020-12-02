#!/bin/bash
###########################################################
## Call trans opt: received. 2-19-98 13:24:18 REC:Loc    ##
##                                                       ##
##      Trace program: running                           ##
##                                                       ##
##            wake up, Neo...                            ##
##         the matrix has you                            ##
##       follow the white rabbit.                        ##
##                                                       ##
##           knock, knock, Neo.                          ##
##                                                       ##
##                         (`.         ,-,               ##
##                         ` `.    ,;' #                 ##
##                          `.  ,'# .'                   ##
##                           `. X #.'                    ##
##                 .-;--''--.._` ` (                     ##
##               .'            #   `                     ##
##              ,           ` '   Q '                    ##
##              ,         ,   `._    \                   ##
##           ,.|         '     `-.;_'                    ##
##           :  . `  ;    `  ` --,.._;                   ##
##            ' `    ,   )   .'                          ##
##               `._ ,  '   #_                           ##
##                  ; ,''-,;' ``-                        ##
##                   ``-..__``--`                        ##
###########################################################


MAIN_PROC_RUN=1
FIRST_RUN=1

trap "docker_stop" SIGINT SIGTERM

function docker_stop {
    echo "[TT-2021 $(date +'%F %H:%S')] Rcv end signal"
    kill -15 ${TT_PID}
    wait ${TT_PID}
    echo "[TT-2021 $(date +'%F %H:%S')] Stop service"
    export MAIN_PROC_RUN=0
}


function check_variables(){

    if [ -z "${TT_DBDATABASE}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_DBDATABASE not found, using default value"
        export TT_DBDATABASE="tt-db"
    fi
    
    if [ -z "${TT_DBHOST}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_DBHOST not found, using default value"
        export TT_DBHOST="127.0.0.1"
    fi
    
    if [ -z "${TT_DBPORT}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_DBPORT not found, using default value"
        export TT_DBPORT="3306"
    fi

    
    if [ -z "${TT_DBUSER}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_DBUSER not found, using default value"
        export TT_DBUSER="tt-user"
    fi
    
    if [ -z "${TT_DBPASSWORD}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_DBPASSWORD not found, using default value"
        export TT_DBPASSWORD="Leiciengabeephoh0phohh2ee"
    fi
    
    if [ -z "${TT_PORT}" ]; then
        echo "[TT-2021 $(date +'%F %H:%S')] Variable TT_PORT not found, using default value"
        export TT_PORT="8080"
    fi
}


while [ ${MAIN_PROC_RUN} -eq 1 ]; do
    if [ "${FIRST_RUN}" -ne 0 ] ; then
        source ../bin/activate
        echo "[TT-2021 $(date +'%F %H:%S')] Starting service..."
        sleep 5
        uwsgi --socket 0.0.0.0:$TT_PORT --protocol=http -w main:app --thunder-lock --enable-threads
        FIRST_RUN=$?
        TT_PID=$!
        deactivate
    fi
    echo "[TT-2021 $(date +'%F %H:%S')] Restarting service"
    sleep 10
done