#-*-coding:UTF-8-*-
__author__ = 'CuiCan'

import os,sys
reload(sys)
sys.setdefaultencoding('utf8')

import Mails
import datetime

import MySQLdb


if __name__ == "__main__":
	conn= MySQLdb.connect(
     	  host='10.127.133.201',
          port = 3306,
          user='ambari_user',
          passwd='qwe1234',
          db ='ambari_metadata_2_2_0')
	cur = conn.cursor()
	sql = "SELECT t1.`host_name`, t1.`ipv4`, t2.`service_name`, t2.`component_name`,  t2.`current_state` \
             from `hosts` t1 join `hostcomponentstate` t2 on t1.`host_id`=t2.`host_id` \
            where t2.`service_name`<>'AMBARI_METRICS' \
	      and exists (select 1 from `hostcomponentstate_backup` t3 \
                           where t3.id=t2.id \
                             and t3.`current_state`='STARTED' \
                             and t2.`current_state`!='STARTED')"
							 
	cur.execute(sql)
	results = cur.fetchall()

	if(results):
		print (len(results))
		sub = "Ambari相关进程报警----监控邮件，请勿回复！"
		html = "<html>"
		html += "<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8' /></head>"
		html += "<style>"
		html += "table {border-collapse: collapse;}"
		html += "table th {border:1px solid #000000;text-align : center;}"
		html += "table td {border:1px solid #000000;}"
		html += "</style>"
		html += "<body>"
		html += "<center><b>" + sub + "</b></center>"
		html += "<table width='800'>"
		html += "<tr>"
		html += "<th width='30%'>主机名</th>"
		html += "<th width='10%'>IP</th>"
		html += "<th width='25%'>服务名</th>"
		html += "<th width='25%'>组件名</th>"
		html += "<th width='10%'>状态</th>"
		html += "</tr>" 
		for r in results:
			print '456'
			html += "<tr>"
			html += "<th width='30%'>"+r[0]+"</th>"
			html += "<th width='10%'>"+r[1]+"</th>"
			html += "<th width='25%'>"+r[2]+"</th>"
			html += "<th width='25%'>"+r[3]+"</th>"
			html += "<th width='10%'>"+r[4]+"</th>"
			html += "</tr>"
		html += "</table>"
		html += "</body>"
		html += "</html>"
		Mails.SendStatMail(sub, html)
	cur.close()
	conn.close()
