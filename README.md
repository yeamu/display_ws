## 构建编译
`` catkin_make_isolated ``
## 启动底盘
`` roslaunch slam_2d one_base.launch ``
## 开始建图
`` roslaunch slam_2d mapping.launch ``
## 保存静态地图
建图完毕，运行  
`` roslaunch slam_2d map_save.launch ``
## 开始导航
`` roslaunch slam_2d navigation.launch ``
