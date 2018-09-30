 文件IO的简单操作
 fo=open("F:\毕设\代码\调用fibo.txt",mode='r')
>>> print("文件名:",fo.name)
文件名: F:\毕设\代码\调用fibo.txt
>>> print("是否已关闭:",fo.closed)
是否已关闭: False
>>> print("访问模式:",fo.mode)
访问模式: r
##新建文件并写入内容
 with open("test.txt","wt")as out_file:
...     out_file.write("今天天气真好\n想出去玩!")