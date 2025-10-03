import imgui
import numpy as np
from utils.graphics import Object, Camera, Shader
from assets.shaders.shaders import object_shader
from assets.objects.objects import playerProps, backgroundProps, obj1Props, enemyProps,entryProps, exitProps,backgroundProps2,backgroundProps3,keyProps
import time
import random


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.screen = -1
        self.camera = Camera(height, width)
        self.shaders = [Shader(object_shader['vertex_shader'], object_shader['fragment_shader'])]
        self.objects = []

        self.ground_level = -40  
        self.is_on_platform = False
        self.is_in_water = False
        self.fall_timer = 0 
        

        #player charcateristics
        self.player_health = 100
        self.player_lives = 3
        self.keys_collected = 0

    def InitScreen(self):
        if self.screen == 0:

            # Initialize platforms/objects
            self.objects = []
            self.keys=[]
            self.collect_key_check=[False]*7
            
            for i in range(6):
                obj = Object(self.shaders[0], obj1Props)
                obj.properties['position'] = np.array(
                    [(-self.width / 2) + 100, (self.height / 2) - (self.height / 8) * (i + 1), 0],
                    dtype=np.float32
                )
                obj.properties['scale'] = np.array([50, 50, 1], dtype=np.float32)
                obj.properties['velocity'] = np.array([50 + 4 * i, 0, 0], dtype=np.float32)  # Keep platform moving
                self.objects.append(obj)

                # Generate keys on only some platforms
                if random.random() < 0.7:  # 50% chance to generate a key
                    key = Object(self.shaders[0], keyProps)
                    key.properties['position'] = obj.properties['position'] + np.array([0, 15, 0], dtype=np.float32)
                    key.properties['scale'] = np.array([3, 3, 1], dtype=np.float32)
                    self.keys.append(key)
                    self.collect_key_check[i] = False  # Mark as not yet collected
                else:
                    self.keys.append(None)  # No key on this platform


            self.entry=Object(self.shaders[0],entryProps)
            self.entry.properties['position']= np.array([-(self.width / 2)+50, 0, 0], dtype=np.float32)
            
            self.exit=Object(self.shaders[0],exitProps)
            self.exit.properties['position']= np.array([(self.width / 2)-50, 0, 0], dtype=np.float32)          

            self.keys_collected =0

            # Reset time for the new game
            self.start_time = time.time()            # Initialize background and player
            self.bg = Object(self.shaders[0], backgroundProps)
            self.player = Object(self.shaders[0], playerProps)
            #palyer at entry position
            self.player.properties['position'] = self.entry.properties['position'].copy()
            self.player.properties['velocity'] = np.array([0, 0, 0], dtype=np.float32)
            self.player.properties['jumping'] = False

            self.enemies=[]
            for i in range(5):
                ene= Object(self.shaders[0], enemyProps)
                ene.properties['position']=np.array(
                    [np.random.uniform(-(self.width / 2)+200, (self.width / 2)-200),np.random.uniform(-self.height / 2, self.height / 2),0],
                    dtype=np.float32
                )
                # Assign a random speed (positive or negative)
                ene.properties['velocity'] = np.array([
                    np.random.choice([-50, 50]),  # Random X direction
                    np.random.choice([-50, 50]),  # Random Y direction
                    0
                ], dtype=np.float32)
    
                self.enemies.append(ene)
      

            # Reset time for the new game
            self.start_time = time.time()

            
        if self.screen == 1:

            # Initialize platforms/objects
            self.objects = []
            self.keys=[]
            self.collect_key_check=[False]*7
            
            for i in range(6):
                obj = Object(self.shaders[0], obj1Props)
                obj.properties['position'] = np.array(
                    [(-self.width / 2) + 100, (self.height / 2) - (self.height / 8) * (i + 1), 0],
                    dtype=np.float32
                )
                obj.properties['scale'] = np.array([50, 50, 1], dtype=np.float32)
                obj.properties['velocity'] = np.array([50 + 4 * i, 0, 0], dtype=np.float32)  # Keep platform moving
                self.objects.append(obj)

                # Generate keys on only some platforms
                if random.random() < 0.7:  # 50% chance to generate a key
                    key = Object(self.shaders[0], keyProps)
                    key.properties['position'] = obj.properties['position'] + np.array([0, 15, 0], dtype=np.float32)
                    key.properties['scale'] = np.array([3, 3, 1], dtype=np.float32)
                    self.keys.append(key)
                    self.collect_key_check[i] = False  # Mark as not yet collected
                else:
                    self.keys.append(None)  # No key on this platform


            self.entry=Object(self.shaders[0],entryProps)
            self.entry.properties['position']= np.array([-(self.width / 2)+50, 0, 0], dtype=np.float32)
            
            self.exit=Object(self.shaders[0],exitProps)
            self.exit.properties['position']= np.array([(self.width / 2)-50, 0, 0], dtype=np.float32)          

            self.keys_collected =0

            # Reset time for the new game
            self.start_time = time.time()            # Initialize background and player
            self.bg = Object(self.shaders[0], backgroundProps2)
            self.player = Object(self.shaders[0], playerProps)
            #palyer at entry position
            self.player.properties['position'] = self.entry.properties['position'].copy()
            self.player.properties['velocity'] = np.array([0, 0, 0], dtype=np.float32)
            self.player.properties['jumping'] = False

            self.enemies=[]
            for i in range(5):
                ene= Object(self.shaders[0], enemyProps)
                ene.properties['position']=np.array(
                    [np.random.uniform(-(self.width / 2)+200, (self.width / 2)-200),np.random.uniform(-self.height / 2, self.height / 2),0],
                    dtype=np.float32
                )
                # Assign a random speed (positive or negative)
                ene.properties['velocity'] = np.array([
                    np.random.choice([-50, 50]),  # Random X direction
                    np.random.choice([-50, 50]),  # Random Y direction
                    0
                ], dtype=np.float32)
    
                self.enemies.append(ene)
      

            # Reset time for the new game
            self.start_time = time.time()

        if self.screen == 2:

            # Initialize platforms/objects
            self.objects = []
            self.keys=[]
            self.collect_key_check=[False]*7
            
            for i in range(6):
                obj = Object(self.shaders[0], obj1Props)
                obj.properties['position'] = np.array(
                    [(-self.width / 2) + 100, (self.height / 2) - (self.height / 8) * (i + 1), 0],
                    dtype=np.float32
                )
                obj.properties['scale'] = np.array([50, 50, 1], dtype=np.float32)
                obj.properties['velocity'] = np.array([50 + 4 * i, 0, 0], dtype=np.float32)  # Keep platform moving
                self.objects.append(obj)

                # Generate keys on only some platforms
                if random.random() < 0.7:  # 50% chance to generate a key
                    key = Object(self.shaders[0], keyProps)
                    key.properties['position'] = obj.properties['position'] + np.array([0, 15, 0], dtype=np.float32)
                    key.properties['scale'] = np.array([3, 3, 1], dtype=np.float32)
                    self.keys.append(key)
                    self.collect_key_check[i] = False  # Mark as not yet collected
                else:
                    self.keys.append(None)  # No key on this platform


            self.entry=Object(self.shaders[0],entryProps)
            self.entry.properties['position']= np.array([-(self.width / 2)+50, 0, 0], dtype=np.float32)
            
            self.exit=Object(self.shaders[0],exitProps)
            self.exit.properties['position']= np.array([(self.width / 2)-50, 0, 0], dtype=np.float32)          

            self.keys_collected =0

            # Reset time for the new game
            self.start_time = time.time()            # Initialize background and player
            self.bg = Object(self.shaders[0], backgroundProps3)
            self.player = Object(self.shaders[0], playerProps)
            #palyer at entry position
            self.player.properties['position'] = self.entry.properties['position'].copy()
            self.player.properties['velocity'] = np.array([0, 0, 0], dtype=np.float32)
            self.player.properties['jumping'] = False

            self.enemies=[]
            for i in range(5):
                ene= Object(self.shaders[0], enemyProps)
                ene.properties['position']=np.array(
                    [np.random.uniform(-(self.width / 2)+200, (self.width / 2)-200),np.random.uniform(-self.height / 2, self.height / 2),0],
                    dtype=np.float32
                )
                # Assign a random speed (positive or negative)
                ene.properties['velocity'] = np.array([
                    np.random.choice([-50, 50]),  # Random X direction
                    np.random.choice([-50, 50]),  # Random Y direction
                    0
                ], dtype=np.float32)
    
                self.enemies.append(ene)
      

            # Reset time for the new game
            self.start_time = time.time()


    def ProcessFrame(self, inputs, time):
        if self.screen == -1:
            self.screen = 0
            self.InitScreen()
        if self.screen == 0:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
        if self.screen == 1:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
        if self.screen==2:
            self.DrawText()
            self.UpdateScene(inputs, time)
            self.DrawScene()
            
    def DrawText(self):
        if self.screen == 0:
           pass
        if self.screen == 1:
           pass
        if self.screen == 2:
           pass

    def RespawnPlayer(self):
        """Respawn the player at the current level's entry point and reset health."""
        self.player_lives -= 1
        self.player_health = 100
        self.player.properties['position'] = self.entry.properties['position'].copy()
        # Optionally, reset velocity
        self.player.properties['velocity'][:] = 0
        if self.player_lives <= 0:
            self.state = "GAME_OVER"

    def TransitionToNextLevel(self):
        """Transition to the next level if available or end the game if last level completed."""
        if self.screen < 2:
            self.screen += 1
            self.InitScreen()  # Reinitialize objects for the new level
            self.keys_collected = 0  # Reset key collection for the new level
            # Set player at the new entry point
            self.player.properties['position'] = self.entry.properties['position'].copy()
        else:
            # Last level completed
            self.state = "YOU_WON"

    def clampPlayerPositionscene0(self):
        # Retrieve the current position.
        pos = self.player.properties["position"]
        # Clamp the x coordinate between -width/2 and width/2.
        pos[0] = np.clip(pos[0], -self.width/2, self.width/2)
        # Clamp the y coordinate between -height/2 and height/2.
        pos[1] = np.clip(pos[1], -self.height/2, self.height/2)
        # Save the clamped position.
        self.player.properties["position"] = pos

    def clampPlayerPositionscene1(self):
        pos = self.player.properties["position"]
        # Clamp the x coordinate between -width/2 and width/2.
        pos[0] = np.clip(pos[0], -self.width/2, self.width/2)
        # Clamp the y coordinate between -height/2 and height/2.
        pos[1] = np.clip(pos[1], -self.height/2, self.height/2)
        # Save the clamped position.
        self.player.properties["position"] = pos



    def clampPlayerPositionscene2(self):
        pos = self.player.properties["position"]
        # Clamp the x coordinate between -width/2 and width/2.
        pos[0] = np.clip(pos[0], -self.width/2, self.width/2)
        # Clamp the y coordinate between -height/2 and height/2.
        pos[1] = np.clip(pos[1], -self.height/2, self.height/2)
        # Save the clamped position.
        self.player.properties["position"] = pos

    def UpdateScene(self, inputs, time):

            
        if self.screen == 0:
            delta_time = time['deltaTime']
            self.is_on_platform=False
            self.player.properties['velocity'][:] = 0



            for i, platform in enumerate(self.objects):  # Loop only over existing platforms
                # Reverse direction if reaching boundary
                if platform.properties['position'][0] < (-self.width / 2) + 100 or platform.properties['position'][0] > (self.width / 2) - 100:
                    platform.properties['velocity'][0] *= -1

                # Update platform position
                platform.properties['position'][0] += platform.properties['velocity'][0] * delta_time

                # Check if a key exists for this platform
                if self.keys[i] is not None:
                    key = self.keys[i]
                    key.properties['position'] = platform.properties['position'] + np.array([0, 15, 0], dtype=np.float32)

                    # Check if player collects the key
                    if np.linalg.norm(self.player.properties['position'] - key.properties['position']) < 40:
                        self.collect_key_check[i] = True
                        self.keys_collected = sum(self.collect_key_check)  # Ensure it updates properly
                        key.properties['scale'] = np.array([0, 0, 0], dtype=np.float32)  # Hide the key




            for platform in self.objects:
                platform_pos = platform.properties['position']
                player_pos = self.player.properties['position']
                
                # Collision detection (player stands on platform)
                if (abs(player_pos[0] - platform_pos[0]) < platform.properties['scale'][0] / 2 and
                    abs(player_pos[1] - platform_pos[1]) < platform.properties['scale'][1] / 2):
                    
                    self.is_on_platform = True
                    self.player.properties['position'][1] = platform_pos[1]  # Stick to platform height
                    self.player.properties['position'][2] = platform_pos[2]+ 15
                    self.player.properties['velocity'] = platform.properties['velocity'].copy()
                    break
                    

        # Apply gravity if not on a platform
            if not self.is_on_platform and (self.player.properties['position'][0]>-400 and self.player.properties['position'][0]<400):
                self.player.properties['velocity'][2] -= 300 * delta_time  # Simulate gravity

            # Jumping mechanics (if on a platform and SPACE is pressed)
            if self.is_on_platform and "SPACE" in inputs:
                self.player.properties["velocity"] = np.array([0, 250, 0], dtype=np.float32)  # Jump up

            
            #if player dies 
            if self.player.properties["position"][2] < -1:
                self.RespawnPlayer()

            #check if player collected all keys or not
            if np.linalg.norm(self.player.properties["position"] - self.exit.properties["position"]) < 40:
                if sum(self.collect_key_check)>= 3:
                    self.TransitionToNextLevel()

            # Handle player movement inputs

            if "A" in inputs:
                self.player.properties["velocity"][0] =self.player.properties["velocity"][0]+ -200
            if "S" in inputs:
                self.player.properties["velocity"][1]+= -200
            if "D" in inputs:
                self.player.properties["velocity"][0]+= 200
            if "W" in inputs:
                self.player.properties["velocity"][1]+= 200

            # Enemy collision check
            for enemy in self.enemies:
                enemy_pos = enemy.properties['position']
                player_pos = self.player.properties['position']

                distance = np.linalg.norm(player_pos - enemy_pos)
                
                if distance < 20:  # If player gets too close
                    self.player_health -= 10  # Reduce health
                    print(f"Player health: {self.player_health}")

                    if self.player_health <= 0:
                        self.player_lives -= 1
                        self.player_health = 100
                        self.player.properties['position'] = self.entry.properties['position'].copy()  # Respawn at start
                        print(f"Respawning player. Lives left: {self.player_lives}")

                        if self.player_lives == 0:
                            print("GAME OVER!")
                            self.screen = -1  # Game over
            # Ensure exactly 5 enemies exist
            while len(self.enemies) < 5:
                ene = Object(self.shaders[0], enemyProps)
                ene.properties['position'] = np.array([
                    np.random.uniform((-self.width / 2) + 100, (self.width / 2) - 100),
                    np.random.uniform(-self.height / 2, self.height / 2),
                    0
                ], dtype=np.float32)
                
                ene.properties['velocity'] = np.array([np.random.choice([-50, 50]), 0, 0], dtype=np.float32)
                
                self.enemies.append(ene)

            # Move enemies and keep them within platform movement boundaries
            for enemy in self.enemies:
                # Reverse direction if reaching X boundaries
                if enemy.properties['position'][0] < (-self.width / 2) + 100 or enemy.properties['position'][0] > (self.width / 2) - 100:
                    enemy.properties['velocity'][0] *= -1  

                # Reverse direction if reaching Y boundaries
                if enemy.properties['position'][1] < (-self.height / 2) + 50 or enemy.properties['position'][1] > (self.height / 2) - 50:
                    enemy.properties['velocity'][1] *= -1  

                # Update enemy position (both X and Y)
                enemy.properties['position'][0] += enemy.properties['velocity'][0] * delta_time
                enemy.properties['position'][1] += enemy.properties['velocity'][1] * delta_time


            # Update player position
            self.player.properties["position"] += self.player.properties["velocity"] * delta_time
            

            #clipping player's position on screen

            self.clampPlayerPositionscene0()
            
        if self.screen == 1:
            delta_time = time['deltaTime']
            self.is_on_platform=False
            self.player.properties['velocity'][:] = 0



            for i, platform in enumerate(self.objects):  # Loop only over existing platforms
                # Reverse direction if reaching boundary
                if platform.properties['position'][0] < (-self.width / 2) + 100 or platform.properties['position'][0] > (self.width / 2) - 100:
                    platform.properties['velocity'][0] *= -1

                # Update platform position
                platform.properties['position'][0] += platform.properties['velocity'][0] * delta_time

                # Check if a key exists for this platform
                if self.keys[i] is not None:
                    key = self.keys[i]
                    key.properties['position'] = platform.properties['position'] + np.array([0, 15, 0], dtype=np.float32)

                    # Check if player collects the key
                    if np.linalg.norm(self.player.properties['position'] - key.properties['position']) < 40:
                        self.collect_key_check[i] = True
                        self.keys_collected = sum(self.collect_key_check)  # Ensure it updates properly
                        key.properties['scale'] = np.array([0, 0, 0], dtype=np.float32)  # Hide the key




            for platform in self.objects:
                platform_pos = platform.properties['position']
                player_pos = self.player.properties['position']
                
                # Collision detection (player stands on platform)
                if (abs(player_pos[0] - platform_pos[0]) < platform.properties['scale'][0] / 2 and
                    abs(player_pos[1] - platform_pos[1]) < platform.properties['scale'][1] / 2):
                    
                    self.is_on_platform = True
                    self.player.properties['position'][1] = platform_pos[1]  # Stick to platform height
                    self.player.properties['position'][2] = platform_pos[2]+ 15
                    self.player.properties['velocity'] = platform.properties['velocity'].copy()
                    break
                    

        # Apply gravity if not on a platform
            if not self.is_on_platform and (self.player.properties['position'][0]>-400 and self.player.properties['position'][0]<400):
                self.player.properties['velocity'][2] -= 300 * delta_time  # Simulate gravity

            # Jumping mechanics (if on a platform and SPACE is pressed)
            if self.is_on_platform and "SPACE" in inputs:
                self.player.properties["velocity"] = np.array([0, 250, 0], dtype=np.float32)  # Jump up

            
            #if player dies 
            if self.player.properties["position"][2] < -1:
                self.RespawnPlayer()

            #check if player collected all keys or not
            if np.linalg.norm(self.player.properties["position"] - self.exit.properties["position"]) < 40:
                if sum(self.collect_key_check)>= 3:
                    self.TransitionToNextLevel()

            # Handle player movement inputs

            if "A" in inputs:
                self.player.properties["velocity"][0] =self.player.properties["velocity"][0]+ -200
            if "S" in inputs:
                self.player.properties["velocity"][1]+= -200
            if "D" in inputs:
                self.player.properties["velocity"][0]+= 200
            if "W" in inputs:
                self.player.properties["velocity"][1]+= 200

            # Enemy collision check
            for enemy in self.enemies:
                enemy_pos = enemy.properties['position']
                player_pos = self.player.properties['position']

                distance = np.linalg.norm(player_pos - enemy_pos)
                
                if distance < 20:  # If player gets too close
                    self.player_health -= 10  # Reduce health
                    print(f"Player health: {self.player_health}")

                    if self.player_health <= 0:
                        self.player_lives -= 1
                        self.player_health = 100
                        self.player.properties['position'] = self.entry.properties['position'].copy()  # Respawn at start
                        print(f"Respawning player. Lives left: {self.player_lives}")

                        if self.player_lives == 0:
                            print("GAME OVER!")
                            self.screen = -1  # Game over
            # Ensure exactly 5 enemies exist
            while len(self.enemies) < 5:
                ene = Object(self.shaders[0], enemyProps)
                ene.properties['position'] = np.array([
                    np.random.uniform((-self.width / 2) + 100, (self.width / 2) - 100),
                    np.random.uniform(-self.height / 2, self.height / 2),
                    0
                ], dtype=np.float32)
                
                ene.properties['velocity'] = np.array([np.random.choice([-50, 50]), 0, 0], dtype=np.float32)
                
                self.enemies.append(ene)

            # Move enemies and keep them within platform movement boundaries
            for enemy in self.enemies:
                # Reverse direction if reaching X boundaries
                if enemy.properties['position'][0] < (-self.width / 2) + 100 or enemy.properties['position'][0] > (self.width / 2) - 100:
                    enemy.properties['velocity'][0] *= -1  

                # Reverse direction if reaching Y boundaries
                if enemy.properties['position'][1] < (-self.height / 2) + 50 or enemy.properties['position'][1] > (self.height / 2) - 50:
                    enemy.properties['velocity'][1] *= -1  

                # Update enemy position (both X and Y)
                enemy.properties['position'][0] += enemy.properties['velocity'][0] * delta_time
                enemy.properties['position'][1] += enemy.properties['velocity'][1] * delta_time


            # Update player position
            self.player.properties["position"] += self.player.properties["velocity"] * delta_time
            

            #clipping player's position on screen

            self.clampPlayerPositionscene1()
            
            
        
        if self.screen == 2:
            delta_time = time['deltaTime']
            self.is_on_platform=False
            self.player.properties['velocity'][:] = 0



            for i, platform in enumerate(self.objects):  # Loop only over existing platforms
                # Reverse direction if reaching boundary
                if platform.properties['position'][0] < (-self.width / 2) + 100 or platform.properties['position'][0] > (self.width / 2) - 100:
                    platform.properties['velocity'][0] *= -1

                # Update platform position
                platform.properties['position'][0] += platform.properties['velocity'][0] * delta_time

                # Check if a key exists for this platform
                if self.keys[i] is not None:
                    key = self.keys[i]
                    key.properties['position'] = platform.properties['position'] + np.array([0, 15, 0], dtype=np.float32)

                    # Check if player collects the key
                    if np.linalg.norm(self.player.properties['position'] - key.properties['position']) < 40:
                        self.collect_key_check[i] = True
                        self.keys_collected = sum(self.collect_key_check)  # Ensure it updates properly
                        key.properties['scale'] = np.array([0, 0, 0], dtype=np.float32)  # Hide the key




            for platform in self.objects:
                platform_pos = platform.properties['position']
                player_pos = self.player.properties['position']
                
                # Collision detection (player stands on platform)
                if (abs(player_pos[0] - platform_pos[0]) < platform.properties['scale'][0] / 2 and
                    abs(player_pos[1] - platform_pos[1]) < platform.properties['scale'][1] / 2):
                    
                    self.is_on_platform = True
                    self.player.properties['position'][1] = platform_pos[1]  # Stick to platform height
                    self.player.properties['position'][2] = platform_pos[2]+ 15
                    self.player.properties['velocity'] = platform.properties['velocity'].copy()
                    break
                    

        # Apply gravity if not on a platform
            if not self.is_on_platform and (self.player.properties['position'][0]>-400 and self.player.properties['position'][0]<400):
                self.player.properties['velocity'][2] -= 300 * delta_time  # Simulate gravity

            # Jumping mechanics (if on a platform and SPACE is pressed)
            if self.is_on_platform and "SPACE" in inputs:
                self.player.properties["velocity"] = np.array([0, 250, 0], dtype=np.float32)  # Jump up

            
            #if player dies 
            if self.player.properties["position"][2] < -1:
                self.RespawnPlayer()

            #check if player collected all keys or not
            if np.linalg.norm(self.player.properties["position"] - self.exit.properties["position"]) < 40:
                if sum(self.collect_key_check)>= 3:
                    self.TransitionToNextLevel()

            # Handle player movement inputs

            if "A" in inputs:
                self.player.properties["velocity"][0] =self.player.properties["velocity"][0]+ -200
            if "S" in inputs:
                self.player.properties["velocity"][1]+= -200
            if "D" in inputs:
                self.player.properties["velocity"][0]+= 200
            if "W" in inputs:
                self.player.properties["velocity"][1]+= 200

            # Enemy collision check
            for enemy in self.enemies:
                enemy_pos = enemy.properties['position']
                player_pos = self.player.properties['position']

                distance = np.linalg.norm(player_pos - enemy_pos)
                
                if distance < 20:  # If player gets too close
                    self.player_health -= 10  # Reduce health
                    print(f"Player health: {self.player_health}")

                    if self.player_health <= 0:
                        self.player_lives -= 1
                        self.player_health = 100
                        self.player.properties['position'] = self.entry.properties['position'].copy()  # Respawn at start
                        print(f"Respawning player. Lives left: {self.player_lives}")

                        if self.player_lives == 0:
                            print("GAME OVER!")
                            self.screen = -1  # Game over
            # Ensure exactly 5 enemies exist
            while len(self.enemies) < 5:
                ene = Object(self.shaders[0], enemyProps)
                ene.properties['position'] = np.array([
                    np.random.uniform((-self.width / 2) + 100, (self.width / 2) - 100),
                    np.random.uniform(-self.height / 2, self.height / 2),
                    0
                ], dtype=np.float32)
                
                ene.properties['velocity'] = np.array([np.random.choice([-50, 50]), 0, 0], dtype=np.float32)
                
                self.enemies.append(ene)

            # Move enemies and keep them within platform movement boundaries
            for enemy in self.enemies:
                # Reverse direction if reaching X boundaries
                if enemy.properties['position'][0] < (-self.width / 2) + 100 or enemy.properties['position'][0] > (self.width / 2) - 100:
                    enemy.properties['velocity'][0] *= -1  

                # Reverse direction if reaching Y boundaries
                if enemy.properties['position'][1] < (-self.height / 2) + 50 or enemy.properties['position'][1] > (self.height / 2) - 50:
                    enemy.properties['velocity'][1] *= -1  

                # Update enemy position (both X and Y)
                enemy.properties['position'][0] += enemy.properties['velocity'][0] * delta_time
                enemy.properties['position'][1] += enemy.properties['velocity'][1] * delta_time


            # Update player position
            self.player.properties["position"] += self.player.properties["velocity"] * delta_time
            

            #clipping player's position on screen

            self.clampPlayerPositionscene2()
            
            

            
    def DrawScene(self):
        if self.screen == 0:

            for shader in self.shaders:
                self.camera.Update(shader)

            self.bg.Draw()
            self.player.Draw()
            self.entry.Draw()
            self.exit.Draw()
            for key in self.keys:
                if key is not None:
                    key.Draw()
            for obj in self.objects:
                obj.Draw()
            for ene in self.enemies:
                ene.Draw()


        if self.screen==1:
            for shader in self.shaders:
                self.camera.Update(shader)

            self.bg.Draw()
            self.player.Draw()
            self.entry.Draw()
            self.exit.Draw()
            for key in self.keys:
                if key is not None:
                    key.Draw()
            for obj in self.objects:
                obj.Draw()
            for ene in self.enemies:
                ene.Draw()
   
        if self.screen==2:
            for shader in self.shaders:
                self.camera.Update(shader)

            self.bg.Draw()
            self.player.Draw()
            self.entry.Draw()
            self.exit.Draw()
            for key in self.keys:
                if key is not None:
                    key.Draw()
            for obj in self.objects:
                obj.Draw()
            for ene in self.enemies:
                ene.Draw()


            
        

