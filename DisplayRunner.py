import Demographic
import Policy
import Window
import Canvas
import MenuBar
import PolicyDisplay



policy_list = [Policy.Policy("Policy X"), Policy.Policy("Policy Y"), Policy.Policy("Policy Z")]
demographic_list = []
demographic_list.append(Demographic.Demographic("First-Generation Students", 0.50))
demographic_list.append(Demographic.Demographic("First-Gen Students With Less Than X Financial Aid", 0.2, "finance"))
demographic_list.append(Demographic.Demographic("First-Gen Students With More Than X Financial Aid", 0.7, "finance"))

window = Window.Window(demographic_list, policy_list)
canvas = Canvas.Canvas(window.frameObj, demographic_list[0])
menu = MenuBar.MenuBar(window.frameObj)
window.windowObj.config(menu=menu.menuObj)
policyDisplay = PolicyDisplay.PolicyDisplay(window.frameObj, policy_list, canvas.canvasObj)

window.windowObj.mainloop()

