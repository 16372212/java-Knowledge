# ps

进程的瞬间信息

-a 不与terminal有关的所有进程

-A 所有的进程均显示出来，与 -e 具有同样的效用；

l 较长、较详细的将该PID 的的信息列出；(UID   PID  PPID CPU PRI NI)

j 工作的格式 (jobs format)(USER         PID  PPID  PGID   SESS JOBC STAT   TT       TIME COMMAND)

-p 52663： pid为52663的信息

-l 列出当前登陆的所有PID: 

axu 目前所有正在运行的程序
    VSZ: 占虚存的量
    RSS: 占固定内存量
    STAT: R正运行，S睡眠，T停止or侦测。Z:程序已经终止，但父进程无法正常终止

> 僵尸进程：子进程先于父进程挂掉 但是父进程并没有正确回收子进程的资源

`ps -A -ostat,ppid,pid,cmd | grep -e '^[Zz]'`

`ps aux | grep Z`
-o 自定义输出字段，我们设定显示字段为stat（状态），ppid（父进程pid），pid（进程pid），cmd（命令行）这四个参数

grep 抓取stat 状态为zZ进程

    一个进程在调用exit命令结束自己的生命的时候，其实它并没有真正的被销毁， 而是留下一个称为僵尸进程（Zombie）的数据结构。直到父进程通过wait回收他。

    占用了内存资源. 

僵尸进程杀死方法：

    1. 用signal函数为SIGCHLD安装handler，因为子进程结束后，父进程会收到该信号，可以在handler中调用wait回收

    2. 将子进程成为孤儿进程，从而其的父进程变为init进程，通过init进程可以处理僵尸进程

    3. 父进程通过wait和waitpid等函数等待子进程结束，这会导致父进程挂起。

