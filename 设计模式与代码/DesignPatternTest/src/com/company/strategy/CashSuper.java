package com.company.strategy;

/**
 * 抽象类中不一定包含抽象方法，但是有抽象方法的类必定是抽象类。抽象类中的抽象方法只是声明，不包含方法体，就是不给出方法的具体实现也就是方法的具体功能。
 */
abstract class CashSuper {
    public abstract double acceptCash(double money);
}

/**
 * 正常策略
 */
class CashNormal extends CashSuper{
    public double acceptCash(double money){
        return money;
    }
}

/**
 * 打折策略
 */
class CashRebate extends CashSuper{

    private double moneyRebate = 1d;

    public CashRebate(String mon){
        moneyRebate = Double.parseDouble(mon);
    }
    public double acceptCash(double money){
        return money * moneyRebate;
    }
}

/**
 * 反利策略
 */
class CashReturn extends CashSuper{

    private double moneyCondition = 0.0d;
    private double moneyReturn = 0.0d;

    public CashReturn(String moneyCondition, String moneyReturn){
        this.moneyCondition = Double.parseDouble(moneyCondition);
        this.moneyReturn = Double.parseDouble(moneyReturn);
    }

    public double acceptCash(double money){
        if(money > moneyCondition){
            return money + moneyReturn;
        }else{
            return money;
        }
    }
}


/**
 * 这里设置一个工厂，需要满足即能打折，又可以反利.
 * 工厂的意义就在于根据条件返回一个具体的子类。所以客户端需要使用factory.createCash方法，同时又要用CashSuper方法中的getResult。
 * 但是策略模式可以让客户端只用到一个类CashContext就可
 *
 */
class CashFactory{
    public static CashSuper createCashAccept(String type){
        CashSuper cs = null;
        switch (type){
            case "正常收费":
                cs = new CashNormal();
                break;
            case "打折":
                cs = new CashRebate("0.8");
                break;
            case "满300返10":
                cs = new CashReturn("300", "10");
                break;
        }
        return cs;
    }
}


/**
 * 结合工厂的方法。获得了这个类并且直接在这个类中执行获得类的该方法。让客户端只需要同这一个类交互即可
 */
class CashContext{
    private CashSuper cs = null;

    public CashContext(String type){

        switch (type){
            case "正常收费":
                cs = new CashNormal();
                break;
            case "打折":
                cs = new CashRebate("0.8");
                break;
            case "满300返10":
                cs = new CashReturn("300", "10");
                break;
        }
    }

    public double GetResult(double money){
        return cs.acceptCash(money);
    }
}


class Main{
    public static void main(String args[]){
        // CashSuper cashSuper = CashFactory.createCashAccept("打折");

    }
}