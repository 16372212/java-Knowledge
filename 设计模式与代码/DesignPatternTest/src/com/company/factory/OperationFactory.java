package com.company.factory;

import com.company.factory.Operation;
import com.company.factory.OperationAdd;
import com.company.factory.OperationSub;

public class OperationFactory {
    public static Operation createOperate(String operate) {
        Operation oper = null;
        switch (operate) {
            case "+":
                oper = new OperationAdd();
                break;
            case "-":
                oper = new OperationSub();
                break;
        }
        return oper;
    }
}
