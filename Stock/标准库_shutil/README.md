shutil可以简单地理解为sh + util，shell工具的意思。shutil模块是对os模块的补充，主要针对文件的拷贝、删除、移动、压缩和解压操作。

警告: 即便是高阶文件拷贝函数 (shutil.copy(), shutil.copy2()) 也无法拷贝所有的文件元数据。