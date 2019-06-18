from register_machine import RegisterMachine


def testAdditionMachine():

    print("  --> Testing addiiton...", end=' ')
    additionMachine = RegisterMachine('examples/addition.txt')

    def testResult(x, y):
        res = additionMachine.run(x, y)
        assert(len(res) == 1 and res[0] == x + y)

    for i in range(100):
        for j in range(i, 100):
            testResult(i, j)

    print("Done!")


def testMultiplicationMachine():

    print("  --> Testing multiplication...", end=' ')
    multiplicationMachine = RegisterMachine('examples/multiplication.txt')

    def testResult(x, y):
        res = multiplicationMachine.run(x, y)
        assert(len(res) == 1 and res[0] == x * y)

    for i in range(50):
        for j in range(i, 50):
            testResult(i, j)

    print("Done!")


def runTests():
    print("Running register machine tests...")
    testAdditionMachine()
    testMultiplicationMachine()
    print("Done")

runTests()
