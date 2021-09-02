package com.company.factory;

public class Operation {

    private double _numberA = 0;
    private double _numberB = 0;
    public double getNumberA(){
        return _numberA;
    }
    public void setNumberA(double numberA){
        _numberA = numberA;
    }

    public double getNumberB(){
        return _numberB;
    }
    public void setNumberB(double numberB){
        _numberB = numberB;
    }

    public double getResult(){
        return 0;
    }

    private double getResult(double numberA, double numberB, String operate){
        double result = 0d;
        switch (operate){
            case "+":
                result = numberA + numberB;
                break;
            case "-":
                result = numberA - numberB;
                break;
        }
        return result;
    }


}

class OperationAdd extends Operation{
    public double getResult(){
        // 除了用static、final、private修饰之外的所有方法都是虚方法。
        return getNumberA() + getNumberB();
    }
}

class OperationSub extends Operation{
    public double getResult(){
        return getNumberA() - getNumberB();
    }
}

class Main{
    public static void main(String args[]){
        try{
            Operation oper = OperationFactory.createOperate("+");
            oper.setNumberA(1d);
            oper.setNumberB(2d);
            System.out.print(oper.getResult());
        }catch( Exception e){
            System.console().writer().print(e.getMessage());
        }
    }
}