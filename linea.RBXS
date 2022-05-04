local TweenService = game:GetService("TweenService")
local linea = script.Parent

local velocidad = linea:GetAttribute("velocidad")
local texture = linea.Texture

linea.AssemblyLinearVelocity = linea.CFrame.LookVector * velocidad

linea:GetAttributeChangedSignal("velocidad"):Connect(function()
	linea.AssemblyLinearVelocity = linea.CFrame.LookVector * linea:GetAttribute("velocidad")
end)

local info = TweenInfo.new(60, Enum.EasingStyle.Linear, Enum.EasingDirection.In, -1)
local tween = TweenService:Create(texture, info, {OffsetStudsV=-300})
tween:Play()
