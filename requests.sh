#Source file:  access_log_Jul95

# 1st task:

oleksiyholyarchuk@ubuntu:~/Documents/Python$ cat access_log_Jul95 | awk {'print $(NF-1)'} | awk '/200|400|500/' | sort | uniq -c
1701534 200
      5 400
     62 500

# 2nd task:
oleksiyholyarchuk@ubuntu:~/Documents/Python$ cat access_log_Jul95 | awk {'print $6'} | grep 'GET\|POST\|PUT' | tr '"' ' '|sort | uniq -c
1887646  GET
    111  POST

#3rd task:

oleksiyholyarchuk@ubuntu:~/Documents/Python$ cat access_log_Jul95 | awk '{print $1}' | sort | uniq -c | sort -n | tail -n 10
   4353 disarray.demon.co.uk
   4863 news.ti.com
   4906 163.206.89.4
   5434 edams.ksc.nasa.gov
   5922 piweba2y.prodigy.com
   7573 siltb10.orl.mmc.com
   7852 alyssa.prodigy.com
   9868 piweba1y.prodigy.com
  11591 piweba4y.prodigy.com
  17572 piweba3y.prodigy.com

#4th task:

oleksiyholyarchuk@ubuntu:~/Documents/Python$ awk '{print $4}' access_log_Jul95 | cut -d: -f1 | uniq -c | head
  64714 [01/Jul/1995
  60265 [02/Jul/1995
  89584 [03/Jul/1995
  70452 [04/Jul/1995
  94575 [05/Jul/1995
 100960 [06/Jul/1995
  87233 [07/Jul/1995
  38867 [08/Jul/1995
  35272 [09/Jul/1995
  72860 [10/Jul/1995

 #5th task:

 oleksiyholyarchuk@ubuntu:~/Documents/Python$ grep "01/Jul" access_log_Jul95 | cut -d[ -f2 | cut -d] -f1 | awk -F: '{print $2":00"}' | sort -n | uniq -c
   3565 00:00
   3004 01:00
   2268 02:00
   1734 03:00
   1482 04:00
   1343 05:00
   1528 06:00
   1557 07:00
   1927 08:00
   2096 09:00
   3046 10:00
   3428 11:00
   2769 12:00
   3086 13:00
   3133 14:00
   3272 15:00
   3191 16:00
   3671 17:00
   3192 18:00
   2831 19:00
   2958 20:00
   3502 21:00
   3278 22:00
   2853 23:00

#6th task:

oleksiyholyarchuk@ubuntu:~/Documents/Python$ cat access_log_Jul95 | awk '{print $1}' | sort | uniq -c | sort -n | tail -n 10 | grep -v "news.ti.com"
   4353 disarray.demon.co.uk
   4906 163.206.89.4
   5434 edams.ksc.nasa.gov
   5922 piweba2y.prodigy.com
   7573 siltb10.orl.mmc.com
   7852 alyssa.prodigy.com
   9868 piweba1y.prodigy.com
  11591 piweba4y.prodigy.com
  17572 piweba3y.prodigy.com
