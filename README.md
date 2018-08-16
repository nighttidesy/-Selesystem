选课系统

角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校， 
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里


文件结构

--bin                       #启动脚本目录                      
    --start.py              #启动脚本
--core                      #核心代码目录
    --corepachge.py         #系统逻辑结构包文件
    --admin_view.py         #管理员视图
    --student_view.py       #学员视图
    --teacher_view.py       #讲师视图
--data                      #存放数据目录
--logs                      #存放日志目录
--doc                       #文档目录
README.md                   #说明文件




程序逻辑结构图如下：

![Image text](https://github.com/nighttidesy/images-packge/blob/master/test.jpg)
