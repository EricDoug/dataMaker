# -*- coding:utf-8 -*-
__author__ = 'EricDoug'
import csv

def listrows2csv(rows, output, header=None):
    """
    将rows list写入到csv中
    :param rows:
    :param output:
    :return:
    """
    with open(output, 'wb') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)


