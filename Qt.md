---
title: Qt
date: 2023-07-28 21:03:52
categories: c++
tags: 
    - qt
    - c++
---

# Qt

## 信号和槽机制

> ```c++
> //拓展
> //信号可以连接信号
> //一个信号可以连接多个槽函数
> //多个信号可以连接同一个槽函数
> //信号和槽函数的参数的类型必须一一对应，有顺序要求
> //信号的参数个数必须>=槽函数的参数个数
>  //参数:参数1->信号的发送者，参数2->发送的信号（函数地址）,参数3->信号的接收者，参数4->处理的槽函数
>  connect(myBtn, &QPushButton::clicked, this, &myWidget::close);
> //最后一个参数可以使用lambda表达式[](){}
> 
> //重载版本
> void(Teacher::*tSignal)(QString) =&Teacher::hungry;
> void(Student::*sSignal)(QString) = &Student::treat;
> connect(t,tSignal,s,sSignal);
> ```

## MainWindow

> ```c
> //重置窗口大小
> resize(600,400);
> //1、创建菜单栏,菜单栏只能有一个
> QMenuBar * bar = menuBar();
> //将菜单栏放入窗口
> setMenuBar(bar);
> //创建菜单
> QMenu * fileMenu = bar->addMenu("文件");
> QMenu * editMenu = bar->addMenu("编辑");
> ```
>
>
> ```c
> //创建菜单项（下拉菜单）
> QAction* newFile =  fileMenu->addAction("新建");
> //添加分隔线
> fileMenu->addSeparator();
> QAction* openFile =  fileMenu->addAction("打开");
> 
> //2、创建工具栏
> QToolBar * toolBar = new QToolBar(this);
> //添加工具栏到左边
> addToolBar(Qt::LeftToolBarArea,toolBar);
> //设置工具栏为只允许左右停靠
> toolBar->setAllowedAreas(Qt::LeftToolBarArea|Qt::RightToolBarArea);
> //设置不能浮动（默认可以浮动）
> toolBar->setFloatable(false);
> //设置移动性（总开关）
> ```
>
>
> ```c++
> //    toolBar->setMovable(false);//相当于固定不能动了，这是总开关
> //工具栏设置功能,这里添加的是上面菜单栏中下拉菜单中的两个功能
> toolBar->addAction(newFile);
> toolBar->addSeparator();//添加分隔线
> toolBar->addAction(openFile);
> //工具栏中添加控件
> QPushButton* btn = new QPushButton("你干嘛",this);
> toolBar->addWidget(btn);
> 
> //3、状态栏，最多只有一个
> QStatusBar * stBar = new QStatusBar();
> setStatusBar(stBar);
> //放标签控件
> QLabel * label1 = new QLabel("多一眼看一眼就会爆炸",this);
> stBar->addWidget(label1);
> //在右边放标签控件
> QLabel * label2 = new QLabel("近一点靠近点快被融化",this);
> stBar->addPermanentWidget(label2);
> 
> //4、铆接部件（浮动窗口）可以有多个dock栏
> QDockWidget * dockWidget = new QDockWidget("一个真正的dock",this);
> addDockWidget(Qt::BottomDockWidgetArea,dockWidget);
> //设置为只能上下停靠
> dockWidget->setAllowedAreas(Qt::TopDockWidgetArea|Qt::BottomDockWidgetArea);
> 
> //设置中心部件,只能有一个
> QTextEdit* edit = new QTextEdit(this);
> setCentralWidget(edit);
> 
> //set->只能有一个
> //add->可以有多个
> ```

## 添加图片资源

> ```c
> //添加图片资源
> //使用添加资源+":+前缀名+文件名"
> ui->actionnew->setIcon(QIcon(":/image/kun.gif"));
> 
> /**
>  * 1、把图片文件复制到项目文件夹下面
>  * 2、右键项目添加新文件
>  * 3、添加Qt source文件->起个名字（res）
>  * 4、添加前缀（/），添加文件（选中文件夹中所有图片打开）
>  * 5、构建后qrc文件展开就能看到图片文件了
>  * */
> ```

## Dialog对话框

> ```c
>  //点击新建弹出对话框,triggered触发
>  connect(ui->actionnew,&QAction::triggered,this,[=](){
>      //对话框分类
>      //模态对话框（可以对其他窗口进行操作）非模态对话框（不能……）
>      //1、模态创建
>      //        QDialog dlg(this);
>      //        dlg.resize(200,100);
>      //        dlg.exec();
>  //        qDebug()<<"模态对话框弹出了";
> ```
>
>
> ```c
>  //2、非模态创建,要用指针，因为lambda表达式执行完就消失了，所以要用堆区创建对象
>  //        QDialog *dlg2 = new QDialog(this);
>  //        dlg2->resize(200,100);
>  //        dlg2->show();
>  //        dlg2->setAttribute(Qt::WA_DeleteOnClose);//关闭后释放堆区对象，否则一直点，叉掉只是不显示，并没有释放内存，可能导致内存泄漏
>  //        qDebug()<<"非模态窗口弹出了";
> 
>  //消息对话框
>  //1、错误对话框
>  //QMessageBox::critical(this,"错误","发生错误了");
> 
>  //2、信息对话框
>  //QMessageBox::information(this,"info","这是信息");
> 
>  //3、提问对话框 QMessageBox::Save|QMessageBox::Cancel是两个按钮类型，最后的参数是默认回车关联的按钮
> ```
>
> ```c
>  //        if(QMessageBox::Save == QMessageBox::question(this,"ques","是否保存？",QMessageBox::Save|QMessageBox::Cancel,QMessageBox::Cancel))
> //        {
> //            qDebug()<<"点击的是保存";
> //        }else{
> //            qDebug()<<"点击的是取消";
> //        }
>  //4、警告对话框
>  //QMessageBox::warning(this,"waring","警告！！！");
> 
>  //其他对话框
>  //1、颜色对话框
>     //        QColor color = QColorDialog::getColor(QColor(100,100,100));
> //        qDebug()<<"rgb="<<color.red()<<color.green()<<color.blue();
> //2、文件对话框,参数1：父亲；参数2：对话框标题；参数3：默认打开的路径；参数4：默认过滤条件
>  //返回值是打开的文件路径
>     //        QString str =   QFileDialog::getOpenFileName(this,"打开文件","C:\\Users\\onebot\\Desktop","(*.md)");
> //        qDebug()<<str;
> //3、字体对话框
>  bool flag;
>  QFont font =  QFontDialog::getFont(&flag,QFont("微软雅黑",16));
>  qDebug()<<font;
>  qDebug()<<"字体:"<<font.family().toUtf8().data()<<"字号:"<<font.pointSize()<<"是否加粗:"<<font.bold()<<"是否倾斜:"<<font.italic();
> ```

## ListWidget列表容器

> ```c
> //设置单选框默认为男
>  ui->rBtnMan->setChecked(true);//设置默认为未婚
> ui->rBtnNoMarry->setChecked(true);
> 
> //选中女后，打印信息
> connect(ui->rBtnWoman,&QRadioButton::clicked,this,[=](){
>  qDebug()<<"女";
> });
> 
> //ikun
> //stateChanged，state--状态 0->选中（1->半选）2->选中
> connect(ui->ngm,&QCheckBox::stateChanged,this,[=](int state){
>  qDebug()<<"你干嘛哈哈哎哟"<<state;
> });
> 
> connect(ui->baozha,&QCheckBox::clicked,this,[=](){
>  qDebug()<<"多一眼看一眼就会爆炸";
> });
> 
> connect(ui->ronghua,&QCheckBox::clicked,this,[=](){
>  qDebug()<<"近一点靠近点快被融化";
> });
> 
> connect(ui->rap,&QCheckBox::clicked,[=](){
>  qDebug()<<"唱跳rap篮球music";
> });
> 
> //使用QListWidget写一首诗
> ```
>
> ```c++
> //    QListWidgetItem*item = new QListWidgetItem("锄禾日当午");
> //    //把诗放到listWidget控件中
> //    ui->listWidget->addItem(item);
> //    item->setTextAlignment(Qt::AlignHCenter);
> //创建QStringList容器,一次性全部加进去
> QStringList list;
> list<<"锄禾日当午"<<"汗滴禾下土"<<"谁知盘中餐"<<"粒粒皆辛苦";
> ui->listWidget->addItems(list);
> ```

## TreeWidget树形目录

> ```c
> //treeWidget使用
> //设置水平头
> ui->treeWidget->setHeaderLabels(QStringList()<<"人物"<<"人物介绍");
> 
> QTreeWidgetItem*liItem = new QTreeWidgetItem(QStringList()<<"力量");
> QTreeWidgetItem*minItem = new QTreeWidgetItem(QStringList()<<"敏捷");
> QTreeWidgetItem*zhiItem = new QTreeWidgetItem(QStringList()<<"智力");
> 
> ui->treeWidget->addTopLevelItem(liItem);
> ui->treeWidget->addTopLevelItem(minItem);
> ui->treeWidget->addTopLevelItem(zhiItem);
> 
> //创建子节点
> QTreeWidgetItem *l1 = new QTreeWidgetItem(QStringList()<<"坤"<<"你干嘛哈哈哎哟");
> liItem->addChild(l1);
> ```

## TableWidget表格容器

> ```c
> //TableWidget控件
> //设置列数
> ui->tableWidget->setColumnCount(3);
> //设置水平表头
> ui->tableWidget->setHorizontalHeaderLabels(QStringList()<<"姓名"<<"性别"<<"年龄");
> 
> //设置行数
> ui->tableWidget->setRowCount(5);
> 
> //设置正文
> //    ui->tableWidget->setItem(0,0,new QTableWidgetItem("坤"));
> QStringList  nameList ;
> nameList<<"张三"<<"李四"<<"王五"<<"鲲鲲"<<"小黑子";
> 
> QStringList  sexList ;
> sexList<<"男"<<"女"<<"男"<<"女"<<"男";
> 
> for(int i=0;i<5;i++){
>  int col=0;
>  ui->tableWidget->setItem(i,col++,new QTableWidgetItem(nameList[i]));
>  ui->tableWidget->setItem(i,col++,new QTableWidgetItem(sexList.at(i)));
>  //int 转 QString
>  ui->tableWidget->setItem(i,col++,new QTableWidgetItem(QString::number(i+18)));
> }
> ```

## 栈控件、下拉框、标签动图

> ```c++
> //1、栈控件使用
> //设置默认显示页面
> ui->stackedWidget->setCurrentIndex(0);
> 
> //设置滚动页面
> connect(ui->btn_sroll,&QPushButton::clicked,this,[=](){
>  ui->stackedWidget->setCurrentIndex(0);
> });
> 
> //设置网页页面
> connect(ui->btn_Web,&QPushButton::clicked,this,[=](){
>  ui->stackedWidget->setCurrentIndex(1);
> });
> 
> //设置工具箱页面
> connect(ui->btn_toolBox,&QPushButton::clicked,this,[=](){
>  ui->stackedWidget->setCurrentIndex(2);
> });
> 
> //2、下拉框
> ui->comboBox->addItem("奔驰");
> ui->comboBox->addItem("宝马");
> ui->comboBox->addItem("拖拉机");
> //点击按钮选中拖拉机选项
> connect(ui->btn_tlj,&QPushButton::clicked,this,[=](){
> //        ui->comboBox->setCurrentIndex(2);
>      ui->comboBox->setCurrentText("拖拉机");
>  });
> //3、使用QLabel显示图片
> //    ui->label->setPixmap(QPixmap(":/html.svg"));
> //显示动图
> QMovie * movie = new QMovie(":/kun.gif");
> ui->label->setMovie(movie);
> //播放动图
> movie->start();
> ```
