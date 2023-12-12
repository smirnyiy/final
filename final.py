import logging
import os
import argparse
from collections import namedtuple

logging.basicConfig(filename='Log/Data_log.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def parse_folder(dir_path):
    if not os.path.isdir(dir_path):
        msg = f'Указан неверный путь: {dir_path}'
        logger.error(msg)
        print(msg)
        exit(1)

    data_list = [(dirs, folders, files) for dirs, folders, files in os.walk(dir_path)]
    # print(*data_list)
    clas_list = []

    Data = namedtuple('Data',
                      ['file_name', 'file_exten', 'dir_flag', 'parent_dir'])
    for i in range(0, len(data_list)):
        parent_dir = data_list[i][0]
        dir_list = data_list[i][1]
        file_list = data_list[i][2]

        for el in dir_list:
            dir_flag = 'Yes'
            file_name = el
            file_exten = ''
            d = Data(file_name, file_exten, dir_flag, parent_dir)
            clas_list.append(d)
            logger.info(
                f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

        for item in file_list:
            dir_flag = 'No'
            try:
                file_name, file_exten = item.split('.')
            except Exception:
                *file_name, file_exten = item.split('.')

            d = Data(file_name, file_exten, dir_flag, parent_dir)
            clas_list.append(d)
            logger.info(
                f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

    # print(*clas_list, sep="\n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Принимает путь до директории")
    parser.add_argument('dir_path', type=str, help='Путь до директории')
    args = parser.parse_args()
    parse_folder(args.dir_path)

# запуск командной строкой: python final.py 'G:\HW\Books'
