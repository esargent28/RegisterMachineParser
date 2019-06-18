from register_machine import RegisterMachine


def TestAdditionMachine():

    print("  --> Testing addiiton...", end=' ')
    additionMachine = RegisterMachine('examples/addition.txt')

    res1 = additionMachine.run(10, 11)
    res2 = additionMachine.run(0, 10)
    res3 = additionMachine.run(11037, 0)
    res4 = additionMachine.run(0, 0)
    res5 = additionMachine.run(11037, 11037)

    assert(len(res1) == 1 and res1[0] == 21)
    assert(len(res2) == 1 and res2[0] == 10)
    assert(len(res3) == 1 and res3[0] == 11037)
    assert(len(res4) == 1 and res4[0] == 0)
    assert(len(res5) == 1 and res5[0] == 2*11037)

    print("Done!")


def runTests():
    print("Running register machine tests...")
    TestAdditionMachine()
    print("Done")

runTests()
