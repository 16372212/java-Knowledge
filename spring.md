## Spring IOC

控制反转 inverse of control. 设计思想。Spring框架负责控制对象的创建（实例化）

举例：实际项目中，一个Service类可能依赖很多其他的类，假如要实例化这个类，可能要搞清楚这个Service所有底层类的构造函数。而现在只要配置好/注解，直接引用即可。IO负责实例化。

## Spring的AOP

面向切面编程。让与业务无关，却为业务模块所共同调用的逻辑或责任封装起来（事务处理、日志管理、控制权限等）。便于减少系统的重复代码。

## bean

被IOC容器管理的对象。

@Component作用于类，通过类路径扫描来自动侦测并装配到Spring容器。@Bean作用于方法，告诉这是某个类的实例。


### bean作用域
-singleton: bean都是单例的，只有一个实例
-prototype: 每个请求创建一个新实例
-request: 每个HTTP创建一个新的bean, bean只对当前http request内有效
-session：每一次来自新session的http请求都会产生一个新的bean, bean仅在当前http session内有效
-global-session：全局session作用域。


### Spring的Bean生命周期

1. 解析类得到beanDefinition
2. 确定构造方法
3. 实例化得到对象
4. 对象中的属性进行填充（@Autoired注解的）
5. 回调Aware方法，比如BeanNameAware，BeanFactoryAware（Aware为了能够感知到自身的一些属性。）
6. 调用BeanPostProcessor的初始化前的方法
7. 调用初始化方法
8. AOP
9. 调用Bean
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