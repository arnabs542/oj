## Java debugging tools
```shell
jstat -gcutil `ps aux |grep java |grep appName |head -n 1 | awk '{print $2}'` 500 100000

jmap -F -histo `ps aux |grep java |grep appName  |head -n 1| awk '{print $2}'`
```
