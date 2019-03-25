import os

# author Rich.Chu
# email：mail@zhutingyu.com

# 视频所在路径，定位到视频顶层
# enter PATH that you need rename files location
path = "/Users/rich/Desktop/test_dir"

# 需要替换掉的文字
# enter string that you want to replace
preReplace = "wait_to_replace"

# 需要替换为哪个文字或字符串,不填写则为删除
# enter string that will be your new filename
afterReplace = "i_will_replace_preReplace"

# 要更名的文件类型
# what kind of files do you want to rename? e.g wmv
fileType = "wmv"

files = list()


def traverse(target):
    # 遍历出所有文件，存储在一个数组中并返回
    # return a List, that will include all file what you want to rename

    fs = os.listdir(target)
    for file in fs:
        temp_path = os.path.join(target, file)
        if not os.path.isdir(temp_path):
            if temp_path[-len(fileType):] == fileType:
                files.append(temp_path)
        else:
            traverse(temp_path)

    return files


def rename(file):
    # 遍历数组中所有的文件，并替换掉所有需要替换掉的文字
    # it will rename all files

    for i in files:
        if preReplace in i:
            new_name = i.replace(preReplace, afterReplace)

            os.rename(i, new_name)


def main():
    # 主函数
    # main function

    res = traverse(path)
    rename(res)


if __name__ == '__main__':
    # 程序入口
    # Program Entry

    main()
