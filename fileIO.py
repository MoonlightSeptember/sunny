 �ļ�IO�ļ򵥲���
 fo=open("F:\����\����\����fibo.txt",mode='r')
>>> print("�ļ���:",fo.name)
�ļ���: F:\����\����\����fibo.txt
>>> print("�Ƿ��ѹر�:",fo.closed)
�Ƿ��ѹر�: False
>>> print("����ģʽ:",fo.mode)
����ģʽ: r
##�½��ļ���д������
 with open("test.txt","wt")as out_file:
...     out_file.write("�����������\n���ȥ��!")