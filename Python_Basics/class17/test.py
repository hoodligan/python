# coding=utf-8
import zipfile
import os

def zipDir(dirpath, outFullName):
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # ȥ��Ŀ���·����ֻ��Ŀ���ļ����±ߵ��ļ����ļ��н���ѹ��
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
    print('ѹ���ɹ�')


if __name__ =='__main__':
    dirpath = r'./files/2020-11-16 21-15-18test_report.html'
    outFullName = r'./files/2020-11-16 21-15-18test_report.zip'
    zipDir(dirpath, outFullName)

# 这部分内容有问题，还没好
