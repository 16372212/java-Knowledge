## spring是什么

spring是一个轻量级的【控制反转】IOC和【面向切面】的AOP【容器】【框架】。
    ioc: 松耦合
    面向切面：分离业务逻辑与系统服务，增强内聚性
    包括并管理bean的配置与生命周期（容器
    将简单的组建配置、组合成复杂的应用（框架

## Spring IOC

控制反转 inverse of control. 设计思想：Spring框架负责控制对象的创建（实例化）。可以实现【容器】【依赖注入】【控制反转】

举例：实际项目中，一个Service类可能依赖很多其他的类，假如要实例化这个类，可能要搞清楚这个Service所有底层类的构造函数。而现在只要配置好/注解，直接引用即可。IO负责实例化。


### 怎么实现的

1. 【找到反射解析】：找到所有含有@bean, @service注解的类，通过反射解析类及其类的各种信息（构造器、方法及参数）。
2. 【封装bean放map构造】IOC容器将其封装成bean定义信息类、constructor信息类、method信息类、property信息类，最终放在一个map里，这个map就是container. 需要这个bean的时候，IOC框架就从container中找到这个类，然后通过构造器new出来，实现控制反转。
3. 【依赖注入/递归注入】：再在这个类中找到是否有@autowired属性，有就递归注入（从container中找到对应的解析类，new出对象。然后信息类中的setter方法注入这个解析类。）


同时可以简单实现单例模式singleton或者多例模式prototype:
`<bean id="hi" class="com.test.Hi" init-method="init" scope="singleton">`
- 如果bean的scope是singleton，那么会重用这个bean而不被创建。将bean放到一个map里。
- 如果bean的scope是session, bean会放到session里。


## Spring的AOP

面向切面编程。让与业务无关，将（事务处理、日志管理、控制权限等）封装成切面，注入到目标对象中（具体的业务逻辑）。便于减少系统的重复代码。

## bean

被IOC容器管理的对象。

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