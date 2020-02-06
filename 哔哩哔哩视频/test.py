import pymysql

db = pymysql.connect(host='localhost', user='xiaoshen', password='xiaoshen', port=3306)
cursor = db.cursor()
sql_str = """insert into `xiaoshen`.`wp_posts` ( `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) values ( '27', '2019-12-14 14:41:29', '2019-12-14 06:41:29', '<h2>一、channel 的基本介绍</h2>', 'go语言管道总结python', '', 'publish', 'open', 'open', '', 'go%e8%af%ad%e8%a8%80%e7%ae%a1%e9%81%93%e6%80%bb%e7%bb%93', '', '', '2019-12-14 15:10:25', '2019-12-14 07:10:25', '', '0', 'https://1024shen.com/?p=171', '0', 'post', '', '0');"""
cursor.execute(sql_str)
data = cursor.fetchone()
print(cursor.lastrowid)
db.commit()
print(data)