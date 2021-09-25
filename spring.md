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
-request: 每个HTTP创建一个新的bean, bean支队当前http request内有效
-session：每一次来自新session的http请求都会产生一个新的bean, bean仅在当前http session内有效
-global-session：全局session作用域。


### Spring的Bean生命周期

1. Bean容器找到配置文件中Spring Bean的定义。
2. Bean容器利用java reflection API创建一个Bean的实例。
3. 利用set()设置属性值
4. 如果Bean实现了BeanNameAware接口，调用setBeanName()方法，传入Bean的名字。
5. 如果Bean实现了BeanClassLoaderAware接口，调用setBeanClassLoader()方法可以传入ClassLoader对象的实例。
6. 如果Bean实现了其他*.Aware接口，就调用相应的方法
7. 如果Bean实现了InitializingBean接口，执行afterPropertiesSet()方法
8. 如果Bean在配置文件中定义包含init-method属性，执行指定方法。
9. 销毁Bean的时候，如果Bean实现了DisposableBean接口，执行destroy方法
10. 销毁Bean的时候，如果Bean在配置文件中的定义包含destroy-method属性，执行指定的方法。



## SpringMVC的请求流程
model, view, controll

1. 客户端发送请求到dispatcherServlet.
2. dispatcherServlet根据请求信息调用HandlerMapping, 解析请求对应的Handler
3. 解析后由HandlerAdapter适配器处理
4. HandlerAdapter根据Handler调用真正的处理器，处理相应的业务逻辑
5. 处理器完成业务后，返回一个ModelAndView对象。model是返回的数据对象，view是逻辑上的view
6. 根据逻辑view找到实际view, 然后把返回的model传递给view, 将view返回给请求者。

## Spring的动态代理

## Spring中有个@Autowire，讲讲

## List和Set的区别

## Spring的动态代理讲讲

## Java线程池大概有哪几种？AQS有了解过嘛？