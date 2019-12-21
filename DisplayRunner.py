
from src.PredictorPackage import DataParser
from src.GraphicsPackage import Window
from src.GraphicsPackage import Canvas
from src.GraphicsPackage import MenuBar
from src.GraphicsPackage import PolicyDisplay

policy_list = DataParser.generatePolicyList("./src/data/PolicyData.csv")
demographic_list = DataParser.generateDemographicsList("./src/data/DemographicsData.csv")

window = Window.Window(demographic_list, policy_list)
canvas = Canvas.Canvas(window.frameObj, demographic_list[0])
menu = MenuBar.MenuBar(window.frameObj)
window.windowObj.config(menu=menu.menuObj)
policyDisplay = PolicyDisplay.PolicyDisplay(window.frameObj, policy_list, canvas.canvasObj)

window.windowObj.mainloop()