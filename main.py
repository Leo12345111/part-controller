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

local LocalScript17 = Instance.new("LocalScript")
LocalScript17.Name = "TornadoUI"
table.insert(cors, sandbox(LocalScript17, function()
	local players = game:GetService("Players")
	local player = players.LocalPlayer
	local playerGui = player:WaitForChild("PlayerGui")
	local runService = game:GetService("RunService")
	local physicsService = game:GetService("PhysicsService")

	local TORNADO_GROUP = "TornadoParts"
	pcall(function()
		physicsService:RegisterCollisionGroup(TORNADO_GROUP)
		physicsService:CollisionGroupSetCollidable(TORNADO_GROUP, TORNADO_GROUP, false)
	end)

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
		
		-- DETECTION LOOP: Runs 2 times per second (task.wait(0.5))
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
					-- Slightly increased grab limit since it checks less often
					local maxGrabsPerCycle = 15 

					for _, v in pairs(workspace:GetDescendants()) do
						if grabbedThisCycle >= maxGrabsPerCycle then break end
						
						if v:IsA("BasePart") then
							local isPlayerPart = false
							for _, p in pairs(players:GetPlayers()) do
								if p.Character and v:IsDescendantOf(p.Character) then
									isPlayerPart = true
									break
								end
							end

							if not v.Anchored and not isPlayerPart then
								local dist = (v.Position - root.Position).Magnitude
								
								if dist <= sRange and dist >= 20 and not partsInTornado[v] then
									
									local isAttachedToPlayer = false
									for _, connectedPart in pairs(v:GetConnectedParts()) do
										for _, p in pairs(players:GetPlayers()) do
											if p.Character and connectedPart:IsDescendantOf(p.Character) then
												isAttachedToPlayer = true
												break
											end
										end
										if isAttachedToPlayer then break end
									end
									
									if not isAttachedToPlayer then
										pcall(function()
											v:BreakJoints()
											v:SetNetworkOwner(player)
											v.CollisionGroup = TORNADO_GROUP
										end)
										
										local bp = Instance.new("BodyPosition")
										bp.Name = "TornadoBP"
										
										local partMass = v:GetMass()
										bp.MaxForce = Vector3.new(math.huge, math.huge, math.huge)
										bp.P = 150000 + (partMass * 5000) 
										bp.D = 1500 
										
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
											spinModifier = math.random(50, 180) / 100,
											speedAdd = math.random(-8, 8)
										}
										
										v.CanQuery = false
										
										grabbedThisCycle = grabbedThisCycle + 1
									end
								end
							end
						end
					end
				end
				-- Wait 0.5 seconds (2 times per second)
				task.wait(0.5) 
			end
		end)
		
		-- MOVEMENT LOOP: Runs every single frame (Heartbeat)
		connection = runService.Heartbeat:Connect(function()
			local char = player.Character
			if not char or not char:FindFirstChild("HumanoidRootPart") then return end
			local root = char.HumanoidRootPart
			
			local baseY = root.Position.Y - 5 
			
			local baseSpeed = tonumber(speedBox.Text) or 35

			for part, data in pairs(partsInTornado) do
				if part.Parent and not part.Anchored then
					
					part.CanCollide = false
					
					local actualSpeed = (baseSpeed * data.spinModifier) + data.speedAdd
					data.angle = data.angle + math.rad(actualSpeed)
					
					local offset = Vector3.zero
					local targetY = baseY

					if currentMode == "Tornado" then
						data.height = data.height + data.upwardSpeed 

						local tHeight = tonumber(heightBox.Text) or 100
						local uWidth = tonumber(upperWidthBox.Text) or 120
						local lWidth = tonumber(lowerWidthBox.Text) or 5
						
						if data.height > tHeight then 
							data.height = 0 
							data.radiusMultiplier = math.random(40, 100) / 100
							data.upwardSpeed = math.random(40, 120) / 100
							data.spinModifier = math.random(50, 180) / 100
							data.speedAdd = math.random(-8, 8)
						end

						local heightPercent = math.clamp(data.height / tHeight, 0, 1)
						local maxRadiusAtHeight = lWidth + ((uWidth - lWidth) * (heightPercent ^ 1.5))
						
						local currentTornadoRadius = math.max(20, maxRadiusAtHeight * data.radiusMultiplier)
						
						local xOff = math.cos(data.angle) * currentTornadoRadius
						local zOff = math.sin(data.angle) * currentTornadoRadius
						
						targetY = baseY + data.height 
						
						offset = Vector3.new(root.Position.X + xOff, targetY, root.Position.Z + zOff)
						
					elseif currentMode == "Ring" then
						local rRadius = tonumber(rRadiusBox.Text) or 30
						local rThickness = tonumber(rThicknessBox.Text) or 10
						
						data.height = 0
						
						local currentRingRadius = math.max(20, rRadius + ((data.radiusMultiplier - 0.7) * rThickness))
						
						local xOff = math.cos(data.angle) * currentRingRadius
						local zOff = math.sin(data.angle) * currentRingRadius
						
						targetY = baseY
						
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

for i,v in pairs(cors) do
	task.spawn(function()
		pcall(v)
	end)
end
