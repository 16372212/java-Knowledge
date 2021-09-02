package com.company.strategy;

/**
 * 用来作为策略类的公共接口。并希望可以同时满足多个策略
 */

abstract class Strategy {
    public abstract void AlgorithmInterface();
}

class ConcretStrategyA extends Strategy{
    public void AlgorithmInterface(){
        System.out.println("算法A实现");
    }
}

class ConcretStrategyB extends Strategy{
    public void AlgorithmInterface(){
        System.out.println("算法B实现");
    }
}

class Context{
    Strategy strategy;
    public Context(Strategy strategy){
        this.strategy = strategy;
    }

    public void ContextInterface(){
        strategy.AlgorithmInterface();
    }
}

class MainStrategy{
    public static void main(String[] args){
        Context context;
        context = new Context(new ConcretStrategyA());
        context.ContextInterface();

        context = new Context(new ConcretStrategyB());
        context.ContextInterface();
    }
}


