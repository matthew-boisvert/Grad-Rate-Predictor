
from PredictorPackage import DataParser
from GraphicsPackage import Window
from GraphicsPackage import Canvas
from GraphicsPackage import MenuBar
from GraphicsPackage import PolicyDisplay

policy_list = DataParser.generatePolicyList("./data/PolicyData.csv")
demographic_list = DataParser.generateDemographicsList("./data/DemographicsData.csv")

window = Window.Window(demographic_list, policy_list)
canvas = Canvas.Canvas(window.frameObj, demographic_list[0])
menu = MenuBar.MenuBar(window.frameObj)
window.windowObj.config(menu=menu.menuObj)
policyDisplay = PolicyDisplay.PolicyDisplay(window.frameObj, policy_list, canvas.canvasObj)

window.windowObj.mainloop()