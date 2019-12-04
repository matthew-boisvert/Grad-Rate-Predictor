import Demographic
import Policy
import Window
import Canvas
import MenuBar
import PolicyDisplay
import DataParser

policy_list = DataParser.generatePolicyList("PolicyData.csv")
demographic_list = DataParser.generateDemographicsList("DemographicsData.csv")

window = Window.Window(demographic_list, policy_list)
canvas = Canvas.Canvas(window.frameObj, demographic_list[0])
menu = MenuBar.MenuBar(window.frameObj)
window.windowObj.config(menu=menu.menuObj)
policyDisplay = PolicyDisplay.PolicyDisplay(window.frameObj, policy_list, canvas.canvasObj)

window.windowObj.mainloop()