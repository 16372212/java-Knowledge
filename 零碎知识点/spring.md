## spring是什么

spring是一个轻量级的开发框架。支持【控制反转】IOC和【面向切面】的AOP【容器】【框架】。
    ioc: 松耦合
     
    面向切面：分离业务逻辑与系统服务，增强内聚性
    包括并管理bean的配置与生命周期（容器
    将简单的组建配置、组合成复杂的应用（框架

Spring的核心：提供了一个IoC容器，它可以管理所有轻量级的JavaBean组件。提供的底层服务包括组件的生命周期管理、配置和组装服务、AOP支持，以及建立在AOP基础上的声明式事务服务等。

思想：不重新造轮子，开箱即用

## SpringMVC

Spring MVC是一个Java框架，用于构建Web应用程序。它遵循Model-View-Controller设计模式。它实现了核心Spring框架的所有基本功能，例如控制反转，依赖注入。Spring MVC通过 `DispatcherServlet` 这个类来接收传入的请求并将其映射到正确的资源，例如控制器，模型和视图。

- model: 应用程序的数据，单个对象或对象的集合。

- view:视图以特定格式表示所提供的信息

- controller:包含应用程序的业务逻辑


其核心思想是通过将业务逻辑、数据、显示分离来组织代码。


## SpringBoot
SpringBoot就是在Spring的基础上减少了很多配置文件，开箱即用。 Spring如果想要实现其特性，需要用 XML 或 Java 进行显式配置。

## 其他一些名词：

a) 容器：运行组件的*软件环境*。提供【运行环境】或【底层服务】 

例如，Tomcat就是一个Servlet容器，它可以为Servlet的运行提供运行环境；类似Docker这样的软件也是一个容器，它提供了必要的Linux环境以便运行一个特定的Linux进程。

同时Servlet容器底层实现了TCP连接，解析HTTP协议等非常复杂的服务，容器可以提供这些服务。

b) Servlet：可以提供http请求和响应的模块。提供了一个Spring MVC Web框架实现。

c) 事物


## Spring流程



## Spring IOC

控制反转 inverse of control. 设计思想：Spring框架负责控制对象的实例化和初始化，控制对象之间的依赖关系。Java对象就是Spring Bean


[举例]：实际项目中，一个Service类S可能依赖于类A, B, C，假如要实例化这个类S，也需要分别实例化ABC。这就增加了代码之间的耦合性。

- 一些组件需要被销毁以释放资源，比如一个类B的实例需要被【销毁】，但如果该组件被多个【组件共享】，如何确保它的【使用方】都已经全部被销毁？
- 不利于业务扩展
- 测试某个组件是复杂的，因为必须要在真实的数据库环境下执行。

这样的话，组件的【生命周期】和【依赖关系】都是由组件自身维护的，大大增加了【耦合】程度。后续【测试】【维护】都不方便。

IOC后：组件由IOC容器负责。实例不需要程序员自己new出来，而是被容器注入进来。

[核心思想]：将组件的【创建】+【配置】与组件的【使用】相分离，IOC来管理组件的【生命周期】

IOC容器从XML中读取组件的【创建】和【配置】信息。

[使用方法]
1. 程序员通过xml配置文件或注解（@component）等对Bean定义。
2. Spring启动时根据配置自动创建对象并管理

依赖注入本质上是Spring Bean属性的一种。

[原理]
工厂模式、Java反射、XML解析
 
1. 把IOC容器当成一个工厂，生产各种Spring Bean
2. 容器启动时会从配置文件XML中加载各个对象的依赖关系。
3. IOC利用**反射**机制、在运行时根据根据类名生成对象（这样增加任意多个子类都不需要修改IOC容器类），并根据依赖关系将对象注入到依赖它的对象中。

        反射作用：
        1、在运行时判断任意一个对象所属的类；

        2、在运行时获取类的对象；

        3、在运行时访问java对象的属性，方法，构造方法等。

说的很清楚的一个博客：https://blog.csdn.net/fuzhongmin05/article/details/61614873




## Spring的AOP

面向切面编程。让与业务无关，将（事务处理、日志管理、控制权限等）封装起来形成可以重用的组件，注入到目标对象中（具体的业务逻辑）。便于减少系统的重复代码。

## bean

被IOC容器管理的对象。


Bean属性注入：

    1）带参构造函数注入（将要注入的属性或Bean作为构造器的参数） 
    2）setter注入（无参构造函数，然后通过反射机制调用setXxx（）方法）


> 默认Bean都是单例的，也可以修改，在bean中配置scope属性：prototype or singleton


@Component作用于类，通过类路径扫描来自动侦测并装配到Spring容器。@Bean作用于方法，告诉这是某个类的实例。


### bean作用域scope
-singleton: bean都是单例的，只有一个实例
-prototype: 每个请求创建一个新实例
-request: 每个HTTP创建一个新的bean, bean只对当前http request内有效
-session：每一次来自新session的http请求都会产生一个新的bean, bean仅在当前http session内有效
-global-session：全局session作用域。


### Spring的Bean生命周期

实例化：
1. 解析类得到beanDefinition
2. 确定构造方法
3. 实例化得到对象
属性赋值：
4. 对象中的属性进行填充（@Autoired注解的）
5. 回调Aware方法，比如BeanNameAware，BeanFactoryAware（Aware为了能够感知到自身的一些属性。）
初始化：
6. 调用BeanPostProcessor的初始化前的方法
7. 调用初始化方法
8. 调用BeanPostProcessor的初始化后的的方法，这里进行AOP
9. 如果bean是单例，会放到单例池。 使用bean
销毁：
10. Spring容器关闭时，使用DisposableBean中的destory()方法

（类的生命周期：家宴准备了西式菜：加载，验证，准备，解析，初始化。）


## SpringMVC的请求流程

SpringMVC （定义了url到handle的映射，将handle结果使用视图解析技术生成视图展现给前端）

model, view, controll

适配请求：根据用户的request请求，tomcat服务器找到对应的handler
1. 客户端发送请求到dispatcherServlet.
2. dispatcherServlet根据请求信息调用HandlerMapping, 解析请求对应的Handler
3. 解析后由HandlerAdapter适配器处理

根据handler调用真正的处理器，处理相应的业务逻辑
4. HandlerAdapter根据Handler调用真正的处理器，处理相应的业务逻辑

处理结束后，将结果进行视图解析，然后返回给前端
5. 处理器完成业务后，返回一个ModelAndView对象。model是返回的数据对象，view是逻辑上的view
6. 根据逻辑view找到实际view, 然后把返回的model传递给view, 将view返回给请求者。

## Spring的动态代理

## Spring中有个@Autowire，讲讲

## List和Set的区别

## Spring的动态代理讲讲

## Java线程池大概有哪几种？AQS有了解过嘛？


项目开始时MS SQL开发的，后来有的另外的客户要求用Oracle数据库。如何应对需求变更？

软件中考虑这个问题，那么在设计过程中需要哪些工作

回答：

首先当遇到需求变更时，首先，不仅要了解两种数据库的特征，还要先了解到背后蕴藏的原因：

MS SQL与Oracle数据库的架构、优势和适用场景不同，意味着背后客户对于数据的要求以及其数据特征不同。Oracle的数据文件包括：控制文件、数据文件、重做日志文件、参数文件、归档文件、密码文件。这是根据文件功能行进行划分，并且所有文件都是二进制编码后的文件，对数据库算法效率有极大的提高。而SQL Server的数据架构基本是纵向划分，分为：Protocol Layer（协议层）， Relational Engine（关系引擎）， Storage Engine（存储引擎）。因此，MS SQL Server主要面向中小企业。其最大的优势就是在于集成了MS公司的各类产品及资源，提供了强大的可视化界面、高度集成的管理开发工具，在快速构建商业智能（BI）方面颇有建树。因此它们的适用环境不同：Oracle的应用，主要在传统行业的数据化业务中，比如：银行、金融这样的对可用性、健壮性、安全性、实时性要求极高的业务；而MS SQL是windows生态系统的产品，虽然它有一个高度的集成化，且可以享受微软提供的整套的软件方案，因此适合对于IT需求要求不大且资金较充足的企业。例如，自建ERP系统、商业智能、垂直领域零售商、餐饮、事业单位等等。

其次，根据客户需求确定未来两种数据库的选型方案：如果客户对安全性、实时性有一个很大的要求，且留给整个团队的开发时间也非常充裕，那么就可以只保留Oracle数据库。先将数据全部从MS SQL中迁移到Oracle中。再修改涉及到的业务逻辑，最后上线产品。但如果客户的数据体量很大，且留给团队的开发时间非常有限，那么为了节省开发和时间成本，可以先让系统同时支持这两种数据库，即使用MS SQL的旧版本代码和使用Oracle的新版本代码，当有新的数据来且没有在新版本中命中数据，但在老版本中命中时，再采用懒加载的方式将该段数据从MS SQL迁移至Oracle。使用离线的数据迁移方式结合同时支持新旧两种版本的业务支持，可以在短时间内满足用户需求，还保证了系统的稳定性和可用性。

技术选型之后就可以着手调研数据迁移的方式了：
将SQLServer数据库中的表和数据全量导入到Oracle数据库可以通过Microsoft SqlServer Management Studio工具，直接导入到oracle数据库，这免去了生成脚本的步骤。



SQL Server 迁移核心特性
SQL Developer 从 Microsoft SQL Server 进行迁移时支持以下核心特性：

自动将列数据类型转换成相应的 Oracle 数据类型。
自动解决对象名冲突，例如，与 Oracle 保留字的冲突。
分析 T-SQL 存储过程、函数、触发器以及视图并将其转换为 Oracle PL/SQL。
提供了高级自定义功能，如更改数据类型映射以及删除并重新命名对象。
生成有关迁移状态的报告。
生成创建目标 Oracle 数据库的 DDL 脚本。
生成数据移动脚本。
在 Progress 窗口中显示有关迁移的信息、错误和警告消息。





