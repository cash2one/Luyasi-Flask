pid=$(cat /tmp/dxc_uwsgi_master.pid)
echo $pid
kill -INT $pid
echo killed!
