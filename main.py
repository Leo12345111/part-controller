function sandbox(var,func)
	local env = getfenv(func)
	local newenv = setmetatable({},{
		__index = function(self,k)
			if k=="script" then
				return var
			else
				return env[k]
			end
		end,
	})
	setfenv(func,newenv)
	return func
end
cors = {}

local TORNADO_GROUP = "TornadoParts"
pcall(function()
	game:GetService("PhysicsService"):RegisterCollisionGroup(TORNADO_GROUP)
	game:GetService("PhysicsService"):CollisionGroupSetCollidable(TORNADO_GROUP, TORNADO_GROUP, false)
end)

local LocalScript17 = Instance.new("LocalScript")
LocalScript17.Name = "TornadoUI"
table.insert(cors, sandbox(LocalScript17, function()
	local player = game:GetService("Players").LocalPlayer
	local playerGui = player:WaitForChild("PlayerGui")
	local runService = game:GetService("RunService")

	if playerGui:FindFirstChild("TornadoUI") then
		playerGui.TornadoUI:Destroy()
	end

	local gui = Instance.new("ScreenGui", playerGui)
	gui.Name = "TornadoUI"
	gui.ResetOnSpawn = false 

	local frame = Instance.new("Frame", gui)
	frame.Size = UDim2.new(0, 250, 0, 310) 
	frame.Position = UDim2.new(0.5, -125, 0.5, -155)
	frame.BackgroundColor3 = Color3.fromRGB(35, 35, 35)
	frame.Active = true
	frame.Draggable = true

	local title = Instance.new("TextLabel", frame)
	title.Size = UDim2.new(1, -30, 0, 30)
	title.Text = "System Control"
	title.TextColor3 = Color3.fromRGB(255, 255, 255)
	title.BackgroundTransparency = 1
	title.Font = Enum.Font.SourceSansBold
	title.TextSize = 18

	local closeBtn = Instance.new("TextButton", frame)
	closeBtn.Size = UDim2.new(0, 30, 0, 30)
	closeBtn.Position = UDim2.new(1, -30, 0, 0)
	closeBtn.Text = "X"
	closeBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
	closeBtn.BackgroundColor3 = Color3.fromRGB(200, 50, 50)
	closeBtn.BorderSizePixel = 0
	closeBtn.Font = Enum.Font.SourceSansBold
	closeBtn.TextSize = 16

	local speedLabel = Instance.new("TextLabel", frame)
	speedLabel.Size = UDim2.new(0.4, 0, 0, 30)
	speedLabel.Position = UDim2.new(0.05, 0, 0, 40)
	speedLabel.Text = "Spin Speed:"
	speedLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	speedLabel.BackgroundTransparency = 1
	speedLabel.Font = Enum.Font.SourceSansSemibold
	speedLabel.TextSize = 15
	speedLabel.TextXAlignment = Enum.TextXAlignment.Left

	local speedBox = Instance.new("TextBox", frame)
	speedBox.Size = UDim2.new(0.45, 0, 0, 30)
	speedBox.Position = UDim2.new(0.5, 0, 0, 40)
	speedBox.Text = "35"
	speedBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	speedBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	speedBox.BorderSizePixel = 0
	speedBox.Font = Enum.Font.SourceSans
	speedBox.TextSize = 16

	local modeLabel = Instance.new("TextLabel", frame)
	modeLabel.Size = UDim2.new(0.3, 0, 0, 30)
	modeLabel.Position = UDim2.new(0.05, 0, 0, 80)
	modeLabel.Text = "Mode:"
	modeLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	modeLabel.BackgroundTransparency = 1
	modeLabel.Font = Enum.Font.SourceSansSemibold
	modeLabel.TextSize = 16
	modeLabel.TextXAlignment = Enum.TextXAlignment.Left

	local modeBtn = Instance.new("TextButton", frame)
	modeBtn.Size = UDim2.new(0.55, 0, 0, 30)
	modeBtn.Position = UDim2.new(0.4, 0, 0, 80)
	modeBtn.Text = "Tornado ▼"
	modeBtn.BackgroundColor3 = Color3.fromRGB(70, 70, 70)
	modeBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
	modeBtn.BorderSizePixel = 0
	modeBtn.Font = Enum.Font.SourceSansBold
	modeBtn.TextSize = 14

	local dropList = Instance.new("Frame", frame)
	dropList.Size = UDim2.new(0.55, 0, 0, 60) 
	dropList.Position = UDim2.new(0.4, 0, 0, 110)
	dropList.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
	dropList.BorderSizePixel = 0
	dropList.Visible = false
	dropList.ZIndex = 10 

	local optTornado = Instance.new("TextButton", dropList)
	optTornado.Size = UDim2.new(1, 0, 0.5, 0)
	optTornado.Text = "Tornado"
	optTornado.BackgroundColor3 = Color3.fromRGB(60, 60, 60)
	optTornado.TextColor3 = Color3.fromRGB(255, 255, 255)
	optTornado.BorderSizePixel = 0
	optTornado.Font = Enum.Font.SourceSans
	optTornado.TextSize = 14
	optTornado.ZIndex = 10

	local optRing = Instance.new("TextButton", dropList)
	optRing.Size = UDim2.new(1, 0, 0.5, 0)
	optRing.Position = UDim2.new(0, 0, 0.5, 0)
	optRing.Text = "Ring"
	optRing.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	optRing.TextColor3 = Color3.fromRGB(255, 255, 255)
	optRing.BorderSizePixel = 0
	optRing.Font = Enum.Font.SourceSans
	optRing.TextSize = 14
	optRing.ZIndex = 10

	local tornadoSettings = Instance.new("Frame", frame)
	tornadoSettings.Size = UDim2.new(1, 0, 0, 120)
	tornadoSettings.Position = UDim2.new(0, 0, 0, 120)
	tornadoSettings.BackgroundTransparency = 1
	tornadoSettings.Visible = true

	local heightLabel = Instance.new("TextLabel", tornadoSettings)
	heightLabel.Size = UDim2.new(0.4, 0, 0, 30)
	heightLabel.Position = UDim2.new(0.05, 0, 0, 0)
	heightLabel.Text = "Max Height:"
	heightLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	heightLabel.BackgroundTransparency = 1
	heightLabel.Font = Enum.Font.SourceSansSemibold
	heightLabel.TextSize = 15
	heightLabel.TextXAlignment = Enum.TextXAlignment.Left

	local heightBox = Instance.new("TextBox", tornadoSettings)
	heightBox.Size = UDim2.new(0.45, 0, 0, 30)
	heightBox.Position = UDim2.new(0.5, 0, 0, 0)
	heightBox.Text = "120"
	heightBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	heightBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	heightBox.BorderSizePixel = 0
	heightBox.Font = Enum.Font.SourceSans
	heightBox.TextSize = 16

	local uWidthLabel = Instance.new("TextLabel", tornadoSettings)
	uWidthLabel.Size = UDim2.new(0.4, 0, 0, 30)
	uWidthLabel.Position = UDim2.new(0.05, 0, 0, 40)
	uWidthLabel.Text = "Upper Width:"
	uWidthLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	uWidthLabel.BackgroundTransparency = 1
	uWidthLabel.Font = Enum.Font.SourceSansSemibold
	uWidthLabel.TextSize = 15
	uWidthLabel.TextXAlignment = Enum.TextXAlignment.Left

	local upperWidthBox = Instance.new("TextBox", tornadoSettings)
	upperWidthBox.Size = UDim2.new(0.45, 0, 0, 30)
	upperWidthBox.Position = UDim2.new(0.5, 0, 0, 40)
	upperWidthBox.Text = "120"
	upperWidthBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	upperWidthBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	upperWidthBox.BorderSizePixel = 0
	upperWidthBox.Font = Enum.Font.SourceSans
	upperWidthBox.TextSize = 16

	local lWidthLabel = Instance.new("TextLabel", tornadoSettings)
	lWidthLabel.Size = UDim2.new(0.4, 0, 0, 30)
	lWidthLabel.Position = UDim2.new(0.05, 0, 0, 80)
	lWidthLabel.Text = "Lower Width:"
	lWidthLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	lWidthLabel.BackgroundTransparency = 1
	lWidthLabel.Font = Enum.Font.SourceSansSemibold
	lWidthLabel.TextSize = 15
	lWidthLabel.TextXAlignment = Enum.TextXAlignment.Left

	local lowerWidthBox = Instance.new("TextBox", tornadoSettings)
	lowerWidthBox.Size = UDim2.new(0.45, 0, 0, 30)
	lowerWidthBox.Position = UDim2.new(0.5, 0, 0, 80)
	lowerWidthBox.Text = "5"
	lowerWidthBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	lowerWidthBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	lowerWidthBox.BorderSizePixel = 0
	lowerWidthBox.Font = Enum.Font.SourceSans
	lowerWidthBox.TextSize = 16

	local ringSettings = Instance.new("Frame", frame)
	ringSettings.Size = UDim2.new(1, 0, 0, 120)
	ringSettings.Position = UDim2.new(0, 0, 0, 120)
	ringSettings.BackgroundTransparency = 1
	ringSettings.Visible = false 

	local rRadiusLabel = Instance.new("TextLabel", ringSettings)
	rRadiusLabel.Size = UDim2.new(0.4, 0, 0, 30)
	rRadiusLabel.Position = UDim2.new(0.05, 0, 0, 0)
	rRadiusLabel.Text = "Radius:"
	rRadiusLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	rRadiusLabel.BackgroundTransparency = 1
	rRadiusLabel.Font = Enum.Font.SourceSansSemibold
	rRadiusLabel.TextSize = 15
	rRadiusLabel.TextXAlignment = Enum.TextXAlignment.Left

	local rRadiusBox = Instance.new("TextBox", ringSettings)
	rRadiusBox.Size = UDim2.new(0.45, 0, 0, 30)
	rRadiusBox.Position = UDim2.new(0.5, 0, 0, 0)
	rRadiusBox.Text = "30"
	rRadiusBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	rRadiusBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	rRadiusBox.BorderSizePixel = 0
	rRadiusBox.Font = Enum.Font.SourceSans
	rRadiusBox.TextSize = 16

	local rThicknessLabel = Instance.new("TextLabel", ringSettings)
	rThicknessLabel.Size = UDim2.new(0.4, 0, 0, 30)
	rThicknessLabel.Position = UDim2.new(0.05, 0, 0, 40)
	rThicknessLabel.Text = "Thickness:"
	rThicknessLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
	rThicknessLabel.BackgroundTransparency = 1
	rThicknessLabel.Font = Enum.Font.SourceSansSemibold
	rThicknessLabel.TextSize = 15
	rThicknessLabel.TextXAlignment = Enum.TextXAlignment.Left

	local rThicknessBox = Instance.new("TextBox", ringSettings)
	rThicknessBox.Size = UDim2.new(0.45, 0, 0, 30)
	rThicknessBox.Position = UDim2.new(0.5, 0, 0, 40)
	rThicknessBox.Text = "10"
	rThicknessBox.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
	rThicknessBox.TextColor3 = Color3.fromRGB(255, 255, 255)
	rThicknessBox.BorderSizePixel = 0
	rThicknessBox.Font = Enum.Font.SourceSans
	rThicknessBox.TextSize = 16

	local currentMode = "Tornado"

	modeBtn.MouseButton1Click:Connect(function()
		dropList.Visible = not dropList.Visible
	end)

	optTornado.MouseButton1Click:Connect(function()
		currentMode = "Tornado"
		modeBtn.Text = "Tornado ▼"
		dropList.Visible = false
		tornadoSettings.Visible = true 
		ringSettings.Visible = false
	end)

	optRing.MouseButton1Click:Connect(function()
		currentMode = "Ring"
		modeBtn.Text = "Ring ▼"
		dropList.Visible = false
		tornadoSettings.Visible = false
		ringSettings.Visible = true 
	end)

	local toggleBtn = Instance.new("TextButton", frame)
	toggleBtn.Size = UDim2.new(0.9, 0, 0, 40)
	toggleBtn.Position = UDim2.new(0.05, 0, 0, 255)
	toggleBtn.Text = "System: OFF"
	toggleBtn.BackgroundColor3 = Color3.fromRGB(50, 150, 50)
	toggleBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
	toggleBtn.BorderSizePixel = 0
	toggleBtn.Font = Enum.Font.SourceSansBold
	toggleBtn.TextSize = 16
	toggleBtn.ZIndex = 1

	local isSystemActive = false
	local connection = nil
	local partsInTornado = {}

	local function stopSystem()
		isSystemActive = false
		toggleBtn.Text = "System: OFF"
		toggleBtn.BackgroundColor3 = Color3.fromRGB(50, 150, 50)
		
		if connection then
			connection:Disconnect()
			connection = nil
		end
		
		for part, data in pairs(partsInTornado) do
			if part and part.Parent then
				local bp = part:FindFirstChild("TornadoBP")
				if bp then bp:Destroy() end
				
				local bav = part:FindFirstChild("TornadoBAV")
				if bav then bav:Destroy() end
				
				part.CanCollide = data.originalCollide 
				part.CanQuery = data.originalQuery
				pcall(function()
					part:SetNetworkOwner(nil)
					part.CollisionGroup = "Default"
				end)
			end
		end
		partsInTornado = {}
	end

	local function startSystem()
		if isSystemActive then return end
		isSystemActive = true
		toggleBtn.Text = "System: ON"
		toggleBtn.BackgroundColor3 = Color3.fromRGB(200, 100, 0)
		
		task.spawn(function()
			while isSystemActive do
				local char = player.Character
				if char and char:FindFirstChild("HumanoidRootPart") then
					local root = char.HumanoidRootPart
					local sRange = 600 
					
					local spawnHeightLimit = 20
					if currentMode == "Tornado" then
						spawnHeightLimit = tonumber(heightBox.Text) or 100
					elseif currentMode == "Ring" then
						spawnHeightLimit = 0 
					end

					local grabbedThisCycle = 0
					local maxGrabsPerCycle = 8

					for _, v in pairs(workspace:GetDescendants()) do
						if grabbedThisCycle >= maxGrabsPerCycle then break end
						
						if v:IsA("BasePart") then
							if not v.Anchored and not v:IsDescendantOf(char) then
								local dist = (v.Position - root.Position).Magnitude
								
								if dist <= sRange and not partsInTornado[v] then
									
									local isAttachedToPlayer = false
									for _, connectedPart in pairs(v:GetConnectedParts()) do
										if connectedPart:IsDescendantOf(char) then
											isAttachedToPlayer = true
											break
										end
									end
									
									if not isAttachedToPlayer then
										pcall(function()
											v:BreakJoints()
											v:SetNetworkOwner(player)
											v.CollisionGroup = "TornadoParts"
										end)
										
										local bp = Instance.new("BodyPosition")
										bp.Name = "TornadoBP"
										
										local partMass = v:GetMass()
										local forceLimit = partMass * 50000 
										bp.MaxForce = Vector3.new(forceLimit, forceLimit, forceLimit)
										
										bp.P = 40000 + (partMass * 3000) 
										bp.D = 6000 
										
										bp.Parent = v
										
										local bav = Instance.new("BodyAngularVelocity")
										bav.Name = "TornadoBAV"
										bav.MaxTorque = Vector3.new(math.huge, math.huge, math.huge)
										bav.AngularVelocity = Vector3.new(math.random(-15, 15), math.random(-15, 15), math.random(-15, 15))
										bav.Parent = v
										
										local pClearance = v.Size.Magnitude / 2
										
										partsInTornado[v] = {
											angle = math.random(1, 360),
											height = math.random(0, spawnHeightLimit), 
											radiusMultiplier = math.random(40, 100) / 100, 
											originalCollide = v.CanCollide,
											originalQuery = v.CanQuery,
											clearance = pClearance,
											upwardSpeed = math.random(40, 120) / 100,
											spinModifier = math.random(60, 140) / 100
										}
										
										v.CanQuery = false
										
										grabbedThisCycle = grabbedThisCycle + 1
									end
								end
							end
						end
					end
				end
				task.wait(0.05) 
			end
		end)
		
		connection = runService.Heartbeat:Connect(function()
			local char = player.Character
			if not char or not char:FindFirstChild("HumanoidRootPart") then return end
			local root = char.HumanoidRootPart
			
			local groundY = root.Position.Y - 3
			local rayParams = RaycastParams.new()
			rayParams.FilterDescendantsInstances = {char}
			rayParams.FilterType = Enum.RaycastFilterType.Exclude
			
			local rayResult = workspace:Raycast(root.Position, Vector3.new(0, -500, 0), rayParams)
			if rayResult then
				groundY = rayResult.Position.Y
			end
			
			local speed = tonumber(speedBox.Text) or 35

			for part, data in pairs(partsInTornado) do
				if part.Parent and not part.Anchored then
					
					part.CanCollide = false
					data.angle = data.angle + math.rad(speed * data.spinModifier)
					
					local offset = Vector3.zero
					local targetY = groundY

					if currentMode == "Tornado" then
						data.height = data.height + data.upwardSpeed 

						local tHeight = tonumber(heightBox.Text) or 100
						local uWidth = tonumber(upperWidthBox.Text) or 120
						local lWidth = tonumber(lowerWidthBox.Text) or 5
						
						if data.height > tHeight then 
							data.height = 0 
							data.radiusMultiplier = math.random(40, 100) / 100
							data.upwardSpeed = math.random(40, 120) / 100
							data.spinModifier = math.random(60, 140) / 100
						end

						local heightPercent = math.clamp(data.height / tHeight, 0, 1)
						local maxRadiusAtHeight = lWidth + ((uWidth - lWidth) * (heightPercent ^ 1.5))
						local currentTornadoRadius = maxRadiusAtHeight * data.radiusMultiplier
						
						local xOff = math.cos(data.angle) * currentTornadoRadius
						local zOff = math.sin(data.angle) * currentTornadoRadius
						targetY = groundY + data.clearance + data.height
						
						offset = Vector3.new(root.Position.X + xOff, targetY, root.Position.Z + zOff)
						
					elseif currentMode == "Ring" then
						local rRadius = tonumber(rRadiusBox.Text) or 30
						local rThickness = tonumber(rThicknessBox.Text) or 10
						
						data.height = 0
						
						local currentRingRadius = rRadius + ((data.radiusMultiplier - 0.7) * rThickness)
						
						local xOff = math.cos(data.angle) * currentRingRadius
						local zOff = math.sin(data.angle) * currentRingRadius
						targetY = root.Position.Y
						
						offset = Vector3.new(root.Position.X + xOff, targetY, root.Position.Z + zOff)
					end

					local bp = part:FindFirstChild("TornadoBP")
					if bp then
						bp.Position = offset
					end
				else
					if part.Parent then
						part.CanCollide = data.originalCollide
						part.CanQuery = data.originalQuery
						pcall(function()
							part:SetNetworkOwner(nil)
							part.CollisionGroup = "Default"
						end)
					end
					partsInTornado[part] = nil
				end
			end
		end)
	end

	toggleBtn.MouseButton1Click:Connect(function()
		if isSystemActive then
			stopSystem()
		else
			startSystem()
		end
	end)

	closeBtn.MouseButton1Click:Connect(function()
		stopSystem()
		gui:Destroy()
	end)
end))

mas = Instance.new("Model",game:GetService("Lighting"))
Tool0 = Instance.new("Tool")
Part1 = Instance.new("Part")
CylinderMesh2 = Instance.new("CylinderMesh")
Part3 = Instance.new("Part")
LocalScript4 = Instance.new("LocalScript")
Script5 = Instance.new("Script")
LocalScript6 = Instance.new("LocalScript")
Script7 = Instance.new("Script")
LocalScript8 = Instance.new("LocalScript")
Part9 = Instance.new("Part")
Script10 = Instance.new("Script")
Part11 = Instance.new("Part")
Script12 = Instance.new("Script")
Part13 = Instance.new("Part")
Script14 = Instance.new("Script")
Tool0.Name = "Object Puller By HouseflyPlayz"
Tool0.Parent = mas
Tool0.CanBeDropped = false
Part1.Name = "Handle"
Part1.Parent = Tool0
Part1.Material = Enum.Material.Neon
Part1.BrickColor = BrickColor.new("Cyan")
Part1.Transparency = 1
Part1.Rotation = Vector3.new(0, 15.4200001, 0)
Part1.CanCollide = false
Part1.FormFactor = Enum.FormFactor.Custom
Part1.Size = Vector3.new(1, 0.400000036, 0.300000012)
Part1.CFrame = CFrame.new(-55.2695465, 0.696546972, 0.383156985, 0.96399641, -4.98074878e-05, 0.265921414, 4.79998416e-05, 1, 1.32960558e-05, -0.265921414, -5.30653779e-08, 0.96399641)
Part1.BottomSurface = Enum.SurfaceType.Smooth
Part1.TopSurface = Enum.SurfaceType.Smooth
Part1.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Part1.Position = Vector3.new(-55.2695465, 0.696546972, 0.383156985)
Part1.Orientation = Vector3.new(0, 15.4200001, 0)
Part1.Color = Color3.new(0.0156863, 0.686275, 0.92549)
CylinderMesh2.Parent = Part1
CylinderMesh2.Scale = Vector3.new(0.100000001, 0.100000001, 0.100000001)
Part3.Name = "Shoot"
Part3.Parent = Tool0
Part3.Material = Enum.Material.Neon
Part3.BrickColor = BrickColor.new("Cyan")
Part3.Reflectance = 0.30000001192093
Part3.Transparency = 1
Part3.Rotation = Vector3.new(90.9799957, 0.25999999, -91.409996)
Part3.CanCollide = false
Part3.FormFactor = Enum.FormFactor.Custom
Part3.Size = Vector3.new(0.200000003, 0.25, 0.310000032)
Part3.CFrame = CFrame.new(-54.7998123, 0.774299085, -0.757350147, -0.0245519895, 0.99968797, 0.00460194098, 0.0169109926, 0.00501798885, -0.999844491, -0.999555528, -0.0244703442, -0.0170289185)
Part3.BottomSurface = Enum.SurfaceType.Smooth
Part3.TopSurface = Enum.SurfaceType.Smooth
Part3.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Part3.Position = Vector3.new(-54.7998123, 0.774299085, -0.757350147)
Part3.Orientation = Vector3.new(88.9899979, 164.87999, 73.4700012)
Part3.Color = Color3.new(0.0156863, 0.686275, 0.92549)
LocalScript4.Parent = Tool0
table.insert(cors,sandbox(LocalScript4,function()
local render = game:GetService("RunService").RenderStepped
local contextActionService = game:GetService("ContextActionService")
local userInputService = game:GetService("UserInputService")
local player = game.Players.LocalPlayer
local mouse = player:GetMouse()
local Tool = script.Parent
local screenSpace = require(Tool:WaitForChild("ScreenSpace"))
local connection
local neck, shoulder, oldNeckC0, oldShoulderC0 
local mobileShouldTrack = true
local function amISitting(character)
	local t = character.Torso
	for _, part in pairs(t:GetConnectedParts(true)) do
		if part:IsA("Seat") or part:IsA("VehicleSeat") then
			return true
		end
	end
end
local function frame(mousePosition)
	if not mobileShouldTrack then return end
	if player.Character.Humanoid:GetState() ~= Enum.HumanoidStateType.Swimming then
		local torso = player.Character.Torso
		local head = player.Character.Head
		local toMouse = (mousePosition - head.Position).unit
		local angle = math.acos(toMouse:Dot(Vector3.new(0,1,0)))
		local neckAngle = angle
		if math.deg(neckAngle) > 110 then
			neckAngle = math.rad(110)
		end
		neck.C0 = CFrame.new(0,1,0) * CFrame.Angles(math.pi - neckAngle,math.pi,0)
		local arm = player.Character:FindFirstChild("Right Arm")
		local fromArmPos = torso.Position + torso.CFrame:vectorToWorldSpace(Vector3.new(
			torso.Size.X/2 + arm.Size.X/2, torso.Size.Y/2 - arm.Size.Z/2, 0))
		local toMouseArm = ((mousePosition - fromArmPos) * Vector3.new(1,0,1)).unit
		local look = (torso.CFrame.lookVector * Vector3.new(1,0,1)).unit
		local lateralAngle = math.acos(toMouseArm:Dot(look))		
		if tostring(lateralAngle) == "-1.#IND" then
			lateralAngle = 0
		end		
		if player.Character.Humanoid:GetState() == Enum.HumanoidStateType.Seated then			
			local cross = torso.CFrame.lookVector:Cross(toMouseArm)
			if lateralAngle > math.pi/2 then
				lateralAngle = math.pi/2
			end
			if cross.Y < 0 then
				lateralAngle = -lateralAngle
			end
		end	
		shoulder.C0 = CFrame.new(1,0.5,0) * CFrame.Angles(math.pi/2 - angle,math.pi/2 + lateralAngle,0)	
		if not amISitting(player.Character) then
			torso.CFrame = CFrame.new(torso.Position, torso.Position + (Vector3.new(
				mousePosition.X, torso.Position.Y, mousePosition.Z)-torso.Position).unit)
		else
		end	
	end
end
local function pcFrame()
	frame(mouse.Hit.p)
end
local function mobileFrame(touch, processed)
	if not processed then
		local test = screenSpace.ScreenToWorld(touch.Position.X, touch.Position.Y, 1)
		local nearPos = game.Workspace.CurrentCamera.CoordinateFrame:vectorToWorldSpace(screenSpace.ScreenToWorld(touch.Position.X, touch.Position.Y, 1))
		nearPos = game.Workspace.CurrentCamera.CoordinateFrame.p - nearPos
		local farPos = screenSpace.ScreenToWorld(touch.Position.X, touch.Position.Y,50) 
		farPos = game.Workspace.CurrentCamera.CoordinateFrame:vectorToWorldSpace(farPos) * -1
		if farPos.magnitude > 900 then
			farPos = farPos.unit * 900
		end
		local ray = Ray.new(nearPos, farPos)
		local part, pos = game.Workspace:FindPartOnRay(ray, player.Character)
		if pos then
			frame(pos)
		end
	end
end
local oldIcon = nil
local function equip()
	local torso = player.Character.Torso
	neck = torso.Neck	
	oldNeckC0 = neck.C0
	shoulder = torso:FindFirstChild("Right Shoulder")
	oldShoulderC0 = shoulder.C0
	oldIcon = mouse.Icon
	mouse.Icon = "rbxassetid:// 2184939409"
	if userInputService.TouchEnabled then
		connection = userInputService.TouchMoved:connect(mobileFrame)
	else
		connection = render:connect(pcFrame)
	end
	userInputService.TouchStarted:connect(function(touch, processed)
		mobileShouldTrack = not processed
	end)	
	userInputService.TouchEnded:connect(function(touch, processed)
		mobileShouldTrack = false
	end)
	game.ReplicatedStorage.ROBLOX_PistolEquipEvent:FireServer()
	mouse.Button1Down:connect(function()
		game.ReplicatedStorage.ROBLOX_PistolFireEvent:FireServer(mouse.Hit.p)
	end)
	contextActionService:BindActionToInputTypes("Reload", function() 
		game.ReplicatedStorage.ROBLOX_PistolReloadEvent:FireServer()		
	end, true, "")
	if workspace.FilteringEnabled then
		while connection do
			wait()
			game.ReplicatedStorage.ROBLOX_PistolUpdateEvent:FireServer(neck.C0, shoulder.C0)
		end
	end
end
local function unequip()
	if connection then connection:disconnect() end
	contextActionService:UnbindAction("Reload")
	game.ReplicatedStorage.ROBLOX_PistolUnequipEvent:FireServer()
	mouse.Icon = oldIcon
	neck.C0 = oldNeckC0
	shoulder.C0 = oldShoulderC0
end
Tool.Equipped:connect(equip)
Tool.Unequipped:connect(unequip)
end))
Script5.Name = "qPerfectionWeld"
Script5.Parent = Tool0
table.insert(cors,sandbox(Script5,function()
local NEVER_BREAK_JOINTS = false 
local function CallOnChildren(Instance, FunctionToCall)
	FunctionToCall(Instance)
	for _, Child in next, Instance:GetChildren() do
		CallOnChildren(Child, FunctionToCall)
	end
end
local function GetNearestParent(Instance, ClassName)
	local Ancestor = Instance
	repeat
		Ancestor = Ancestor.Parent
		if Ancestor == nil then
			return nil
		end
	until Ancestor:IsA(ClassName)
	return Ancestor
end
local function GetBricks(StartInstance)
	local List = {}
	CallOnChildren(StartInstance, function(Item)
		if Item:IsA("BasePart") then
			List[#List+1] = Item;
		end
	end)
	return List
end
local function Modify(Instance, Values)
	assert(type(Values) == "table", "Values is not a table");
	for Index, Value in next, Values do
		if type(Index) == "number" then
			Value.Parent = Instance
		else
			Instance[Index] = Value
		end
	end
	return Instance
end
local function Make(ClassType, Properties)
	return Modify(Instance.new(ClassType), Properties)
end
local Surfaces = {"TopSurface", "BottomSurface", "LeftSurface", "RightSurface", "FrontSurface", "BackSurface"}
local HingSurfaces = {"Hinge", "Motor", "SteppingMotor"}
local function HasWheelJoint(Part)
	for _, SurfaceName in pairs(Surfaces) do
		for _, HingSurfaceName in pairs(HingSurfaces) do
			if Part[SurfaceName].Name == HingSurfaceName then
				return true
			end
		end
	end
	return false
end
local function ShouldBreakJoints(Part)
	if NEVER_BREAK_JOINTS then
		return false
	end
	if HasWheelJoint(Part) then
		return false
	end
	local Connected = Part:GetConnectedParts()
	if #Connected == 1 then
		return false
	end
	for _, Item in pairs(Connected) do
		if HasWheelJoint(Item) then
			return false
		elseif not Item:IsDescendantOf(script.Parent) then
			return false
		end
	end
	return true
end
local function WeldTogether(Part0, Part1, JointType, WeldParent)
	JointType = JointType or "Weld"
	local RelativeValue = Part1:FindFirstChild("qRelativeCFrameWeldValue")
	local NewWeld = Part1:FindFirstChild("qCFrameWeldThingy") or Instance.new(JointType)
	Modify(NewWeld, {
		Name = "qCFrameWeldThingy";
		Part0  = Part0;
		Part1  = Part1;
		C0     = CFrame.new();
		C1     = RelativeValue and RelativeValue.Value or Part1.CFrame:toObjectSpace(Part0.CFrame); 
		Parent = Part1;
	})
	if not RelativeValue then
		RelativeValue = Make("CFrameValue", {
			Parent     = Part1;
			Name       = "qRelativeCFrameWeldValue";
			Archivable = true;
			Value      = NewWeld.C1;
		})
	end
	return NewWeld
end
local function WeldParts(Parts, MainPart, JointType, DoNotUnanchor)
	for _, Part in pairs(Parts) do
		if ShouldBreakJoints(Part) then
			Part:BreakJoints()
		end
	end
	for _, Part in pairs(Parts) do
		if Part ~= MainPart then
			WeldTogether(MainPart, Part, JointType, MainPart)
		end
	end
	if not DoNotUnanchor then
		for _, Part in pairs(Parts) do
			Part.Anchored = false
		end
		MainPart.Anchored = false
	end
end
local function PerfectionWeld()	
	local Tool = GetNearestParent(script, "Tool")
	local Parts = GetBricks(script.Parent)
	local PrimaryPart = Tool and Tool:FindFirstChild("Handle") and Tool.Handle:IsA("BasePart") and Tool.Handle or script.Parent:IsA("Model") and script.Parent.PrimaryPart or Parts[1]
	if PrimaryPart then
		WeldParts(Parts, PrimaryPart, "Weld", false)
	else
		warn("qWeld - Unable to weld part")
	end
	return Tool
end
local Tool = PerfectionWeld()
if Tool and script.ClassName == "Script" then
	script.Parent.AncestryChanged:connect(function()
		PerfectionWeld()
	end)
end
end))
LocalScript6.Name = "Animate"
LocalScript6.Parent = Tool0
table.insert(cors,sandbox(LocalScript6,function()
local arms = nil
local torso = nil
local welds = {}
local Tool = script.Parent
local neck = nil
local orginalC0 = CFrame.new(0, 1, 0, -1, -0, -0, 0, 0, 1, 0, 1, 0)
function Equip(mouse)
wait(0.01)
arms = {Tool.Parent:FindFirstChild("Left Arm"), Tool.Parent:FindFirstChild("Right Arm")}
head = Tool.Parent:FindFirstChild("Head") 
torso = Tool.Parent:FindFirstChild("Torso")
if neck == nil then 
neck = Tool.Parent:FindFirstChild("Torso").Neck
end 
if arms ~= nil and torso ~= nil then
local sh = {torso:FindFirstChild("Left Shoulder"), torso:FindFirstChild("Right Shoulder")}
if sh ~= nil then
local yes = true
if yes then
yes = false
sh[1].Part1 = nil
sh[2].Part1 = nil
local weld1 = Instance.new("Weld")
weld1.Part0 = head
weld1.Parent = head
weld1.Part1 = arms[1]
welds[1] = weld1
local weld2 = Instance.new("Weld")
weld2.Part0 = head
weld2.Parent = head
weld2.Part1 = arms[2]
welds[2] = weld2
weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0, math.rad(-90))
weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)
	mouse.Move:connect(function ()
		local Direction = mouse.Hit.p
		local b = head.Position.Y-Direction.Y
		local dist = (head.Position-Direction).magnitude
		local answer = math.asin(b/dist)
		neck.C0=orginalC0*CFrame.fromEulerAnglesXYZ(answer,0,0)
		wait(0.1)
	end)end
else
print("sh")
end
else
print("arms")
end
end
function Unequip(mouse)
if arms ~= nil and torso ~= nil then
local sh = {torso:FindFirstChild("Left Shoulder"), torso:FindFirstChild("Right Shoulder")}
if sh ~= nil then
local yes = true
if yes then
yes = false
	neck.C0 = orginalC0
sh[1].Part1 = arms[1]
sh[2].Part1 = arms[2]
welds[1].Parent = nil
welds[2].Parent = nil
end
else
print("sh")
end
else
print("arms")
end
end
Tool.Equipped:connect(Equip)
Tool.Unequipped:connect(Unequip)
function Animate()
arms = {Tool.Parent:FindFirstChild("Left Arm"), Tool.Parent:FindFirstChild("Right Arm")}
	if Tool.AnimateValue.Value == "Shoot" then 
		local weld1 = welds[1]
		local weld2 = welds[2]
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.05, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.1, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-95), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.3, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-110), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.35, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-115), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.00001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)	
		Tool.AnimateValue.Value = "None"
	end 
	if Tool.AnimateValue.Value == "Reload" then 
		local weld1 = welds[1]
		local weld2 = welds[2]
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-95), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-100), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-105), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-110), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.4, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-115), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.45, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.45, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.9, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.5, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 1, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.55, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 1.1, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.57, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 1.2, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.6, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 1.3, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0.6, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-120), math.rad(-15), 0)
		wait(0.0001)
		weld1.C1 = CFrame.new(-0.5+1.5, 0.8, .9)* CFrame.fromEulerAnglesXYZ(math.rad(290), 0, math.rad(-90))
		weld2.C1 = CFrame.new(-1, 0.8, 0.5-1.5) * CFrame.fromEulerAnglesXYZ(math.rad(-90), math.rad(-15), 0)	
		Tool.AnimateValue.Value = "None"
	end 
end 
Tool.AnimateValue.Changed:connect(Animate)
end))
Script7.Name = "LineConnect"
Script7.Parent = Tool0
Script7.Disabled = true
table.insert(cors,sandbox(Script7,function()
wait()
local check = script.Part2
local part1 = script.Part1.Value
local part2 = script.Part2.Value
local parent = script.Par.Value
local color = script.Color
local line = Instance.new("Part")
line.TopSurface = 0
line.BottomSurface = 0
line.Reflectance = .5
line.Name = "Laser"
line.Transparency = 0.6
line.Locked = true
line.CanCollide = false
line.Anchored = true
line.formFactor = 0
line.Size = Vector3.new(0.4,0.4,1)
local mesh = Instance.new("BlockMesh")
mesh.Parent = line
while true do
	if (check.Value==nil) then break end
	if (part1==nil or part2==nil or parent==nil) then break end
	if (part1.Parent==nil or part2.Parent==nil) then break end
	if (parent.Parent==nil) then break end
	local lv = CFrame.new(part1.Position,part2.Position)
	local dist = (part1.Position-part2.Position).magnitude
	line.Parent = parent
	line.Material = "Neon"
	line.BrickColor = color.Value.BrickColor
	line.Reflectance = color.Value.Reflectance
	line.Transparency = "0.2"
	line.CFrame = CFrame.new(part1.Position+lv.lookVector*dist/2)
	line.CFrame = CFrame.new(line.Position,part2.Position)
	mesh.Scale = Vector3.new(.25,.25,dist)
	wait()
end
line:remove()
script:remove() 
end))
LocalScript8.Name = "MainScript"
LocalScript8.Parent = Tool0
table.insert(cors,sandbox(LocalScript8,function()
wait() 
tool = script.Parent
lineconnect = tool.LineConnect
object = nil
mousedown = false
found = false
BP = Instance.new("BodyPosition")
BP.maxForce = Vector3.new(math.huge*math.huge,math.huge*math.huge,math.huge*math.huge)
BP.P = BP.P*10
dist = nil
point = Instance.new("Part")
point.Locked = true
point.Anchored = true
point.formFactor = 0
point.Shape = 0
point.Material = 'Neon'
point.BrickColor = BrickColor.new("Toothpaste")
point.Size = Vector3.new(1,1,1)
point.CanCollide = false
local mesh = Instance.new("SpecialMesh")
mesh.MeshType = "Sphere"
mesh.Scale = Vector3.new(.2,.2,.2)
mesh.Parent = point
handle = tool.Shoot
front = tool.Shoot
color = tool.Shoot
objval = nil
local hooked = false 
local hookBP = BP:clone() 
hookBP.maxForce = Vector3.new(30000,30000,30000) 
function LineConnect(part1,part2,parent)
	local p1 = Instance.new("ObjectValue")
	p1.Value = part1
	p1.Name = "Part1"
	local p2 = Instance.new("ObjectValue")
	p2.Value = part2
	p2.Name = "Part2"
	local par = Instance.new("ObjectValue")
	par.Value = parent
	par.Name = "Par"
	local col = Instance.new("ObjectValue")
	col.Value = color
	col.Name = "Color"
	local s = lineconnect:clone()
	s.Disabled = false
	p1.Parent = s
	p2.Parent = s
	par.Parent = s
	col.Parent = s
	s.Parent = workspace
	if (part2==object) then
		objval = p2
	end
end
function onButton1Down(mouse)
	if (mousedown==true) then return end
	mousedown = true
	coroutine.resume(coroutine.create(function()
		local p = point:clone()
		p.Parent = tool
		LineConnect(front,p,workspace)
		while (mousedown==true) do
			p.Parent = tool
			if (object==nil) then
				if (mouse.Target==nil) then
					local lv = CFrame.new(front.Position,mouse.Hit.p)
					p.CFrame = CFrame.new(front.Position+(lv.lookVector*1000))
				else
					p.CFrame = CFrame.new(mouse.Hit.p)
				end
			else
				LineConnect(front,object,workspace)
				break
			end
			wait()
		end
		p:remove()
	end))
	while (mousedown==true) do
		if (mouse.Target~=nil) then
			local t = mouse.Target
			if (t.Anchored==false) then
				object = t
				dist = (object.Position-front.Position).magnitude
				break
			end
		end
		wait()
	end
	while (mousedown==true) do
		if (object.Parent==nil) then break end
		local lv = CFrame.new(front.Position,mouse.Hit.p)
		BP.Parent = object
		BP.position = front.Position+lv.lookVector*dist
		wait()
	end
	BP:remove()
	object = nil
	objval.Value = nil
end
function onKeyDown(key,mouse) 
	local key = key:lower() 
	local yesh = false 
	if (key=="q") then 
		if (dist>=5) then 
			dist = dist-5 
		end 
	end 
	if key == "t" then 
	if (object==nil) then return end 
	for _,v in pairs(object:children()) do 
	if v.className == "BodyGyro" then 
	return nil 
	end 
	end 
	BG = Instance.new("BodyGyro") 
	BG.maxTorque = Vector3.new(math.huge,math.huge,math.huge) 
	BG.cframe = CFrame.new(object.CFrame.p) 
	BG.Parent = object 
	repeat wait() until(object.CFrame == CFrame.new(object.CFrame.p)) 
	BG.Parent = nil 
	if (object==nil) then return end 
	for _,v in pairs(object:children()) do 
	if v.className == "BodyGyro" then 
	v.Parent = nil 
	end 
	end 
	object.Velocity = Vector3.new(0,0,0) 
	object.RotVelocity = Vector3.new(0,0,0) 
	end 
	if (key=="e") then
		dist = dist+5
	end
	if (string.byte(key)==27) then 
		if (object==nil) then return end
		local e = Instance.new("Explosion")
		e.Parent = workspace
		e.Position = object.Position
		color.BrickColor = BrickColor.Black()
		point.BrickColor = BrickColor.White() 
		wait(.48)
		color.BrickColor = BrickColor.White() 
		point.BrickColor = BrickColor.Black() 
	end
	if (key=="") then 
		if not hooked then 
		if (object==nil) then return end 
		hooked = true 
		hookBP.position = object.Position 
		if tool.Parent:findFirstChild("Torso") then 
		hookBP.Parent = tool.Parent.Torso 
		if dist ~= (object.Size.x+object.Size.y+object.Size.z)+5 then 
		dist = (object.Size.x+object.Size.y+object.Size.z)+5 
		end 
		end 
		else 
		hooked = false 
		hookBP.Parent = nil 
		end 
	end 
	if (key=="r") then 
		if (object==nil) then return end 
		color.BrickColor = BrickColor.new("Toothpaste") 
		point.BrickColor = BrickColor.new("Toothpaste") 
		object.Parent = nil 
		wait(.48) 
		color.BrickColor = BrickColor.new("Toothpaste")
		point.BrickColor = BrickColor.new("Toothpaste")
	end 
	if (key=="x") then 
	if (object==nil) then return end 
	local New = object:clone() 
	New.Parent = object.Parent 
	for _,v in pairs(New:children()) do 
	if v.className == "BodyPosition" or v.className == "BodyGyro" then 
	v.Parent = nil 
	end 
	end 
	object = New 
	mousedown = false 
	mousedown = true 
	LineConnect(front,object,workspace) 
		while (mousedown==true) do
		if (object.Parent==nil) then break end
		local lv = CFrame.new(front.Position,mouse.Hit.p)
		BP.Parent = object
		BP.position = front.Position+lv.lookVector*dist
		wait()
	end
	BP:remove()
	object = nil
	objval.Value = nil
	end 
	if (key=="c") then 
		local Cube = Instance.new("Part") 
		Cube.Locked = true 
		Cube.Size = Vector3.new(4,4,4) 
		Cube.formFactor = 0 
		Cube.TopSurface = 0 
		Cube.BottomSurface = 0 
		Cube.Name = "WeightedStorageCube" 
		Cube.Parent = workspace 
		Cube.CFrame = CFrame.new(mouse.Hit.p) + Vector3.new(0,2,0) 
		for i = 0,5 do 
			local Decal = Instance.new("Decal") 
			Decal.Texture = "http://www.roblox.com/asset/?id=2662260" 
			Decal.Face = i 
			Decal.Name = "WeightedStorageCubeDecal" 
			Decal.Parent = Cube 
		end 
	end 
	if (key=="") then 
		if dist ~= 15 then 
			dist = 15 
		end 
	end 
end
function onEquipped(mouse)
	keymouse = mouse
	local char = tool.Parent
	human = char.Humanoid
	human.Changed:connect(function() if (human.Health==0) then mousedown = false BP:remove() point:remove() tool:remove() end end)
	mouse.Button1Down:connect(function() onButton1Down(mouse) end)
	mouse.Button1Up:connect(function() mousedown = false end)
	mouse.KeyDown:connect(function(key) onKeyDown(key,mouse) end)
	mouse.Icon = "rbxassetid://2184939409"
end
tool.Equipped:connect(onEquipped)
end))
Part9.Name = "GlowPart"
Part9.Parent = Tool0
Part9.Material = Enum.Material.Neon
Part9.BrickColor = BrickColor.new("Cyan")
Part9.Transparency = 0.5
Part9.Rotation = Vector3.new(0, -89.5899963, 0)
Part9.Shape = Enum.PartType.Cylinder
Part9.Size = Vector3.new(1.20000005, 0.649999976, 2)
Part9.CFrame = CFrame.new(-54.8191681, 0.773548007, -0.0522949994, 0.00736002205, 4.68389771e-11, -0.999974668, 4.72937245e-11, 1, 1.41590961e-10, 0.999974668, 5.09317033e-11, 0.00736002252)
Part9.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Part9.Position = Vector3.new(-54.8191681, 0.773548007, -0.0522949994)
Part9.Orientation = Vector3.new(0, -89.5799942, 0)
Part9.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Script10.Name = "Glow Script"
Script10.Parent = Part9
table.insert(cors,sandbox(Script10,function()
while true do
wait(0.05)
script.Parent.Transparency = .5
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .9
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .5
end
end))
Part11.Name = "GlowPart"
Part11.Parent = Tool0
Part11.Material = Enum.Material.Neon
Part11.BrickColor = BrickColor.new("Cyan")
Part11.Transparency = 0.5
Part11.Rotation = Vector3.new(-89.3799973, -55.7399979, -89.25)
Part11.Size = Vector3.new(0.280000001, 0.25999999, 0.200000003)
Part11.CFrame = CFrame.new(-54.9808807, 0.99843204, 0.799362957, 0.00736002205, 0.562958956, -0.826454222, 4.72937245e-11, 0.826475084, 0.56297338, 0.999974668, -0.00414349511, 0.00608287565)
Part11.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Part11.Position = Vector3.new(-54.9808807, 0.99843204, 0.799362957)
Part11.Orientation = Vector3.new(-34.2599983, -89.5799942, 0)
Part11.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Script12.Name = "Glow Script"
Script12.Parent = Part11
table.insert(cors,sandbox(Script12,function()
while true do
wait(0.05)
script.Parent.Transparency = .5
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .9
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .5
end
end))
Part13.Name = "GlowPart"
Part13.Parent = Tool0
Part13.Material = Enum.Material.Neon
Part13.BrickColor = BrickColor.new("Cyan")
Part13.Transparency = 0.5
Part13.Rotation = Vector3.new(95.1500015, -53.8199997, 98.0799942)
Part13.Size = Vector3.new(0.280000001, 0.25999999, 0.200000003)
Part13.CFrame = CFrame.new(-54.5909271, 0.978429973, 0.799362957, -0.0830051303, -0.584483683, -0.807150841, 0.0241250042, 0.808528602, -0.58796227, 0.996258855, -0.0682764053, -0.0530113392)
Part13.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Part13.Position = Vector3.new(-54.5909271, 0.978429973, 0.799362957)
Part13.Orientation = Vector3.new(36.0099983, -93.7599945, 1.70999992)
Part13.Color = Color3.new(0.0156863, 0.686275, 0.92549)
Script14.Name = "Glow Script"
Script14.Parent = Part13
table.insert(cors,sandbox(Script14,function()
while true do
wait(0.05)
script.Parent.Transparency = .5
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .9
wait(0.05)
script.Parent.Transparency = .8
wait(0.05)
script.Parent.Transparency = .7
wait(0.05)
script.Parent.Transparency = .6
wait(0.05)
script.Parent.Transparency = .5
end
end))
for i,v in pairs(mas:GetChildren()) do
	v.Parent = game:GetService("Players").LocalPlayer:WaitForChild("Backpack")
	pcall(function() v:MakeJoints() end)
end
mas:Destroy()
for i,v in pairs(cors) do
	task.spawn(function()
		pcall(v)
	end)
end
