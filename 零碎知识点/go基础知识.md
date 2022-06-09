
一旦 main 函数执行完毕并返回，所有的 goroutine 都会被强制结束。所以在本文测试一些代码时，不要忘记使用 time.Sleep(...) 或者 func{} 将主 goroutine 挂起或另其空转。

