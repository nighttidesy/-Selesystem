选课系统

角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程 
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
6. 创建讲师角色时要关联学校， 
7. 提供两个角色接口
7.1 学员视图， 可以注册， 交学费， 选择班级，
7.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 
7.3 管理视图，创建讲师， 创建班级，创建课程

8. 上面的操作产生的数据都通过pickle序列化保存到文件里
====================================================================
分析：
一：基础类
1.创建学校类，通过学校类创建学校
2.3 创建课程类，通过学校类创建课程，创建时候关联学校 创建时候要包含周期价格
4.创建班级类，但是通过学校创建班级，创建时候关联课程，讲师
5.创建学员类，学员自行注册创建，创建时候选择学校，选择上课班级
6.创建讲师类，通过学校类创建讲师，创建时候关联学校
二：逻辑类
7.创建三个视图类
1.学员视图：  拥有功能： 注册（注册时候选择班级）  交学费  上课
2.讲师视图：  讲课，讲课时候选择班级  进入讲课后可查看班级学员列表 
3.管理视图： 创建/删除讲师 创建/删除班级 创建/删除学校 创建/删除课程 创建/删除讲师  

文件结构如下:
![Image text](https://raw.githubusercontent.com/nighttidesy/images-packge/master/20180816174534.jpg)


程序逻辑结构图如下：

![Image text](https://github.com/nighttidesy/images-packge/blob/master/test.jpg)
