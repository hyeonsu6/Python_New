'''
���ϸ� : Ex03-appendHello.py

open �Լ� ���
    a(append mode) : �߰� ���
'''
file = open('./Python_New/Day01/hello.txt', 'at', encoding='UTF-8')
file.write('Hello\n')
file.write('Nice to meet you\n')
print('hello.txt ���Ͽ� ���ο� ������ �߰� �Ǿ����ϴ�.')
file.close()
