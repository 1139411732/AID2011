from multiprocessing import Pool, Queue

q = Queue()
import os


# 拷贝每一个文件 --》 进程池要做的事情
def copy(filename, old_folder, new_folder):
    fr = open(old_folder + "/" + filename, 'rb')
    fw = open(new_folder + "/" + filename, 'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n)
    fr.close()
    fw.close()

# def total_size():


# 创建进程池 参数为要拷贝的目录
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)

    total_size = os.path.getsize(old_folder)

    pool = Pool(4)
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,
                         args=(file, old_folder, new_folder))

    pool.close()
    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get()
        print(f'%{copy_size/total_size*100}')
    pool.join()


if __name__ == '__main__':
    main("/home/tarena/month02/day13")
