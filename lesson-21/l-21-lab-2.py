class Tool:
    def __init__(self) -> None:
        self.durability = 100

    def action(self):
        self.durability -= 10


class Saw(Tool):
    def __init__(self) -> None:
        super().__init__()

    def action(self):
        super().action()
        print(self.durability)
        print('Saw is action')


class Axe(Tool):
    def __init__(self) -> None:
        super().__init__()

    def action(self):
        super().action()
        print(self.durability)
        print('Axe is action')


class Robot():
    def __init__(self, tool: Tool = None) -> None:
        self.tool = tool

    def setup_tool(self, tool):
        self.tool = tool

    def drop_tool(self):
        self.tool = None

    def action(self):

        if self.tool:
            if self.tool.durability > 0:
                self.tool.action()
            else:
                self.drop_tool()
                print('Тооl is dropped')
        else:
            print('No tool')


tool = Tool()

saw = Saw()
axe = Axe()

# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()
# saw.action()

# axe.action()
# axe.action()

robot = Robot()

robot.setup_tool(axe)

robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()

robot.setup_tool(saw)

robot.action()
robot.action()
